# main.py
from lexer import Lexer

def main():
    # Leer archivo de entrada
    input_file = 'codigo_fuente.py'
    with open(input_file, 'r') as file:
        code = file.read()
    
    # Crear el analizador léxico y tokenizar el código
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    # Guardar los tokens en el archivo de salida
    with open('output.txt', 'w') as output_file:
        for token in tokens:
            output_file.write(f"{token}\n")

if __name__ == "__main__":
    main()
