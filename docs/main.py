import ast
import operator as op

# Supported operators
operators = {
    ast.Add: op.add, 
    ast.Sub: op.sub, 
    ast.Mult: op.mul, 
    ast.Div: op.truediv,
    ast.USub: op.neg  # Handle unary subtraction
}

def evaluate_expr(node):
    if isinstance(node, ast.Num):  # <number>
        return node.n
    elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
        return operators[type(node.op)](evaluate_expr(node.left), evaluate_expr(node.right))
    elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
        return operators[type(node.op)](evaluate_expr(node.operand))
    else:
        raise TypeError(node)

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
        # Parse the expression
        node = ast.parse(expression, mode='eval')

        # Evaluate the expression
        result = evaluate_expr(node.body)

        # Check for non-numeric result
        if not isinstance(result, (int, float)):
            raise ValueError("Expression did not result in a number")

        # Round the result to 10 decimal places to avoid floating point precision issues
        return round(result, 10)
    except ZeroDivisionError:
        # Re-raise ZeroDivisionError
        raise
    except Exception:
        # Catch all other exceptions and raise a SyntaxError
        raise SyntaxError("Invalid syntax")