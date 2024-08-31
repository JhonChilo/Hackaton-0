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
        # Redefinir el entorno seguro para eval, limitando el acceso a builtins
        allowed_locals = {"math": math}
        result = eval(expression, {"__builtins__": None}, allowed_locals)
        
        # Redondear resultados con decimales para evitar problemas de precisión
        if isinstance(result, float):
            result = round(result, 10)
        
        return result
    
    except ZeroDivisionError:
        raise ValueError("División por cero")
    except SyntaxError:
        raise ValueError("Error en la expresión")
    except Exception as e:
        raise ValueError(f"Error en la expresión: {str(e)}")
