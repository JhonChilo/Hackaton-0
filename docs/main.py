import ast
import operator

# Define the operators mapping
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def calculate(expression):
    if not expression.strip():  # Handle empty or whitespace-only input
        raise ValueError("Empty input is not allowed")

    try:
        # Parse the expression into an Abstract Syntax Tree (AST)
        tree = ast.parse(expression, mode='eval')

        # Define a function to recursively evaluate the AST
        def eval_node(node):
            if isinstance(node, ast.BinOp):
                left = eval_node(node.left)
                right = eval_node(node.right)
                op = OPERATORS[type(node.op)]
                return op(left, right)
            elif isinstance(node, ast.UnaryOp):  # Handle unary operators
                operand = eval_node(node.operand)
                if isinstance(node.op, ast.UAdd):  # Unary plus
                    return +operand
                elif isinstance(node.op, ast.USub):  # Unary minus
                    return -operand
                else:
                    raise TypeError(f"Unsupported UnaryOp type: {type(node.op)}")
            elif isinstance(node, ast.Num):  # Python 3.7 and below
                return node.n
            elif isinstance(node, ast.Constant):  # Python 3.8+
                return node.value
            else:
                raise TypeError(f"Unsupported AST node type: {type(node)}")

        # Evaluate the AST and return the result
        result = eval_node(tree.body)
        return result

    except (SyntaxError, TypeError, ValueError, ZeroDivisionError) as e:
        raise