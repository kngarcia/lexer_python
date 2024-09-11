# lexer.py
from tokens import is_reserved_word, is_operator, is_delimiter, OPERATORS, DELIMITERS

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []
    
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
                print(f">>> Error léxico(linea:{self.line},posicion:{self.column})")
                return
        
        return self.tokens
    
    def tokenize_identifier(self):
        """Tokeniza identificadores y palabras reservadas."""
        start_pos = self.position
        while self.peek() and (self.peek().isalnum() or self.peek() == '_'):
            self.advance()
        identifier = self.code[start_pos:self.position]
        if is_reserved_word(identifier):
            self.tokens.append((identifier, self.line, self.column))
        else:
            self.tokens.append(("id", identifier, self.line, self.column))

    def tokenize_number(self):
        """Tokeniza números enteros y flotantes."""
        start_pos = self.position
        while self.peek() and self.peek().isdigit():
            self.advance()
        number = self.code[start_pos:self.position]
        self.tokens.append(("tk_entero", number, self.line, self.column))
    
    def tokenize_operator(self):
        """Tokeniza operadores."""
        char = self.peek()
        token_name = OPERATORS[char]
        self.tokens.append((token_name, self.line, self.column))
        self.advance()
    
    def tokenize_delimiter(self):
        """Tokeniza delimitadores."""
        char = self.peek()
        token_name = DELIMITERS[char]
        self.tokens.append((token_name, self.line, self.column))
        self.advance()
