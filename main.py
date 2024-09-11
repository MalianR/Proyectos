# main.py
import sys  # Importamos sys para manejar argumentos de la línea de comandos
from lexico import analizar  # Importamos la función 'analizar' desde lexico.py

# Esta función guarda los tokens en un archivo de salida.
def guardar_tokens_en_archivo(tokens, archivo_salida):
    #Abrir el archivo de salida, 'w', permisos para sobreescribir el archivo
    with open(archivo_salida, 'w') as f:
        # Recorremos la lista de tokens y los guardamos en el archivo de salida.
        for token in tokens:
            #Recorrer la lista de tokens
            if len(token) == 3:
                #Sobreescribir los tokens
                f.write(f'<{token[0]},{token[1]},{token[2]}>\n')
            else:
                f.write(f'<{token[0]},{token[1]},{token[2]},{token[3]}>\n')

# Función principal que gestiona la ejecución del programa.
def principal():
    # Verificamos si la cantidad de argumentos es correcta (3 en total).
    if len(sys.argv) != 3:
        #Manejar el error, avisar que se necesita un archivo de entrada y uno de salida.
        print("Uso: python main.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)  # Terminamos la ejecución si los argumentos no son correctos.

    # Capturamos el archivo de entrada y el archivo de salida desde los argumentos.
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]

    # Llamamos a la función 'analizar' para realizar el análisis léxico del archivo de entrada.
    tokens = analizar(archivo_entrada)

    # Guardamos los tokens generados en el archivo de salida.
    guardar_tokens_en_archivo(tokens, archivo_salida)

# Ejecutamos la función principal si el archivo se ejecuta directamente.
#Entry point.
if __name__ == "__main__":
    principal()
