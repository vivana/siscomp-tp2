# siscomp-tp2
archivos de resolución para TP#2 de la asignatura sistemas de computación año 2023

# Calculadora de cotización de criptomonedas
Este programa recupera la cotización de al menos dos criptomonedas haciendo uso de API Rest y Python. Los datos de consulta realizados son entregados a un programa en C que convoca rutinas en ensamblador para que haga los cálculos de conversión y devuelva las cotizaciones en pesos, u$s y euros. Finalmente el programa muestra los cálculos obtenidos.-

## Makefile
Se provee un archivo make para realizar la compilación y generar los archivos binarios necesarios para la ejecución del programa cotiza.py
+ `$ make make` : ejecuta el código en python que hace uso de la librería compartida para ejecutar el código en c que a su vez invoca el código en assembler.
+ `$ make debug` : ejecuta el código en c inicializando la consola GDB.

Para asegurarnos de eliminar todos los binarios podemos ejecutar:
+ `$ make clean` : realiza el borrado de los archivos binarios
+ `$ make clean_debug` : realiza el borrado de los archivos binarios y el archivo de depuración para gdb.

