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

# def factorial_or_sqrt(n):
#     options = [(f"{int(n)}" if n.is_integer() else f"{round(n, 1)}", n)]  # Store formatted expression and its value
    
#     # Base transformations
#     if n == 9:
#         sqrt_val = math.sqrt(n)
#         options.append((f"sqrt({int(n)})", sqrt_val))
#         # Factorial after sqrt(9) = 3!
#         options.append((f"(sqrt({int(n)}))!", math.factorial(int(sqrt_val))))
#         # Negative versions of sqrt(9) and its factorial
#         options.append((f"-sqrt({int(n)})", -sqrt_val))
#         options.append((f"-((sqrt({int(n)}))!)", -math.factorial(int(sqrt_val))))
    
#     if n in [0, 3, 4]:
#         options.append((f"{int(n)}!", math.factorial(int(n))))
#         options.append((f"-{int(n)}!", -math.factorial(int(n))))

#     if n == 4:
#         sqrt_val = math.sqrt(n)
#         options.append((f"sqrt({int(n)})", sqrt_val))
#         options.append((f"-sqrt({int(n)})", -sqrt_val))
    
#     # Add negative version of the number
#     options.append((f"-{int(n)}" if n.is_integer() else f"-{round(n, 1)}", -n))

#     return options

def factorial_or_sqrt(n):
    options = [(f"{int(n)}" if n.is_integer() else f"{round(n, 1)}", n)]  # Store formatted expression and its value
    neg_options = [(f"-{int(n)}" if n.is_integer() else f"-{round(n, 1)}", -n)]  # Include negative values
    
    # Add negative versions of numbers
    options += neg_options

    # Allow both factorial and square root for 4
    if abs(n) == 4:  # Handle both positive and negative 4
        options.append((f"{int(abs(n))}!", math.factorial(int(abs(n)))))
        sqrt_val = math.sqrt(abs(n))
        options.append((f"sqrt({int(abs(n))})", sqrt_val))
    # Factorials for 0 and 3
    elif abs(n) in [0, 3]:  # Handle positive and negative cases
        options.append((f"{int(abs(n))}!", math.factorial(int(abs(n)))))

    # Square root for 9
    if abs(n) == 9:
        sqrt_val = math.sqrt(abs(n))
        options.append((f"sqrt({int(abs(n))})", sqrt_val))

    return options

def check_combinations_to_ten(numbers):
    operators = ['+', '-', '*', '/', '**']
    combinations = []
    for ops in product(operators, repeat=3):
        for a_expr, a in factorial_or_sqrt(numbers[0]):
            for b_expr, b in factorial_or_sqrt(numbers[1]):
                for c_expr, c in factorial_or_sqrt(numbers[2]):
                    for d_expr, d in factorial_or_sqrt(numbers[3]):
                        expression = f"{a} {ops[0]} {b} {ops[1]} {c} {ops[2]} {d}"
                        #print(f"Trying expression: {expression}")  # Debug statement
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                            combination = f"{a_expr} {ops[0]} {b_expr} {ops[1]} {c_expr} {ops[2]} {d_expr}"
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
