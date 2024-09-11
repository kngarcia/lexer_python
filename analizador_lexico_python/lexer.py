from tokens import is_reserved_word, is_operator, is_delimiter, OPERATORS, DELIMITERS

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        self.error_reported = False
        self.error_message = "" 
        
        # Reiniciar el archivo de salida al inicio
        open('output.txt', 'w').close()  # Vacía el archivo al iniciar
    
    def advance(self):
        """Avanza el puntero de posición y ajusta columna y línea."""
        if self.position < len(self.code):
            if self.code[self.position] == '\n':
                self.line += 1
                self.column = 0
            self.column += 1
            self.position += 1

    def peek(self):
        """Retorna el siguiente carácter sin avanzar."""
        if self.position < len(self.code):
            return self.code[self.position]
        return None

    def tokenize(self):
        """Realiza el análisis léxico del código fuente."""
        while self.position < len(self.code):
            if self.error_reported:
                break
            
            char = self.peek()
            
            if char.isspace():
                self.advance()
                continue
            
            if char.isalpha() or char == '_':
                self.tokenize_identifier()
            elif char.isdigit():
                self.tokenize_number()
            elif is_operator(char):
                self.tokenize_operator()
            elif is_delimiter(char):
                self.tokenize_delimiter()
            else:
                # Error léxico
                self.report_error()
                break  # Detenerse inmediatamente después de reportar el error
        
        self.write_output()
        return self.tokens
    
    def report_error(self):
        """Almacena un mensaje de error léxico sin escribirlo inmediatamente."""
        if not self.error_reported:
            # Almacena el mensaje de error en lugar de escribirlo inmediatamente
            self.error_message = f">>> Error léxico(linea:{self.line},posicion:{self.column})\n"
            print(f"Error léxico reportado: linea:{self.line}, posicion:{self.column}")  # Para depuración
            self.error_reported = True

    def write_output(self):
        """Escribe los tokens en el archivo de salida."""
        try:
            with open('output.txt', 'w') as file:  # Cambiado a 'w' para sobrescribir
                # Primero escribe todos los tokens válidos
                for token in self.tokens:
                    if isinstance(token, tuple):
                        if len(token) == 4:  # Token con lexema
                            file.write(f"<{token[0]},{token[1]},{token[2]},{token[3]}>\n")
                        elif len(token) == 3:  # Palabra reservada
                            file.write(f"<{token[0]},{token[1]},{token[2]}>\n")
                    else:
                        file.write(f"{token}\n")
                
                # Luego escribe el mensaje de error si existe
                if hasattr(self, 'error_message') and self.error_message:
                    file.write(self.error_message)
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")


    
    def tokenize_identifier(self):
        """Tokeniza identificadores y palabras reservadas, manejando errores léxicos."""
        start_pos = self.position
        # Verificar si el primer carácter es válido para un identificador
        if self.peek() and (self.peek().isalpha() or self.peek() == '_'):
            self.advance()  # Avanzar para procesar el siguiente carácter
            # Continuar mientras se encuentren caracteres válidos
            while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
                self.advance()

            identifier = self.code[start_pos:self.position]
            
            # Comprobar si es una palabra reservada
            if is_reserved_word(identifier):
                self.tokens.append((identifier, self.line, self.column))
            else:
                self.tokens.append(("id", identifier, self.line, self.column))
        else:
            # Si el primer carácter no es válido para un identificador, reportar error léxico
            self.report_error()
    
    def tokenize_number(self):
        """Tokeniza números enteros y maneja errores léxicos si un número es seguido por caracteres inválidos."""
        start_pos = self.position
        while self.peek() and self.peek().isdigit():
            self.advance()
        
        # Después de procesar un número, verifica el siguiente carácter
        if self.peek() and (self.peek().isalpha() or self.peek() == '_'):
            # Si hay un alfabético o guion bajo después de un número, es un error léxico
            self.report_error()
            return
        
        number = self.code[start_pos:self.position]
        self.tokens.append(("tk_entero", number, self.line, self.column))
    
    def tokenize_operator(self):
        """Tokeniza operadores."""
        char = self.peek()
        token_name = OPERATORS.get(char, None)
        if token_name:
            self.tokens.append((token_name, self.line, self.column))
            self.advance()
        else:
            self.report_error()
    
    def tokenize_delimiter(self):
        """Tokeniza delimitadores."""
        char = self.peek()
        token_name = DELIMITERS.get(char, None)
        if token_name:
            self.tokens.append((token_name, self.line, self.column))
            self.advance()
        else:
            self.report_error()
