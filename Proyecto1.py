# Definir las palabras clave de Python
keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
    'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]

# Definir los patrones de los tokens
token_patterns = [
    (' ', None),  # Ignorar espacios
    ('\t', None),  # Ignorar tabulaciones
    ('\n', 'NEWLINE'),  # Nueva línea
    ('#', 'COMMENT'),  # Comentarios
    ('.', 'FLOAT'),  # Punto decimal
    ('0', 'INTEGER'),  # Números enteros (0-9)
    ('1', 'INTEGER'),
    ('2', 'INTEGER'),
    ('3', 'INTEGER'),
    ('4', 'INTEGER'),
    ('5', 'INTEGER'),
    ('6', 'INTEGER'),
    ('7', 'INTEGER'),
    ('8', 'INTEGER'),
    ('9', 'INTEGER'),
    ('=', 'COMPARISON'),  # Operadores de comparación
    ('!', 'COMPARISON'),
    ('<', 'COMPARISON'),
    ('>', 'COMPARISON'),
    ('+', 'OPERATOR'),  # Operadores aritméticos
    ('-', 'OPERATOR'),
    ('*', 'OPERATOR'),
    ('/', 'OPERATOR'),
    ('%', 'OPERATOR'),
    ('(', 'tk_par_izq'),  # Paréntesis izquierdo
    (')', 'tk_par_der'),  # Paréntesis derecho
    ('[', 'BRACKET'),  # Corchetes
    (']', 'BRACKET'),
    ('{', 'BRACKET'),  # Llaves
    ('}', 'BRACKET'),
    ('"', 'tk_cadena'),  # Cadenas de texto (comillas dobles)
    ("'", 'tk_cadena'),  # Cadenas de texto (comillas simples)
    (':', 'tk_dos_puntos'),  # Dos puntos
    ('@', 'SYMBOL'),
    ('&', 'SYMBOL'),
    ('|', 'SYMBOL'),
    ('^', 'SYMBOL'),
    ('~', 'SYMBOL'),
    ('<', 'SYMBOL'),
    ('>', 'SYMBOL'),
    ('=', 'tk_asig'),  # Asignación
    ('+', 'SYMBOL'),
    ('-', 'SYMBOL'),
    ('*', 'SYMBOL'),
    ('/', 'SYMBOL'),
    ('%', 'SYMBOL'),
    ('_', 'SYMBOL'),
    ('?', 'SYMBOL'),
]

# Añadir patrones para letras del alfabeto, el guion bajo (_) y el signo de interrogación (?)
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in letters:
    token_patterns.append((letter, 'IDENTIFIER'))

# Lista de símbolos no manejados en Python
non_python_symbols = []

# Función para analizar los tokens
def tokenize(code):
    tokens = []  # Lista para almacenar los tokens encontrados
    line_num = 1  # Número de línea inicial
    col_num = 1  # Número de columna inicial
    pos = 0  # Posición inicial en el código
    while pos < len(code):  # Mientras no lleguemos al final del código
        match = None  # Inicializar la variable de coincidencia
        # Recorrer los patrones para buscar una coincidencia
        for pattern, tag in token_patterns:
            # Comprobamos si la cadena en la posición actual coincide con el patrón
            if code[pos:pos+len(pattern)] == pattern:
                match = pattern  # Si coincide, lo asignamos a 'match'
                break  # Rompemos el bucle si encontramos una coincidencia
        if match:
            text = match  # Asignamos la coincidencia a 'text'
            if tag:  # Si hay una etiqueta asociada
                # Si es un identificador, comprobamos si es una palabra clave
                if tag == 'IDENTIFIER' and text in keywords:
                    tag = 'KEYWORD'  # Lo marcamos como palabra clave
                # Añadimos el token a la lista de tokens
                token = (tag, text, line_num, col_num)
                tokens.append(token)
                # Si el token es desconocido, lo mostramos y lo añadimos a la lista
                if tag == 'UNKNOWN':
                    print(f'Token desconocido encontrado: {text} en la línea {line_num}')
                    if text not in non_python_symbols:
                        non_python_symbols.append(text)
            col_num += len(match)  # Avanzamos la posición de la columna
            pos += len(match)  # Avanzamos la posición
            # Si es una nueva línea, incrementamos el número de línea y reiniciamos la columna
            if text == '\n':
                line_num += 1
                col_num = 1
        else:
            # Si no hay coincidencia, manejamos el carácter desconocido
            unknown_char = code[pos]  # Capturamos el carácter desconocido
            print(f'Token desconocido encontrado: {unknown_char} en la línea {line_num}')
            tokens.append(('UNKNOWN', unknown_char, line_num, col_num))
            col_num += 1
            pos += 1  # Avanzamos la posición
    return tokens  # Devolvemos la lista de tokens

# Función principal que toma los archivos de entrada y salida
def main(input_file, output_file):
    # Leer el contenido del archivo de entrada
    with open(input_file, 'r', encoding='utf-8') as f:
        code = f.read()
    # Tokenizar el código leído
    tokens = tokenize(code)
    # Escribir los tokens en el archivo de salida en el formato específico
    with open(output_file, 'w', encoding='utf-8') as f:
        for token in tokens:
            f.write(f'<{token[0]},{token[1]},{token[2]},{token[3]}>\n')
    # Mostrar los símbolos no manejados si se encuentran
    if non_python_symbols:
        print('Símbolos no manejados en Python encontrados:')
        for symbol in non_python_symbols:
            print(symbol)

# Iniciar la ejecución del programa
if __name__ == '__main__':
    import sys
    # Comprobar si se pasaron los argumentos correctos
    if len(sys.argv) != 3:
        print('Uso: python Proyecto1.py <archivo_entrada> <archivo_salida>')
    else:
        main(sys.argv[1], sys.argv[2])
