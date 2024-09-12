from tokens import is_reserved_word, is_operator, is_delimiter,is_caracterinventado, DELIMITERS, OPERATORS, RESERVED_WORDS, CARACTERINVENTADOS

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        self.error_reported = False
        self.error_message = ""
        self.symbol_stack = []  # Pila para manejar símbolos de apertura y cierre
        self.OPENING_SYMBOLS = {'(', '[', '{'}
        self.CLOSING_SYMBOLS = {')', ']', '}'}
        self.MATCHING_SYMBOLS = {('(', ')'), ('[', ']'), ('{', '}')}

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
                break  # Detener si ya se ha reportado un error
            char = self.peek()

            # Ignorar espacios en blanco
            if char.isspace():
                self.advance()
                continue

            # Procesar cadenas de texto y comentarios
            if char in {'"', "'", '#'}:
                self.tokenize_string_or_comment()
                continue

            # Tokenizar identificadores y palabras reservadas
            if char.isalpha() or char == '_':
                self.tokenize_identifier()

            # Tokenizar números
            elif char.isdigit():
                self.tokenize_number()

            # Tokenizar operadores
            elif is_operator(char):
                self.tokenize_operator()

            # Tokenizar delimitadores
            elif is_delimiter(char):
                self.tokenize_delimiter()

            # Si no coincide con nada, es un error léxico
            else:
                self.report_error()
                break  # Detenerse inmediatamente después de reportar el error

        # Verificar si hay símbolos de apertura sin cerrar en la pila
        if self.symbol_stack:
            opening_symbol, opening_line, opening_column = self.symbol_stack.pop()
            self.error_message = f">>> Error léxico: símbolo de apertura '{opening_symbol}' sin cierre (linea:{opening_line}, columna:{opening_column})\n"
            self.error_reported = True

        # Escribir los tokens generados en el archivo de salida
        self.write_output()
        return self.tokens

    def report_error(self):
        """Almacena un mensaje de error léxico sin escribirlo inmediatamente."""
        if not self.error_reported:
            # Almacena el mensaje de error en lugar de escribirlo inmediatamente
            self.error_message = f">>> Error léxico(linea:{self.line},columna:{self.column})\n"
            print(f"Error léxico reportado: linea:{self.line}, columna:{self.column}")  # Para depuración
            self.error_reported = True

    def write_output(self):
        """Escribe los tokens en el archivo de salida."""
        try:
            with open('output.txt', 'w') as file:
                # Primero escribe todos los tokens válidos
                for token in self.tokens:
                    if isinstance(token, tuple):
                        if len(token) == 4:  # Token con lexema
                            file.write(f"<{token[0]},{token[1]},{token[2]},{token[3]}>\n")
                        elif len(token) == 3:  # Palabra reservada
                            file.write(f"<{token[0]},{token[1]},{token[2]}>\n")
                # Luego escribe el mensaje de error si existe
                if hasattr(self, 'error_message') and self.error_message:
                    file.write(self.error_message)
        except Exception as e:
            print(f"Error al escribir en el archivo: {e}")

    def tokenize_identifier(self):
        """Tokeniza identificadores y palabras reservadas."""
        start_pos = self.position
        start_column = self.column
        if self.peek() and (self.peek().isalpha() or self.peek() == '_'):
            self.advance()
            while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
                self.advance()
            identifier = self.code[start_pos:self.position]
            if is_reserved_word(identifier):
                self.tokens.append((identifier, self.line, start_column))
            else:
                self.tokens.append(("id", identifier, self.line, start_column))
        else:
            self.report_error()

    def tokenize_number(self):
        """Tokeniza números enteros y maneja errores léxicos si un número es seguido por caracteres inválidos."""
        start_pos = self.position
        start_column = self.column
        while self.peek() and self.peek().isdigit():
            self.advance()
        number = self.code[start_pos:self.position]
        self.tokens.append(("tk_entero", number, self.line, start_column))
        
        # Después de tokenizar el número, verificar si hay caracteres no válidos
        if self.peek() and (self.peek().isalpha() or self.peek() == '_'):
            self.report_error()


    def tokenize_operator(self):
        """Tokeniza operadores de uno, dos o tres caracteres."""
        start_column = self.column
        char = self.peek()

        # Verifica si hay uno o dos caracteres después del operador actual
        next_char = self.code[self.position + 1] if self.position + 1 < len(self.code) else None
        next_next_char = self.code[self.position + 2] if self.position + 2 < len(self.code) else None

        # Combinaciones de tres caracteres para operadores triples (e.g. //=, **=, etc.)
        if next_char and next_next_char:
            combined_three = f"{char}{next_char}{next_next_char}"
            if combined_three in OPERATORS:  # Verifica si el operador de tres caracteres existe
                token_name = OPERATORS[combined_three]
                self.tokens.append((token_name, self.line, start_column))
                self.advance()  # Avanzar tres caracteres
                self.advance()
                self.advance()
                return

        # Combinaciones de dos caracteres para operadores dobles (e.g. +=, ==, etc.)
        if next_char:
            combined_two = f"{char}{next_char}"
            if combined_two in OPERATORS:  # Verifica si el operador combinado existe
                token_name = OPERATORS[combined_two]
                self.tokens.append((token_name, self.line, start_column))
                self.advance()  # Avanzar dos caracteres
                self.advance()
                return

        # Si no hay operador de dos o tres caracteres, verifica un operador de un solo carácter
        if char in OPERATORS:
            token_name = OPERATORS[char]
            self.tokens.append((token_name, self.line, start_column))
            self.advance()
        else:
            self.report_error()


    def tokenize_delimiter(self):
        """Tokeniza delimitadores y maneja el balanceo de símbolos."""
        start_column = self.column
        char = self.peek()
        token_name = DELIMITERS.get(char, None)
        if token_name:
            self.tokens.append((token_name, self.line, start_column))
            if char in self.OPENING_SYMBOLS:
                self.symbol_stack.append((char, self.line, self.column))
            elif char in self.CLOSING_SYMBOLS:
                if not self.symbol_stack:
                    self.error_message = f">>> Error léxico: símbolo de cierre '{char}' sin apertura (linea:{self.line}, columna:{self.column})\n"
                    self.error_reported = True
                else:
                    opening_symbol, opening_line, opening_column = self.symbol_stack.pop()
                    if (opening_symbol, char) not in self.MATCHING_SYMBOLS:
                        self.error_message = f">>> Error léxico: símbolo '{char}' no cierra correctamente '{opening_symbol}' (linea:{opening_line}, columna:{opening_column})\n"
                        self.error_reported = True
            self.advance()
        else:
            self.report_error()

    def tokenize_string_or_comment(self):
        """Tokeniza cadenas de texto y comentarios."""
        start_line = self.line
        start_column = self.column
        current_char = self.peek()

        # Comentarios de una línea
        if current_char == '#':
            while self.peek() != '\n' and self.peek() is not None:
                self.advance()
            self.advance()
            return

        # Cadenas y comentarios multilínea
        if current_char in {'"', "'"}:
            quote_char = current_char
            self.advance()
            if self.peek() == quote_char and self.code[self.position:self.position + 2] == quote_char * 2:
                self.advance()
                self.advance()
                while self.peek() is not None and self.code[self.position:self.position + 3] != quote_char * 3:
                    self.advance()
                if self.peek() is not None:
                    self.advance()
                    self.advance()
                    self.advance()
                return

            string_content = ""
            while self.peek() is not None:
                current_char = self.peek()
                if current_char == quote_char:
                    self.advance()
                    self.tokens.append(("tk_string", string_content, start_line, start_column))
                    return
                if current_char == '\n':
                    self.line += 1
                    self.column = 0
                else:
                    self.column += 1
                string_content += current_char
                self.advance()

            self.line = start_line
            self.column = start_column
            self.report_error()

    def tokenize_caracterinventado(self):

        start_column = self.column
        char = self.peek()

        # Tokenizar caracteres inventados
        if char in CARACTERINVENTADOS:
            token_name = CARACTERINVENTADOS[char]
            self.tokens.append((token_name, self.line, start_column))
            self.advance()
        else:
            self.report_error()