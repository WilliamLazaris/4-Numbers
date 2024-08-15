import math
from itertools import product

def safe_eval(expression):
    try:
        return eval(expression)
    except (ZeroDivisionError, OverflowError, ValueError):
        return None

def factorial_or_sqrt(n):
    options = [n]
    if n >= 0 and n == int(n):  # Factorial is only defined for non-negative integers
        options.append(math.factorial(int(n)))
    if n >= 0:  # Square root is only defined for non-negative numbers
        options.append(math.sqrt(n))
    return options

def check_combinat0ions_to_ten(numbers):
    operators = ['+', '-', '*', '/', '**']
    combinations = []
    for a in factorial_or_sqrt(numbers[0]):
        for b in factorial_or_sqrt(numbers[1]):
            for c in factorial_or_sqrt(numbers[2]):
                for d in factorial_or_sqrt(numbers[3]):
                    for ops in product(operators, repeat=3):
                        expression = f"{numbers[0]} {ops[0]} {numbers[1]} {ops[1]} {numbers[2]} {ops[2]} {numbers[3]}"
                        result = safe_eval(expression)
                        if result is not None and math.isclose(result, 10, rel_tol=1e-9):  # Using isclose for float comparison
                            combinations.append(expression)
    return combinations

def main():
    try:
        A = int(input("Enter value for A: "))
        B = int(input("Enter value for B: "))
        C = int(input("Enter value for C: "))
        D = int(input("Enter value for D: "))

        numbers = [A, B, C, D]
        combinations = check_combinations_to_ten(numbers)
        
        if combinations:
            print(f"The possible combinations of {A}, {B}, {C}, and {D} that add, subtract, multiply, divide, or exponentiate to equal 10 are:")
            for combination in combinations:
                print(combination)
        else:
            print(f"There are no combinations of {A}, {B}, {C}, and {D} that add, subtract, multiply, divide, or exponentiate to equal 10.")
    except ValueError:
        print("Please enter valid integers for A, B, C, and D.")

if __name__ == "__main__":
    main()

# Case 1: (((A) o1 (B)) o2 ((C) o3 (D)))
# Case 2: ((((A) o1 (B)) o2 (C)) o3 (D))
# Case 3: (((A) o1 ((B) o2 (C))) o3 (D))
# Case 4: ((A) o1 (((B) o2 (C)) o3 (D)))
# Case 5: ((A) o1 ((B) o2 ((C) o3 (D))))

# 6 Cases for A: A, -A, A!, -(A!), sqrt(A), -sqrt(A)