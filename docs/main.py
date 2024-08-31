import re

def evaluate_expression(expression):
    """Evalúa la expresión matemática dada, permitiendo solo multiplicación y división."""
    try:
        # Validar que la expresión solo contenga números, operadores * y / y espacios
        if re.match(r'^[0-9*/ ]+$', expression):
#
def evaluate_expression(expression):
    """Evalúa la expresión matemática dada, permitiendo solo suma y resta."""
    try:
        if re.match(r'^[0-9+\- ]+$', expression):
            return eval(expression)
        else:
            return "Expresión no válida"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Calculadora simple")
    print("Escribe una operación (multiplicación/división) y presiona Enter para calcular.")
    print("Escribe una operación (suma/resta) y presiona Enter para calcular.")
    print("Presiona 'c' para borrar la entrada.")
    
    while True:
        user_input = input("Ingrese operación: ")
        
        if user_input.lower() == 'c':
            # Borra la entrada
            print("Entrada borrada")
        else:
            # Evaluar y mostrar el resultado
            result = evaluate_expression(user_input)
            print(f"Resultado: {result}")

if __name__ == "__main__":
    main()

