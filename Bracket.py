import math
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

    # Check if n is a valid integer for factorial calculation
    if n.is_integer() and (n in [0,3,4] or n >= 10):  # Limiting factorial to 0, 3, 4,10+
        n_int = int(n)
        factorial_val = math.factorial(n_int)
        options.append((f"{n_int}!", factorial_val))
        options.append((f"-{n_int}!", -factorial_val))

    # Check if n is non-negative for square root calculation
    if n in [4,9,16,25,36,49,64,81,100]:
        sqrt_val = math.sqrt(n)
        options.append((f"sqrt({int(n)})", sqrt_val))
        options.append((f"-sqrt({int(n)})", -sqrt_val))

        # Factorial of the square root if the square root is an integer
        if sqrt_val.is_integer() and (sqrt_val in [0,3,4] or sqrt_val >= 10):  # Limiting factorial for square root values
            sqrt_int = int(sqrt_val)
            factorial_sqrt_val = math.factorial(sqrt_int)
            options.append((f"(sqrt({int(n)}))!", factorial_sqrt_val))
            options.append((f"-((sqrt({int(n)}))!)", -factorial_sqrt_val))

    # Add negative version of the number
    options.append((f"-{int(n)}" if n.is_integer() else f"-{round(n, 1)}", -n))

    return options

def check_combinations_to_ten(numbers):
    operators = ['+', '-', '*', '/', '**']
    combinations = []
    for ops in product(operators, repeat=3):
        for a_expr, a in factorial_sqrt_neg(numbers[0]):
            for b_expr, b in factorial_sqrt_neg(numbers[1]):
                for c_expr, c in factorial_sqrt_neg(numbers[2]):
                    for d_expr, d in factorial_sqrt_neg(numbers[3]):                 
                        
                        # Case 0: A B C D 
                        expression = f"{a} {ops[0]} {b} {ops[1]} {c} {ops[2]} {d}"
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                            combination = f"{a_expr} {ops[0]} {b_expr} {ops[1]} {c_expr} {ops[2]} {d_expr}"
                            combinations.append(combination)

                        # Case 1: (AB) (CD)
                        expression_with_parens = f"({a} {ops[0]} {b}) {ops[1]} ({c} {ops[2]} {d})"
                        if parentheses_needed(expression, expression_with_parens):
                            result = safe_eval(expression_with_parens)
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"({a_expr} {ops[0]} {b_expr}) {ops[1]} ({c_expr} {ops[2]} {d_expr})"
                                combinations.append(combination)
                       
                        # Case 2: ((AB) C)  D
                        expression_with_parens = f"(({a} {ops[0]} {b}) {ops[1]} {c}) {ops[2]} {d}"
                        if parentheses_needed(expression, expression_with_parens):
                            result = safe_eval(expression_with_parens)
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"(({a_expr} {ops[0]} {b_expr}) {ops[1]} {c_expr}) {ops[2]} {d_expr}"
                                combinations.append(combination)

                        # Case 3: (A (BC)) D
                        expression_with_parens = f"({a} {ops[0]} ({b} {ops[1]} {c})) {ops[2]} {d}"
                        if parentheses_needed(expression, expression_with_parens):
                            result = safe_eval(expression_with_parens)
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"({a_expr} {ops[0]} ({b_expr} {ops[1]} {c_expr})) {ops[2]} {d_expr}"
                                combinations.append(combination)

                        # Case 4: A ((BC) D)
                        expression_with_parens = f"{a} {ops[0]} (({b} {ops[1]} {c}) {ops[2]} {d})"
                        if parentheses_needed(expression, expression_with_parens):
                            result = safe_eval(expression_with_parens)
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"{a_expr} {ops[0]} (({b_expr} {ops[1]} {c_expr}) {ops[2]} {d_expr})"
                                combinations.append(combination)

                        # Case 5: A (B (CD))
                        expression_with_parens = f"{a} {ops[0]} ({b} {ops[1]} ({c} {ops[2]} {d}))"
                        if parentheses_needed(expression, expression_with_parens):
                            result = safe_eval(expression_with_parens)
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"{a_expr} {ops[0]} ({b_expr} {ops[1]} ({c_expr} {ops[2]} {d_expr}))"
                                combinations.append(combination) 

    return combinations

def main():
    try:
        A = float(input("Enter value for A: "))
        B = float(input("Enter value for B: "))
        C = float(input("Enter value for C: "))
        D = float(input("Enter value for D: "))

        numbers = [A, B, C, D]
        combinations = check_combinations_to_ten(numbers)
        
        if combinations:
            print(f"The possible combinations of {int(A)}, {int(B)}, {int(C)}, and {int(D)} (including factorials, square roots, and negatives) that result in 10 are:")
            for combination in combinations:
                print(combination)
        else:
            print(f"There are no combinations of {int(A)}, {int(B)}, {int(C)}, and {int(D)} (including factorials, square roots, and negatives) that result in 10.")
    except ValueError:
        print("Please enter valid numbers for A, B, C, and D.")

if __name__ == "__main__":
    main()


#3! / (-5 + 7) + 7