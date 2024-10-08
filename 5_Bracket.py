import math
import time
from itertools import product

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
        #print(f"Error evaluating expression '{expression}': {e}")
        return None

def parentheses_needed(expression_without_parens, expression_with_parens):
    result_without_parens = safe_eval(expression_without_parens)
    result_with_parens = safe_eval(expression_with_parens)

    # If either result is None (due to an invalid expression), parentheses are considered necessary
    if result_without_parens is None or result_with_parens is None:
        return True

    # Compare the results, if they are not close, parentheses are necessary
    return not math.isclose(result_without_parens, result_with_parens, rel_tol=1e-9)

def factorial_sqrt_neg(n):
    options = [(f"{int(n)}" if n.is_integer() else f"{round(n, 1)}", n)]  # Store formatted expression and its value
    # Add negative version of the number
    options.append((f"-{int(n)}" if n.is_integer() else f"-{round(n, 1)}", -n))
    
    
    # Check if n is a valid integer for factorial calculation
    #if n.is_integer() and (n in [0,3,4,5,6] or n >= 10):  # Limiting factorial to 0, 3, 4,10+
    n_int = int(n)
    factorial_val = math.factorial(n_int)
    options.append((f"{n_int}!", factorial_val))
    options.append((f"-{n_int}!", -factorial_val))

    factorial_int = int(factorial_val)
    sqrt_factorial_val = math.sqrt(factorial_int)
    options.append((f"sqrt({n_int}!)", sqrt_factorial_val))
    options.append((f"-sqrt({n_int}!)", -sqrt_factorial_val))

    # Check if n is non-negative for square root calculation
    #if n in [4,9,16,25,36,49,64,81,100] or n > 100:
    sqrt_val = math.sqrt(n)
    options.append((f"sqrt({n_int})", sqrt_val))
    options.append((f"-sqrt({n_int})", -sqrt_val))

    # Factorial of the square root if the square root is an integer
    #if sqrt_val.is_integer() and (sqrt_val in [0,3,4,5,6] or sqrt_val >= 10):  # Limiting factorial for square root values
    sqrt_float = sqrt_val
    if sqrt_float.is_integer():
        factorial_sqrt_val = math.factorial(sqrt_float)
    else:
        factorial_sqrt_val = sqrt_float
    options.append((f"(sqrt({n_int}))!", factorial_sqrt_val))
    options.append((f"-((sqrt({n_int}))!)", -factorial_sqrt_val))

    return options

def check_combinations_to_ten(numbers):
    operators = ['+', '-', '*', '/', '**']
    combinations = []
    total_tested = 0
    for ops in product(operators, repeat=3):
        for a_expr, a in factorial_sqrt_neg(numbers[0]):
            for b_expr, b in factorial_sqrt_neg(numbers[1]):
                for c_expr, c in factorial_sqrt_neg(numbers[2]):
                    for d_expr, d in factorial_sqrt_neg(numbers[3]):                 
                        
                        # Case 0: A B C D 
                        expression = f"{a} {ops[0]} {b} {ops[1]} {c} {ops[2]} {d}"
                        total_tested += 1
                        result = safe_eval(expression)
                        if result is not None and result == 10:  # Checking for exact equality
                            combination = f"{a_expr} {ops[0]} {b_expr} {ops[1]} {c_expr} {ops[2]} {d_expr}"
                            combinations.append(combination)

                        # Case 1: (AB) (CD)
                        expression_with_parens = f"({a} {ops[0]} {b}) {ops[1]} ({c} {ops[2]} {d})"
                        total_tested += 1
                        # if parentheses_needed(expression, expression_with_parens):
                        result = safe_eval(expression_with_parens)
                        if result is not None and result == 10:  # Checking for exact equality
                            combination = f"({a_expr} {ops[0]} {b_expr}) {ops[1]} ({c_expr} {ops[2]} {d_expr})"
                            combinations.append(combination)
                    
                        # Case 2: ((AB) C)  D
                        expression_with_parens = f"(({a} {ops[0]} {b}) {ops[1]} {c}) {ops[2]} {d}"
                        total_tested += 1
                        # if parentheses_needed(expression, expression_with_parens):
                        result = safe_eval(expression_with_parens)
                        if result is not None and result == 10:  # Checking for exact equality
                            combination = f"(({a_expr} {ops[0]} {b_expr}) {ops[1]} {c_expr}) {ops[2]} {d_expr}"
                            combinations.append(combination)

                        # Case 3: (A (BC)) D
                        expression_with_parens = f"({a} {ops[0]} ({b} {ops[1]} {c})) {ops[2]} {d}"
                        total_tested += 1
                        # if parentheses_needed(expression, expression_with_parens):
                        result = safe_eval(expression_with_parens)
                        if result is not None and result == 10:  # Checking for exact equality
                            combination = f"({a_expr} {ops[0]} ({b_expr} {ops[1]} {c_expr})) {ops[2]} {d_expr}"
                            combinations.append(combination)

                        # Case 4: A ((BC) D)
                        expression_with_parens = f"{a} {ops[0]} (({b} {ops[1]} {c}) {ops[2]} {d})"
                        total_tested += 1
                        # if parentheses_needed(expression, expression_with_parens):
                        result = safe_eval(expression_with_parens)
                        if result is not None and result == 10:  # Checking for exact equality
                            combination = f"{a_expr} {ops[0]} (({b_expr} {ops[1]} {c_expr}) {ops[2]} {d_expr})"
                            combinations.append(combination)

                        # Case 5: A (B (CD))
                        expression_with_parens = f"{a} {ops[0]} ({b} {ops[1]} ({c} {ops[2]} {d}))"
                        total_tested += 1
                        # if parentheses_needed(expression, expression_with_parens):
                        result = safe_eval(expression_with_parens)
                        if result is not None and result == 10:  # Checking for exact equality
                            combination = f"{a_expr} {ops[0]} ({b_expr} {ops[1]} ({c_expr} {ops[2]} {d_expr}))"
                            combinations.append(combination) 

    return combinations, total_tested

def main():
    try:
        A = float(input("Enter value for A: "))
        B = float(input("Enter value for B: "))
        C = float(input("Enter value for C: "))
        D = float(input("Enter value for D: "))

        numbers = [A, B, C, D]
        combinations, total_tested = check_combinations_to_ten(numbers)

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