import re

def calculate(expression):
    """Evalúa una expresión matemática con operadores básicos: +, -, *, /."""
    try:
        # Validar que la expresión solo contenga números, operadores aritméticos y espacios
        if not expression.strip():
            raise ValueError("La expresión está vacía")
        if re.match(r'^[\d+\-*/.() ]+$', expression):
            # Evalúa la expresión matemática de forma segura
            return eval(expression)
        else:
            raise ValueError("Expresión no válida")
    except SyntaxError:
        raise SyntaxError("Error de sintaxis en la expresión")
    except ZeroDivisionError:
        raise ZeroDivisionError("División por cero no permitida")
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")
