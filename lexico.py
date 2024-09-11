# lexico.py
# Conjunto de palabras reservadas de Python.
palabras_reservadas = {
    'False', 'await', 'else', 'import', 'pass',
    'None', 'break', 'except', 'in', 'raise',
    'True', 'class', 'finally', 'is', 'return',
    'and', 'continue', 'for', 'lambda', 'try',
    'as', 'def', 'from', 'nonlocal', 'while',
    'assert', 'del', 'global', 'not', 'with',
    'async', 'elif', 'if', 'or', 'yield', 'range'
}

# Palabras clave suaves (soft keywords) en Python.
palabras_suaves = {'match', 'case', 'type', '_'}

# Operadores reconocidos en Python.
operadores = {
    '+', '-', '', '*', '/', '//', '%', '@',
    '<<', '>>', '&', '|', '^', '~', ':=',
    '<', '>', '<=', '>=', '==', '!=', '!'
}

# Delimitadores utilizados en Python.
delimitadores = {
    '(', ')', '[', ']', '{', '}', ',', ':', '.', ';', '@', '=',
    '->', '+=', '-=', '*=', '/=', '//=', '%=', '@=', '&=', '|=', '^=',
    '>>=', '<<=', '**='
}

# Funciones auxiliares para identificar caracteres.
def es_digito(caracter):
    return '0' <= caracter <= '9' #Identificar números enternos

def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z' #Identifica letras de caracteres (string)

def es_espacio_blanco(caracter):
    return caracter in ' \t' #Identifica espacios en blanco

def es_operador(caracter):
    return caracter in operadores #Identifica operadores aritméticos

def es_delimitador(caracter):
    return caracter in delimitadores #Identifica delimitadores.

# Función que valida si una cadena es un identificador válido.
def es_identificador_valido(cadena):
    #Busca la primera de posición de la cadena si es un _ o una letra, porque todas las variable deben empezar por letra
    return cadena[0] == '_' or es_letra(cadena[0])

# Función que realiza el análisis léxico de un archivo.
def analizar(archivo_entrada):
    # 'r' realiza la lectura ('r' -> permiso de lectura)
    with open(archivo_entrada, 'r') as archivo:
        #Guardar lo que se leyó en el archivo
        contenido = archivo.read()

    tokens = []  # Lista donde se almacenarán los tokens identificados.
    i = 0
    numero_linea = 1  # Número de línea actual.
    numero_columna = 1  # Número de columna actual.

    # Bucle while para recorrer el contenido del archivo y procesar los caracteres.
    while i < len(contenido):
        #Cada caracter será una posición en el contenido del archivo
        caracter = contenido[i]

        # Ignoramos espacios en blanco.
        if es_espacio_blanco(caracter):
            numero_columna += 1
            i += 1
            continue  # Saltamos a la siguiente iteración del bucle

        # Manejamos saltos de línea.
        if caracter == '\n':
            #Se añade una línea
            numero_linea += 1
            #Se ubica en la primera columna del archivo
            numero_columna = 1
            #Se itera en todo el archivo
            i += 1
            continue  # Saltamos a la siguiente iteración del bucle

        # Ignoramos los comentarios (líneas que comienzan con #).
        if caracter == '#':
            #Se mueve el iterador para encontrar el siguiente caracter
            while i < len(contenido) and contenido[i] != '\n':
                i += 1
            continue  # Saltamos a la siguiente iteración del bucle

        # Identificamos palabras reservadas e identificadores.
        if es_letra(caracter) or caracter == '_':
            inicio = i
            #Identificar una sintaxis válida
            while i < len(contenido) and (es_letra(contenido[i]) or es_digito(contenido[i]) or contenido[i] == '_'):
                i += 1
            lexema = contenido[inicio:i]
            #Sino se encuentra un identificador válido
            if not es_identificador_valido(lexema):
                #Manejo del error léxico
                print(f'>>> Error léxico (línea {numero_linea}, posición {numero_columna}): identificador no válido "{lexema}".')
                #Guardar el token del error
                tokens.append(('tk_error', f'identificador no válido: {lexema}', numero_linea, numero_columna))
            #Guardar los lexemas en la lista de tokens, además de su posición en el archivo
            elif lexema in palabras_reservadas:
                tokens.append((lexema, numero_linea, numero_columna))
            elif lexema in palabras_suaves:
                tokens.append(('tk_palabra_suave', lexema, numero_linea, numero_columna))
            else:
                #Identificar un id valido
                tokens.append(('id', lexema, numero_linea, numero_columna))
            numero_columna += (i - inicio)
            continue  # Saltamos a la siguiente iteración del bucle

        # Procesamos números (enteros y flotantes).
        if es_digito(caracter):
            #Se crea un iterado, i
            inicio = i
            #Inicializar el booleano para identificar flotantes
            es_flotante = False
            #Iterar los digitos
            while i < len(contenido) and es_digito(contenido[i]):
                i += 1
            #Guardar los tiplo flotante
            if i < len(contenido) and contenido[i] == '.':
                #Si esta el . en el contenido del archivo, lo establecemos como flotante
                es_flotante = True
                #Seguimos recorriendo el archivo
                i += 1
                #Mientras el tamaño del contenido sea menor a i, y sea considerado digito se sigue iterando
                while i < len(contenido) and es_digito(contenido[i]):
                    i += 1
            #Consideramos como lexema el incio de cada token
            lexema = contenido[inicio:i]
            #Guardar el tipo de token
            tipo_token = 'tk_flotante' if es_flotante else 'tk_entero'
            #Añadirlo a la lista de tokens
            tokens.append((tipo_token, lexema, numero_linea, numero_columna))
            #Pasar a la siguiente columnna
            numero_columna += (i - inicio)
            continue  # Saltamos a la siguiente iteración del bucle

        # Procesamos operadores.
        if caracter in operadores:
            inicio = i
            i += 1
            #Mientras exista el contenido en el archivo, se identifican los operadores
            while i < len(contenido) and contenido[inicio:i] in operadores:
                i += 1
            #Recorrer el contenido hasta el último elemento
            lexema = contenido[inicio:i-1]
            #Añadir el identificador seleccionado
            tokens.append((f'tk_operador_{lexema}', numero_linea, numero_columna))
            #Moverse una columna a la izquierda
            numero_columna += (i - inicio)
            continue  # Saltamos a la siguiente iteración del bucle

        # Procesamos delimitadores.
        if caracter in delimitadores:
            #Identificar el delimitador
            tokens.append((f'tk_delimitador_{caracter}', numero_linea, numero_columna))
            #Moverse una columna a la derecha
            numero_columna += 1
            #Seguir iterando
            i += 1
            continue  # Saltamos a la siguiente iteración del bucle
        else:
            # Si encontramos un carácter no reconocido, reportamos un error léxico.
            tokens.append(('tk_error', f'carácter no reconocido: {caracter}', numero_linea, numero_columna))
            #Moverse una columna a la derecha
            i += 1
            numero_columna += 1
            continue  # Saltamos a la siguiente iteración del bucle

    return tokens  # Devolvemos la lista de tokens identificados.
