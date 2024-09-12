# Lexer en Python

Instrucciones de Uso:

Como funciona: 

** Metodos principales: **

__init__(self, code): Inicializa el Lexer con el código fuente a analizar.
advance(self): Avanza la posición del puntero en el código fuente.
peek(self): Retorna el siguiente carácter en el código fuente sin avanzar el puntero.
tokenize(self): Realiza el análisis léxico y retorna una lista de tokens.
report_error(self): Reporta un error léxico.
write_output(self): Muestra los tokens y el mensaje de error (si existe) en pantalla.
tokenize_identifier(self): Tokeniza identificadores y palabras reservadas.
tokenize_number(self): Tokeniza números enteros

