import math
from itertools import product

def safe_eval(expression):
    try:3
        result = eval(expression)
        if isinstance(result, complex):  # Ignore complex results
            return None
        if isinstance(result, (int, float)) and (result > 1e308 or result < -1e308):  # Prevent overflow
            return None
        return result
    except (ZeroDivisionError, OverflowError, ValueError, SyntaxError):
        return None

def factorial_or_sqrt(n):
    options = [(f"{int(n)}" if n.is_integer() else f"{round(n, 1)}", n)]  # Store formatted expression and its value
    if n >= 0 and n == int(n):  # Factorial is defined for non-negative integers
        if n <= 20:  # Limit factorial to prevent overly large results
            options.append((f"{int(n)}!", math.factorial(int(n))))
    if n >= 0:  # Square root is only defined for non-negative numbers
        sqrt_val = math.sqrt(n)
        options.append((f"sqrt({int(n)})" if sqrt_val.is_integer() else f"sqrt({round(n, 1)})", sqrt_val))
    return options

def check_combinations_to_ten(numbers):
    operators = ['+', '-', '*', '/', '**']
    combinations = []
    
    for ops in product(operators, repeat=3):
        for a_expr, a in factorial_or_sqrt(numbers[0]):
            for b_expr, b in factorial_or_sqrt(numbers[1]):
                for c_expr, c in factorial_or_sqrt(numbers[2]):
                    for d_expr, d in factorial_or_sqrt(numbers[3]):
                        # Check if any operand exceeds reasonable limits
                        if any(abs(x) > 1e6 for x in (a, b, c, d)):
                            continue

                        # Case 1: (((A) o1 (B)) o2 ((C) o3 (D)))
                        expression = f"(({a} {ops[0]} {b}) {ops[1]} ({c} {ops[2]} {d}))"
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                            combination = f"(({a_expr} {ops[0]} {b_expr}) {ops[1]} ({c_expr} {ops[2]} {d_expr}))"
                            combinations.append(combination)

                        # Case 2: ((((A) o1 (B)) o2 (C)) o3 (D))
                        expression = f"((({a} {ops[0]} {b}) {ops[1]} {c}) {ops[2]} {d})"
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                            combination = f"((({a_expr} {ops[0]} {b_expr}) {ops[1]} {c_expr}) {ops[2]} {d_expr})"
                            combinations.append(combination)

                        # Case 3: (((A) o1 ((B) o2 (C))) o3 (D))
                        expression = f"(({a} {ops[0]} ({b} {ops[1]} {c})) {ops[2]} {d})"
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                            combination = f"(({a_expr} {ops[0]} ({b_expr} {ops[1]} {c_expr})) {ops[2]} {d_expr})"
                            combinations.append(combination)

                        # Case 4: ((A) o1 (((B) o2 (C)) o3 (D)))
                        expression = f"({a} {ops[0]} (({b} {ops[1]} {c}) {ops[2]} {d}))"
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                            combination = f"({a_expr} {ops[0]} (({b_expr} {ops[1]} {c_expr}) {ops[2]} {d_expr}))"
                            combinations.append(combination)

                        # Case 5: ((A) o1 ((B) o2 ((C) o3 (D))))
                        expression = f"({a} {ops[0]} ({b} {ops[1]} ({c} {ops[2]} {d})))"
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                            combination = f"({a_expr} {ops[0]} ({b_expr} {ops[1]} ({c_expr} {ops[2]} {d_expr})))"
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
            print(f"The possible combinations of {int(A)}, {int(B)}, {int(C)}, and {int(D)} (including factorials, square roots, and bracket placements) that add, subtract, multiply, divide, or exponentiate to equal 10 are:")
            for combination in combinations:
                print(combination)
        else:
            print(f"There are no combinations of {int(A)}, {int(B)}, {int(C)}, and {int(D)} (including factorials, square roots, and bracket placements) that add, subtract, multiply, divide, or exponentiate to equal 10.")
    except ValueError:
        print("Please enter valid numbers for A, B, C, and D.")

if __name__ == "__main__":
    main()
