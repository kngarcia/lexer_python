# main.py
from lexer import Lexer

def main():
    # Leer archivo de entrada
    input_file = 'codigo_fuente.py'
    with open(input_file, 'r') as file:
        code = file.read()
    
    # Crear el analizador léxico y tokenizar el código
    lexer = Lexer(code)
    lexer.tokenize()  # No hace falta guardar el retorno ya que se manejan internamente los tokens y errores

if __name__ == "__main__":
    main()
