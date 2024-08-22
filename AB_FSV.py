import math
from itertools import product

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
    if n.is_integer() and (n in [0,3,4,5,6] or n >= 10):  # Limiting factorial to 0, 3, 4,10+
        n_int = int(n)
        factorial_val = math.factorial(n_int)
        options.append((f"{n_int}!", factorial_val))
        options.append((f"-{n_int}!", -factorial_val))

    # Check if n is non-negative for square root calculation
    if n in [4,9,16,25,36,49,64,81,100] or n > 100:
        sqrt_val = math.sqrt(n)
        options.append((f"sqrt({int(n)})", sqrt_val))
        options.append((f"-sqrt({int(n)})", -sqrt_val))

        # Factorial of the square root if the square root is an integer
        if sqrt_val.is_integer() and (sqrt_val in [0,3,4,5,6] or sqrt_val >= 10):  # Limiting factorial for square root values
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
    total_tested = 0  # Counter for the total combinations tested
    for ops in product(operators, repeat=3):
        for a_expr, a in factorial_sqrt_neg(numbers[0]):
            for b_expr, b in factorial_sqrt_neg(numbers[1]):
                for c_expr, c in factorial_sqrt_neg(numbers[2]):
                    for d_expr, d in factorial_sqrt_neg(numbers[3]):                 
                        
                        # Case 0: A B C D 
                        case_0(ops, a_expr, b_expr, c_expr, d_expr, a, b, c, d, total_tested, combinations)
                        expression, total_tested, combinations = case_0(ops, a_expr, b_expr, c_expr, d_expr, a, b, c, d, total_tested, combinations)

                        # Case 1: (AB) (CD)
                        case_1(ops, a, b, c, d, total_tested, combinations, expression)
                        total_tested, combinations = case_1(ops, a, b, c, d, total_tested, combinations, expression)

                        # Case 2: ((AB) C) D
                        case_2(ops, a, b, c, d, total_tested, combinations, expression)
                        total_tested, combinations = case_2(ops, a, b, c, d, total_tested, combinations, expression)

                        # Case 3: (A (BC)) D
                        case_3(ops, a_expr, a, b, c, d, total_tested, combinations, expression)
                        total_tested, combinations = case_3(ops, a_expr, a, b, c, d, total_tested, combinations, expression)

                        # Case 4: A ((BC) D)
                        case_4(ops, a_expr, a, b, c, d, total_tested, combinations, expression)
                        total_tested, combinations = case_4(ops, a_expr, a, b, c, d, total_tested, combinations, expression)

                        # Case 5: A (B (CD))0
                        case_5(ops, a_expr, b_expr, a, b, c, d, total_tested, combinations, expression)
                        total_tested, combinations = case_5(ops, a_expr, b_expr, a, b, c, d, total_tested, combinations, expression)

    return combinations, total_tested

def case_0(ops, a_expr, b_expr, c_expr, d_expr, a, b, c, d, total_tested, combinations):
    expression = f"{a} {ops[0]} {b} {ops[1]} {c} {ops[2]} {d}"
    total_tested += 1
    result = safe_eval(expression)

    if result is not None:
        # Check if the result is close to 10
        if math.isclose(result, 10, rel_tol=1e-9):
            combination = f"{a_expr} {ops[0]} {b_expr} {ops[1]} {c_expr} {ops[2]} {d_expr}"
            combinations.append(combination)

        # Check if sqrt(result) is close to 10 (only for non-negative results)
        if result >= 0:
            sqrt_result = math.sqrt(result)
            if math.isclose(sqrt_result, 10, rel_tol=1e-9):
                combination = f"sqrt({a_expr} {ops[0]} {b_expr} {ops[1]} {c_expr} {ops[2]} {d_expr})"
                combinations.append(combination)
    return total_tested, combinations

def case_1(ops, a, b, c, d, total_tested, combinations, expression):
    expression_with_parens = f"({a} {ops[0]} {b}) {ops[1]} ({c} {ops[2]} {d})"
    total_tested += 1
    if parentheses_needed(expression, expression_with_parens):
        result = safe_eval(expression_with_parens)

        if result is not None:
            # Evaluate AB and CD sub-expressions
            ab_result = safe_eval(f"{a} {ops[0]} {b}")
            cd_result = safe_eval(f"{c} {ops[2]} {d}")
            
            # If AB and CD are valid results, apply factorial_sqrt_neg on them
            if ab_result is not None and cd_result is not None:
                ab_options = factorial_sqrt_neg(ab_result)
                cd_options = factorial_sqrt_neg(cd_result)

                # Loop through all combinations of AB and CD options
                for ab_expr, ab_val in ab_options:
                    for cd_expr, cd_val in cd_options:
                        # Create the new expression using AB and CD options
                        expression_with_parens = f"({ab_val}) {ops[1]} ({cd_val})"
                        total_tested += 1
                        result = safe_eval(expression_with_parens)

                        if result is not None:  # Ensure result is not None before further checks
                                                                
                            # Check if result == 10
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"({ab_expr}) {ops[1]} ({cd_expr})"
                                combinations.append(combination)

                            # Check if sqrt(result) == 10 (only for non-negative results)
                            if result is not None and result >= 0:
                                sqrt_result = math.sqrt(result)
                                if math.isclose(sqrt_result, 10, rel_tol=1e-9):
                                    combination = f"sqrt(({ab_expr}) {ops[1]} ({cd_expr}))"
                                    combinations.append(combination)
    return total_tested, combinations

def case_2(ops, a, b, c, d, total_tested, combinations, expression):
    expression_with_parens = f"(({a} {ops[0]} {b}) {ops[1]} {c}) {ops[2]} {d}"
    total_tested += 1
    if parentheses_needed(expression, expression_with_parens):
        result = safe_eval(expression_with_parens)

        if result is not None:
            # Evaluate AB, ABC and CD
            ab_result = safe_eval(f"{a} {ops[0]} {b}")
            abc_result = safe_eval(f"({a} {ops[0]} {b}) {ops[1]} {c}")
            cd_result = safe_eval(f"{c} {ops[2]} {d}")

            # Apply factorial_sqrt_neg on AB, ABC, and CD
            if ab_result is not None and abc_result is not None and cd_result is not None:
                ab_options = factorial_sqrt_neg(ab_result)
                abc_options = factorial_sqrt_neg(abc_result)
                cd_options = factorial_sqrt_neg(cd_result)

                # Loop through AB, ABC, and CD options
                for ab_expr, ab_val in ab_options:
                    for abc_expr, abc_val in abc_options:
                        for cd_expr, cd_val in cd_options:
                            expression_with_parens = f"(({ab_val}) {ops[1]} {abc_val}) {ops[2]} {cd_val}"
                            total_tested += 1
                            result = safe_eval(expression_with_parens)

                            if result is not None:  # Ensure result is not None before further checks

                                # Check if result == 10
                                if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                    combination = f"(({ab_expr}) {ops[1]} {abc_expr}) {ops[2]} {cd_expr}"
                                    combinations.append(combination)

                                # Check sqrt(result) == 10
                                if result >= 0:
                                    sqrt_result = math.sqrt(result)
                                    if math.isclose(sqrt_result, 10, rel_tol=1e-9):
                                        combination = f"sqrt(({ab_expr}) {ops[1]} {abc_expr}) {ops[2]} {cd_expr})"
                                        combinations.append(combination)
    return total_tested, combinations                      

def case_3(ops, a_expr, a, b, c, d, total_tested, combinations, expression):
    expression_with_parens = f"({a} {ops[0]} ({b} {ops[1]} {c})) {ops[2]} {d}"
    total_tested += 1
    if parentheses_needed(expression, expression_with_parens):
        result = safe_eval(expression_with_parens)

        if result is not None:
            # Evaluate BC, ABC
            bc_result = safe_eval(f"{b} {ops[1]} {c}")
            abc_result = safe_eval(f"{a} {ops[0]} ({b} {ops[1]} {c})")

            # Apply factorial_sqrt_neg on BC, ABC
            if bc_result is not None and abc_result is not None:
                bc_options = factorial_sqrt_neg(bc_result)
                abc_options = factorial_sqrt_neg(abc_result)

                # Loop through BC and ABC options
                for bc_expr, bc_val in bc_options:
                    for abc_expr, abc_val in abc_options:
                        expression_with_parens = f"({a} {ops[0]} ({bc_val})) {ops[2]} {abc_val}"
                        total_tested += 1
                        result = safe_eval(expression_with_parens)

                        if result is not None:  # Ensure result is not None before further checks

                            # Check if result == 10
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"({a_expr} {ops[0]} ({bc_expr})) {ops[2]} {abc_expr}"
                                combinations.append(combination)

                            # Check sqrt(result) == 10
                            if result >= 0:
                                sqrt_result = math.sqrt(result)
                                if math.isclose(sqrt_result, 10, rel_tol=1e-9):
                                    combination = f"sqrt(({a_expr} {ops[0]} ({bc_expr})) {ops[2]} {abc_expr})"
                                    combinations.append(combination)
    return total_tested, combinations

def case_4(ops, a_expr, a, b, c, d, total_tested, combinations, expression):
    expression_with_parens = f"{a} {ops[0]} (({b} {ops[1]} {c}) {ops[2]} {d})"
    total_tested += 1
    if parentheses_needed(expression, expression_with_parens):
        result = safe_eval(expression_with_parens)

        if result is not None:
            # Evaluate BC, ABC, BCD
            bc_result = safe_eval(f"{b} {ops[1]} {c}")
            bcd_result = safe_eval(f"({b} {ops[1]} {c}) {ops[2]} {d}")

            # Apply factorial_sqrt_neg on BC and BCD
            if bc_result is not None and bcd_result is not None:
                bc_options = factorial_sqrt_neg(bc_result)
                bcd_options = factorial_sqrt_neg(bcd_result)

                # Loop through BC and BCD options
                for bc_expr, bc_val in bc_options:
                    for bcd_expr, bcd_val in bcd_options:
                        expression_with_parens = f"{a} {ops[0]} (({bc_val}) {ops[2]} {bcd_val})"
                        total_tested += 1
                        result = safe_eval(expression_with_parens)

                        if result is not None:  # Ensure result is not None before further checks
                            # Check if result == 10
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"{a_expr} {ops[0]} (({bc_expr}) {ops[2]} {bcd_expr})"
                                combinations.append(combination)

                            # Check sqrt(result) == 10
                            if result >= 0:
                                sqrt_result = math.sqrt(result)
                                if math.isclose(sqrt_result, 10, rel_tol=1e-9):
                                    combination = f"sqrt({a_expr} {ops[0]} (({bc_expr}) {ops[2]} {bcd_expr}))"
                                    combinations.append(combination)
    return total_tested, combinations

def case_5(ops, a_expr, b_expr, a, b, c, d, total_tested, combinations, expression):
    expression_with_parens = f"{a} {ops[0]} ({b} {ops[1]} ({c} {ops[2]} {d}))"
    total_tested += 1
    if parentheses_needed(expression, expression_with_parens):
        result = safe_eval(expression_with_parens)

        if result is not None:
            # Evaluate CD, ABC, BCD
            cd_result = safe_eval(f"{c} {ops[2]} {d}")
            bcd_result = safe_eval(f"{b} {ops[1]} ({c} {ops[2]} {d})")

            # Apply factorial_sqrt_neg on CD and BCD
            if cd_result is not None and bcd_result is not None:
                cd_options = factorial_sqrt_neg(cd_result)
                bcd_options = factorial_sqrt_neg(bcd_result)

                # Loop through CD and BCD options
                for cd_expr, cd_val in cd_options:
                    for bcd_expr, bcd_val in bcd_options:
                        expression_with_parens = f"{a} {ops[0]} ({b} {ops[1]} ({cd_val}))"
                        total_tested += 1
                        result = safe_eval(expression_with_parens)

                        if result is not None:  # Ensure result is not None before further checks

                            # Check if result == 10
                            if result is not None and math.isclose(result, 10, rel_tol=1e-9):
                                combination = f"{a_expr} {ops[0]} ({b_expr} {ops[1]} ({cd_expr}))"
                                combinations.append(combination)

                            # Check sqrt(result) == 10
                            if result >= 0:
                                sqrt_result = math.sqrt(result)
                                if math.isclose(sqrt_result, 10, rel_tol=1e-9):
                                    combination = f"sqrt({a_expr} {ops[0]} ({b_expr} {ops[1]} ({cd_expr})))"
                                    combinations.append(combination)
    return total_tested, combinations

if __name__ == "__main__":
    main()

