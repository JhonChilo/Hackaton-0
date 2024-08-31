import re

def evaluate_expression(expression):
    """Evalúa una expresión matemática con operadores básicos: +, -, *, /."""
    try:
        # Validar que la expresión solo contenga números, operadores aritméticos y espacios
        if re.match(r'^[\d+\-*/.() ]+$', expression):
            # Evalúa la expresión matemática de forma segura
            return eval(expression)
        else:
            return "Expresión no válida"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Calculadora simple")
    print("Escribe una operación matemática y presiona Enter para calcular.")
    print("Escribe 'c' para borrar la entrada.")
    
    while True:
        user_input = input("Ingrese operación: ")
        
        if user_input.lower() == 'c':
            print("Entrada borrada")
        else:
            # Evaluar y mostrar el resultado
            result = evaluate_expression(user_input)
            print(f"Resultado: {result}")

if __name__ == "__main__":
    main()
