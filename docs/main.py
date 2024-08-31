def calculate(expression: str) -> int:
    # Eliminar espacios en blanco alrededor de la expresión
    expression = expression.replace(" ", "")
    
    # Identificar la operación en la expresión
    if '+' in expression:
        num1, num2 = expression.split('+')
        return int(num1) + int(num2)
    elif '-' in expression:
        num1, num2 = expression.split('-')
        return int(num1) - int(num2)
    elif '*' in expression:
        num1, num2 = expression.split('*')
        return int(num1) * int(num2)
    elif '/' in expression:
        num1, num2 = expression.split('/')
        return int(num1) // int(num2)  # División entera
    else:
        raise ValueError("Operación no soportada")