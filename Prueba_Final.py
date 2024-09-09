# Este es un archivo de prueba para el tokenizador

# Importar módulos
import os
import sys

# Definir una función simple
def saludo(nombre):
    print(f"Hola, {nombre}!")

# Usar la función
saludo("Mundo")

# Operaciones aritméticas
a = 10
b = 20
c = a + b * (a - b) / a

# Comparaciones
if a > b:
    print("a es mayor que b")
else:
    print("a no es mayor que b")

# Uso de listas y diccionarios
lista = [1, 2, 3, 4, 5]
diccionario = {"clave1": "valor1", "clave2": "valor2"}

# Bucle for
for i in lista:
    print(i)

# Bucle while
while a < b:
    a += 1

# Manejo de excepciones
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: División por cero")

# Comentarios y cadenas de texto
# Este es un comentario
cadena = "Esto es una cadena de texto"

# Símbolos adicionales
@decorador
def funcion_decorada():
    pass

# Operadores bit a bit
x = a & b
y = a | b
z = a ^ b
w = ~a
shift_izq = a << 2
shift_der = a >> 2

# Operadores de asignación
a += 1
b -= 1
c *= 2
d /= 2
e %= 3

# Elementos fuera de Python
# Esto es un comentario en español
# This is a comment in English
# これは日本語のコメントです
# Ceci est un commentaire en français
# Dies ist ein Kommentar auf Deutsch
