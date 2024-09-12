# Lexer en Python

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
