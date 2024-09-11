# Proyecto Primer Corte -  Analizador Léxico Lenguaje Python
**Realizado por:**
- Andres Sebastian Urrego Amaya
- Sebastián Cortés Briceño
- Julian Esteban Rincón Rodríguez
- Mariana Ruge Vargas

## Descripción
Python es un lenguaje de programación de propósito general, el objetivo de este proyecto es tomar un código fuente en Python y realizar un análisis léxico de dicho código.
El programa procesa archivos de texto y códigos fuente, identificando **tokens** como palabras reservadas, operadores, delimitadores, identificadores y números. También se identifican y reportan errores léxicos.

## Uso
### Requisitos
- **python 3.x:** Por defecto viene instalado en la mayoría de distribuciones de Linux, puedes verificar su instalación y versión con el comando:

	`python --version`

- **Sistema operativo compatible con la ejecución**, este programa fue probado en Ubuntu. Con la siguiente versión de la terminal.

	`GNOME Terminal 3.44.0`

### Clonar el repositorio
A continuación se presentan las instrucciones para clonar el repositorio de forma local.

1. Ejecuta en tu terminal el siguiente comando.

	`git clone https://github.com/MalianR/Proyectos`

2. Verifica los archivos del repositorio. Al clonar se te debió crear en la ruta especificada una carpeta llamada Proyectos. Para acceder a ella úbicate en:

	`cd Proyectos`

	Luego, ejecuta:
	
	`ls`

	Deberias ver los archivos que contiene este repositorio donde:

	**main.py**:  Es el archivo principal desde donde se hace la ejecución el análisis léxico de los archivos de entrada.

	**lexico.py**: Módulo que contiene las funciones para realizar el análisis léxico.

	**prueba.py**: Es una prueba para verificar que Python esté reconociendo las palabras 
    reservadas y tokens establecidos. Es un archivo con código para ser procesado por el analizador léxico.

	**salida.txt**: Este archivo,**no lo verás inicialmente,** se produce al ejecutar el programa, se guarda el resultado del análisis léxico.

### Ejecutar el programa
1. Una vez estas ubicado en la carpeta del programa, ejecuta este comando en tu terminal.

	`python3 main.py  prueba.py salida.txt`
	
	Debes especificar el archivo a ejecutar (main.py), la entrada de prueba para el análisis (prueba.py) y el nombre de  archivo de salida (salida.txt).

2. Esto genera un archivo de salida llamado "salida.txt", donde se hace todo el análisis, de todos los tokens y caracteres puestos en el archivo de entrada (prueba.py)

3. Puedes revisar el archivo con:
	`cat salida.txt`

