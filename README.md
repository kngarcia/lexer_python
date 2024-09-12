# Lexer en Python

## Estructura del proyecto:

lexer.py Contiene la clase Lexer, que es la encargada de realizar el análisis léxico del código fuente.

tokens.py Archivo auxiliar que define las funciones y constantes necesarias para reconocer palabras reservadas, operadores y delimitadores.

main.py El archivo principal que inicializa el lexer, lee el archivo de entrada y ejecuta el proceso de tokenización.

## Métodos principales en Lexer:

__init__(self, code): Constructor que inicializa las variables del lexer como el código fuente, posición actual, línea, columna, lista de tokens y manejo de errores. Además, vacía el archivo de salida antes de empezar el análisis.\n

advance(self): Avanza el puntero de lectura sobre el código fuente, actualizando la columna y línea cuando sea necesario.\n

peek(self): Retorna el siguiente carácter sin avanzar el puntero, permitiendo inspeccionar el carácter antes de procesarlo.\n

tokenize(self): Realiza el análisis léxico del código, procesando secuencialmente los caracteres y generando tokens. Detecta y almacena identificadores, palabras reservadas, operadores, delimitadores, números, cadenas de texto y comentarios.\n

report_error(self): Almacena un mensaje de error léxico cuando se detecta una secuencia no válida en el código, deteniendo el análisis si es necesario.\n

write_output(self): Escribe en el archivo de salida los tokens generados y los errores léxicos, mostrando el contenido en consola.\n

tokenize_identifier(self): Tokeniza los identificadores y palabras reservadas. Un identificador válido debe empezar con una letra o un guion bajo (_) y puede contener caracteres alfanuméricos adicionales. \n

tokenize_number(self): Tokeniza números enteros y maneja posibles errores léxicos si el número es seguido por caracteres inválidos. \n

tokenize_operator(self): Tokeniza operadores de uno, dos o tres caracteres, verificando combinaciones como +=, ==, **=, entre otros. \n

tokenize_delimiter(self): Tokeniza delimitadores y maneja el balanceo de símbolos de apertura y cierre como (), {}, [], reportando errores si hay un desequilibrio en los símbolos. \n

tokenize_string_or_comment(self): Tokeniza cadenas de texto y comentarios. Soporta comentarios de una línea (#) y cadenas delimitadas por comillas simples o dobles, así como comentarios multilínea. \n


## Descripción

El `Lexer` es una clase diseñada para realizar el análisis léxico de código fuente. Convierte una cadena de código fuente en una secuencia de tokens, facilitando el proceso de análisis sintáctico posterior. El lexer maneja identificadores, números, operadores, delimitadores, cadenas de texto y comentarios, y reporta errores léxicos.



## Características

- **Identificación de Tokens**: Reconoce identificadores, palabras reservadas, números, operadores y delimitadores.
- **Manejo de Errores**: Reporta errores léxicos, incluyendo símbolos desbalanceados y caracteres inesperados.
- **Comentarios y Cadenas**: Soporta comentarios de una línea y comentarios multilínea en forma de cadenas.
- **Balanceo de Símbolos**: Verifica que todos los símbolos de apertura tengan su correspondiente símbolo de cierre.

## Instalación

No es necesario realizar una instalación específica. Simplemente asegúrate de que el archivo `tokens.py` esté en el mismo directorio que el archivo que contiene la clase `Lexer`.

## Uso

### Importación

Para usar la clase `Lexer`, primero debes importarla y los componentes necesarios desde `tokens.py`:

```python
from tokens import is_reserved_word, is_operator, is_delimiter, DELIMITERS, OPERATORS, RESERVED_WORDS
from lexer import Lexer  # Ajusta el import según la ubicación de tu archivo


