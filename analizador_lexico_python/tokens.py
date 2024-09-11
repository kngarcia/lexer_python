# Palabras reservadas
RESERVED_WORDS = {
    "False", "None", "True", "and", "as", "assert", "async", "await", "break", 
    "class", "continue", "def", "del", "elif", "else", "except", "finally", 
    "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", 
    "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"
}

# Operadores y delimitadores
OPERATORS = {
    "+": "tk_suma", "-": "tk_resta", "*": "tk_multiplicacion", "/": "tk_division",
    "%": "tk_modulo", "=": "tk_asig", "==": "tk_igual", "!=": "tk_distinto",
    "<": "tk_menor", ">": "tk_mayor", "<=": "tk_menor_igual", ">=": "tk_mayor_igual", "!": "dis"
}

DELIMITERS = {
    "(": "tk_par_izq", ")": "tk_par_der", "[": "tk_corchete_izq", "]": "tk_corchete_der",
    "{": "tk_llave_izq", "}": "tk_llave_der", ",": "tk_coma", ":": "tk_dos_puntos",
    ".": "tk_punto", ";": "tk_punto_coma"
}

# Funciones para categorizar tokens
def is_reserved_word(word):
    return word in RESERVED_WORDS

def is_operator(char):
    return char in OPERATORS

def is_delimiter(char):
    return char in DELIMITERS
