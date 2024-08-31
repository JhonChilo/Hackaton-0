import re
import math

def calculate(expression):
    """Evalúa una expresión matemática con operadores básicos: +, -, *, /."""
    try:
        # Validar que la expresión solo contenga números, operadores aritméticos y espacios
        if not re.match(r'^[\d+\-*/.() ]+$', expression):
            raise ValueError("Expresión no válida")
        
        # Verificar si la expresión está vacía o tiene solo espacios en blanco
        if expression.strip() == "":
            raise ValueError("Expresión vacía o solo contiene espacios en blanco")

        # Utilizar una precisión adecuada para manejar decimales
        result = eval(expression, {"__builtins__": None, "math": math})
        
        # Redondear resultados con decimales para evitar problemas de precisión
        if isinstance(result, float):
            result = round(result, 10)
            
        return result
    except ZeroDivisionError:
        raise
    except SyntaxError:
        raise
    except Exception as e:
        raise ValueError(f"Error en la expresión: {str(e)}")