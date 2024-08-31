def calculate(expression):
    # Remove whitespace
    expression = expression.strip()

    # Check for empty input
    if not expression:
        raise ValueError("Input cannot be empty")

    # Check for invalid characters
    for char in expression:
        if not char.isdigit() and char not in "+-*/. ()":
            raise ValueError(f"Invalid character: {char}")

    try:
        # Evaluate the expression
        result = eval(expression)

        # Check for non-numeric result
        if not isinstance(result, (int, float)):
            raise ValueError("Expression did not result in a number")

        return result
    except ZeroDivisionError:
        # Re-raise ZeroDivisionError
        raise
    except Exception:
        # Catch all other exceptions and raise a SyntaxError
        raise SyntaxError("Invalid syntax")