# Importar la librería math
import math

# Definir las palabras clave de Python
keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
    'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]

# Definir los patrones de los tokens
token_patterns = [
    (' ', None),  # Espacios
    ('\t', None),  # Tabulaciones
    ('\n', 'NEWLINE'),  # Nueva línea
    ('#', 'COMMENT'),  # Comentarios
    ('.', 'FLOAT'),  # Punto decimal
    ('0', 'INTEGER'),  # Números enteros
    ('1', 'INTEGER'),  # Números enteros
    ('2', 'INTEGER'),  # Números enteros
    ('3', 'INTEGER'),  # Números enteros
    ('4', 'INTEGER'),  # Números enteros
    ('5', 'INTEGER'),  # Números enteros
    ('6', 'INTEGER'),  # Números enteros
    ('7', 'INTEGER'),  # Números enteros
    ('8', 'INTEGER'),  # Números enteros
    ('9', 'INTEGER'),  # Números enteros
    ('=', 'COMPARISON'),  # Operadores de comparación
    ('!', 'COMPARISON'),  # Operadores de comparación
    ('<', 'COMPARISON'),  # Operadores de comparación
    ('>', 'COMPARISON'),  # Operadores de comparación
    ('+', 'OPERATOR'),  # Operadores aritméticos
    ('-', 'OPERATOR'),  # Operadores aritméticos
    ('*', 'OPERATOR'),  # Operadores aritméticos
    ('/', 'OPERATOR'),  # Operadores aritméticos
    ('%', 'OPERATOR'),  # Operadores aritméticos
    ('(', 'BRACKET'),  # Paréntesis
    (')', 'BRACKET'),  # Paréntesis
    ('[', 'BRACKET'),  # Corchetes
    (']', 'BRACKET'),  # Corchetes
    ('{', 'BRACKET'),  # Llaves
    ('}', 'BRACKET'),  # Llaves
    ('"', 'STRING'),  # Cadenas de texto
    ("'", 'STRING'),  # Cadenas de texto
    (':', 'SYMBOL'),  # Símbolos adicionales
    ('@', 'SYMBOL'),  # Símbolos adicionales
    ('&', 'SYMBOL'),  # Símbolos adicionales
    ('|', 'SYMBOL'),  # Símbolos adicionales
    ('^', 'SYMBOL'),  # Símbolos adicionales
    ('~', 'SYMBOL'),  # Símbolos adicionales
    ('<', 'SYMBOL'),  # Símbolos adicionales
    ('>', 'SYMBOL'),  # Símbolos adicionales
    ('=', 'SYMBOL'),  # Símbolos adicionales
    ('+', 'SYMBOL'),  # Símbolos adicionales
    ('-', 'SYMBOL'),  # Símbolos adicionales
    ('*', 'SYMBOL'),  # Símbolos adicionales
    ('/', 'SYMBOL'),  # Símbolos adicionales
    ('%', 'SYMBOL'),  # Símbolos adicionales
    ('<<', 'SYMBOL'),  # Símbolos adicionales
    ('>>', 'SYMBOL'),  # Símbolos adicionales
    ('**', 'SYMBOL'),  # Símbolos adicionales
    ('//', 'SYMBOL'),  # Símbolos adicionales
    ('_', 'UNDERSCORE'),  # Identificación de subrayado
    ('?', 'QUESTION')    # Identificación de signo de interrogación
]

# Lista de símbolos no manejados en Python
non_python_symbols = []

def tokenize(code):
    tokens = []
    line_num = 1  # Número de línea inicial
    pos = 0  # Posición inicial en el código
    while pos < len(code):
        match = None
        for pattern, tag in token_patterns:
            # Verificar si el patrón coincide con el código en la posición actual
            if code[pos:pos+len(pattern)] == pattern:
                match = pattern
                break
        if match:
            text = match
            if tag:
                # Identificación de palabras clave
                if tag == 'IDENTIFIER' and text in keywords:
                    tag = 'KEYWORD'
                token = (tag, text, line_num)
                tokens.append(token)
                if tag == 'UNKNOWN':
                    print(f'Token desconocido encontrado: {text} en la línea {line_num}')
                    if text not in non_python_symbols:
                        non_python_symbols.append(text)
            pos += len(match)
            if text == '\n':
                line_num += 1
        else:
            # Manejar caracteres desconocidos
            unknown_char = code[pos]
            print(f'Token desconocido encontrado: {unknown_char} en la línea {line_num}')
            tokens.append(('UNKNOWN', unknown_char, line_num))
            pos += 1
    return tokens

def main(input_file, output_file):
    # Leer el contenido del archivo de entrada
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()
    # Tokenizar el código
    tokens = tokenize(code)
    # Escribir los tokens en el archivo de salida
    with open(output_file, 'w', encoding='utf-8') as f:
        for token in tokens:
            f.write(f'Token: {token[0]}, Lexema: {token[1]}, Línea: {token[2]}\n')
    # Mostrar símbolos no manejados en Python
    if non_python_symbols:
        print('Símbolos no manejados en Python encontrados:')
        for symbol in non_python_symbols:
            print(symbol)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print('Uso: python Proyecto1.py <archivo_entrada> <archivo_salida>')
    else:
        main(sys.argv[1], sys.argv[2])
