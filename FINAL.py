import math
import time
from itertools import product

total_tested = 0  # Counter for the total combinations tested

def safe_eval(expression):
    try:
        # Prevent overly large results by checking for large exponents
        if "**" in expression:
            base, exponent = expression.split("**")
            base = float(base.strip())
            exponent = float(exponent.strip())
            if base > 100 or exponent > 10:
                raise OverflowError("Result too large")
        
        return eval(expression)
    except (ZeroDivisionError, OverflowError, ValueError, SyntaxError) as e:
        print(f"Error evaluating expression '{expression}': {e}")
        return None

def parentheses_needed(expression_without_parens, expression_with_parens):
    result_without_parens = safe_eval(expression_without_parens)
    result_with_parens = safe_eval(expression_with_parens)

    # If either result is None (due to an invalid expression), parentheses are considered necessary
    if result_without_parens is None or result_with_parens is None:
        return True

    # Compare the results, if they are not close, parentheses are necessary
    return not math.isclose(result_without_parens, result_with_parens, rel_tol=1e-9)

def factorial_sqrt_neg(str_n, n):
    global total_tested
    n = abs(n)
    options=[]
    options.append((f"{str_n}" if n.is_integer() else f"{round(n, 1)}", n)) # Store formatted expression and its value
    options.append((f"-{str_n}" if n.is_integer() else f"-{round(n, 1)}", -n))     # Add negative version of the number

    # Check if n is a valid integer for factorial calculation
    if n.is_integer() and (n in [0,3,4,5,6,7,8,9]):  # Limiting factorial to 0, 3, 4,10+
        factorial_val = math.factorial(int(n))
        options.append((f"{str_n}!", factorial_val))
        options.append((f"-{str_n}!", -factorial_val))

        if factorial_val in [4,9,16,25,36,49,64,81,100,144,169,196,225]:
            factorial_int = int(factorial_val)
            sqrt_factorial_val = math.sqrt(factorial_int)
            options.append((f"sqrt({str_n}!)", sqrt_factorial_val))
            options.append((f"-sqrt({str_n}!)", -sqrt_factorial_val))
        else:
            total_tested += 1
    else:
        total_tested += 1

    # Check if n is non-negative for square root calculation
    if n in [4,9,16,25,36,49,64,81,100,144,169,196,225]:
        sqrt_val = math.sqrt(n)
        options.append((f"sqrt({str_n})", sqrt_val))
        options.append((f"-sqrt({str_n})", -sqrt_val))

        # Factorial of the square root if the square root is an integer
        if sqrt_val.is_integer() and (sqrt_val in [0,3,4,5,6,7,8,9]):  # Limiting factorial for square root values
            if sqrt_val.is_integer():
                sqrt_val = int(sqrt_val)
                factorial_sqrt_val = math.factorial(sqrt_val)
            else:
                factorial_sqrt_val = sqrt_val
            
            options.append((f"sqrt({str_n})!", factorial_sqrt_val))
            options.append((f"- sqrt({str_n})!", -factorial_sqrt_val))
        
        else:
            total_tested += 1
    else:
        total_tested += 1
    
    return options

def check_combinations_to_ten(numbers, str_numbers):
    global total_tested
    operators = ['+', '-', '*', '/', '**']
    combinations = []
    for ops in product(operators, repeat=3):
        for a_expr, a in factorial_sqrt_neg(str_numbers[0], numbers[0]):
            for b_expr, b in factorial_sqrt_neg(str_numbers[1],numbers[1]):
                for c_expr, c in factorial_sqrt_neg(str_numbers[2],numbers[2]):
                    for d_expr, d in factorial_sqrt_neg(str_numbers[3],numbers[3]):                 
                        
                        # Case 0: A B C D 
                        expression = f"{a} {ops[0]} {b} {ops[1]} {c} {ops[2]} {d}"
                        combination = f"{a_expr} {ops[0]} {b_expr} {ops[1]} {c_expr} {ops[2]} {d_expr}"
                        total_tested += 1
                        result = safe_eval(expression)
                        if result is not None and result == 10:  # Checking for exact equality
                            combinations.append(combination)
                        if result == 100:
                            ABCD_combination = f"sqrt({combination})"
                            combinations.append(ABCD_combination)
                        
                        a = float(a)
                        b = float(b)
                        c = float(c)
                        d = float(d)
                        ab_expression = f"{a} {ops[0]} {b}"
                        bc_expression = f"{b} {ops[1]} {d}"
                        cd_expression = f"{c} {ops[2]} {d}"
                        # print(f"Evaluating AB: {ab_expression} -> {ab_result}")
                        # print(f"Evaluating CD: {cd_expression} -> {cd_result}")
                        ab_combination = f"({a_expr} {ops[0]} {b_expr})" 
                        bc_combination = f"({b_expr} {ops[1]} {c_expr})"                          
                        cd_combination = f"({c_expr} {ops[2]} {d_expr})"
                        ab_result = safe_eval(ab_expression)
                        bc_result = safe_eval(bc_expression)
                        cd_result = safe_eval(cd_expression)                        
                        
                        if ab_result is not None and bc_result is not None and cd_result is not None:
                        
                            # Case 1 with AB CD factorial_sqrt_neg                                              
                            # Ensure ab_expression and cd_expression are valid before proceeding
                            for ab_expr, ab in factorial_sqrt_neg(ab_combination, ab_result):
                                for bc_expr, bc in factorial_sqrt_neg(bc_combination, bc_result):
                                    for cd_expr, cd in factorial_sqrt_neg(cd_combination, cd_result):
                                        # Case 1: (ab) (cd)          
                                        expression_with_parens = f"{ab} {ops[1]} {cd}"
                                        combination = f"{ab_expr} {ops[1]} {cd_expr}"
                                        total_tested += 1
                                        print(total_tested)
                                        # print(f"Combining: {ab_expr} {ops[1]} {cd_expr} -> {expression_with_parens}")
                                        # Evaluate the expression and check if it equals 10 or sqrt(100)
                                        result = safe_eval(expression_with_parens)                  
                                        if result is not None and result == 10:  # Checking for exact equality
                                            combinations.append(combination)
                                        if result == 100:
                                            ABCD_combination = f"sqrt({combination})"
                                            combinations.append(ABCD_combination)          
                                                                                      
                                        ab = float(ab)
                                        bc = float(bc)
                                        cd = float(cd)
                                        
                                        abC_expression = f"{ab} {ops[1]} {c}"
                                        Abc_expression = f"{a} {ops[0]} {bc}"
                                        bcD_expression = f"{bc} {ops[2]} {d}"
                                        Bcd_expression = f"{b} {ops[1]} {cd}"
                                        
                                        abC_combination = f"({ab_expr} {ops[1]} {c_expr})"
                                        Abc_combination = f"({a_expr} {ops[0]} {bc_expr})"
                                        bcD_combination = f"({bc_expr} {ops[2]} {d_expr})"
                                        Bcd_combination = f"({b_expr} {ops[1]} {cd_expr})"
                                         
                                        abC_result = safe_eval(abC_expression)
                                        Abc_result = safe_eval(Abc_expression)
                                        bcD_result = safe_eval(bcD_expression)
                                        Bcd_result = safe_eval(Bcd_expression)
                                        
                                        if abC_result is not None and Abc_result is not None and bcD_result is not None and Bcd_result is not None:
                                            
                                            # Case 2 with AB ABC factorial_sqrt_neg
                                            for abC_expr, abC in factorial_sqrt_neg(abC_combination, abC_result):
                                                expression_with_parens = f"{abC} {ops[2]} {d}"
                                                combination = f"{abC_expr} {ops[2]} {d_expr}"
                                                total_tested += 1
                                                #if parentheses_needed(expression, expression_with_parens):
                                                result = safe_eval(expression_with_parens)
                                                if result is not None and result == 10:  # Checking for exact equality
                                                    combinations.append(combination)         
                                                if result == 100:
                                                    ABCD_combination = f"sqrt({combination})"
                                                    combinations.append(ABCD_combination)

                                            # Case 3 with BC ABC factorial_sqrt_neg
                                            for Abc_expr, Abc in factorial_sqrt_neg(Abc_combination, Abc_result):
                                                expression_with_parens = f"{Abc} {ops[2]} {d}"
                                                combination = f"{Abc_expr} {ops[2]} {d_expr}"
                                                total_tested += 1
                                                #if parentheses_needed(expression, expression_with_parens):
                                                result = safe_eval(expression_with_parens)
                                                if result is not None and result == 10:  # Checking for exact equality
                                                    combinations.append(combination)          
                                                if result == 100:
                                                    ABCD_combination = f"sqrt({combination})"
                                                    combinations.append(ABCD_combination)
                                                
                                            # Case 4 with BC BCD factorial_sqrt_neg
                                            for bcD_expr, bcD in factorial_sqrt_neg(bcD_combination, bcD_result):
                                                expression_with_parens = f"{a} {ops[0]} {bcD}"
                                                combination = f"{a_expr} {ops[0]} {bcD_expr}"                       
                                                total_tested += 1
                                                #if parentheses_needed(expression, expression_with_parens):
                                                result = safe_eval(expression_with_parens)
                                                if result is not None and result == 10:  # Checking for exact equality
                                                    combinations.append(combination)            
                                                if result == 100:
                                                    ABCD_combination = f"sqrt({combination})"
                                                    combinations.append(ABCD_combination)       

                                            # Case 5 with CD BCD factorial_sqrt_neg
                                            for Bcd_expr, Bcd in factorial_sqrt_neg(Bcd_combination, Bcd_result):
                                                expression_with_parens = f"{a} {ops[0]} {Bcd}"
                                                combination = f"{a_expr} {ops[0]} {Bcd_expr}"                       
                                                total_tested += 1
                                                #if parentheses_needed(expression, expression_with_parens):
                                                result = safe_eval(expression_with_parens)
                                                if result is not None and result == 10:  # Checking for exact equality
                                                    combinations.append(combination)         
                                                if result == 100:
                                                    ABCD_combination = f"sqrt({combination})"
                                                    combinations.append(ABCD_combination)

    return combinations

def main():
    try:
        A = float(input("Enter value for A: "))
        B = float(input("Enter value for B: "))
        C = float(input("Enter value for C: "))
        D = float(input("Enter value for D: "))

        str_A = str(A)
        str_B = str(B)
        str_C = str(C)
        str_D = str(D)

        numbers = [A, B, C, D]
        str_numbers = [str_A, str_B, str_C, str_D]
        global total_tested
        
        combinations = check_combinations_to_ten(numbers, str_numbers)
        
        if combinations:
            print(f"The possible combinations of {int(A)}, {int(B)}, {int(C)}, and {int(D)} (including factorials, square roots, and negatives) that result in 10 are:")
            for combination in combinations:
                print(combination)
            print("Total Number of Combinations:",len(combinations))
        else:
            print(f"There are no combinations of {int(A)}, {int(B)}, {int(C)}, and {int(D)} (including factorials, square roots, and negatives) that result in 10.")
        
        print(f"Total Number of Combinations Tested: {total_tested}")

    except ValueError:
        print("Please enter valid numbers for A, B, C, and D.")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))