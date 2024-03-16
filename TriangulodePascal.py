""" 
Archivo: TriangulodePascal.py

Autores: 
         Fiorella Abarca Valverde 305190505
 
         José Pablo Morales del Valle 901110261 
         
         Roberto Montoya Leiva 304290937 
         
# Fecha: 20/11/2023

# Descripción: 
    Este programa genera el Triángulo de Pascal hasta "n" número 
    de filas específicado por el usuario. El triángulo de Pascal
    es una estructura matemática que muestra los coeficientes binomiales.
               
# LLAMADA A LIBRERIAS:

En este script, no se utilizan librerías externas.

# CONSTANTES:

    No hay constantes definidas en este script.

# FUNCIONES Y PROCEDIMIENTOS:

def generar_triangulo_pascal(num_filas):
        
    Genera el triángulo de Pascal hasta el número de filas especificado.
    
   
    
    
def guardar_en_txt(triangulo, nombre_archivo):
    
    Guarda el triángulo de Pascal en un archivo de texto.
    
    
"""

## Cuerpo principal del programa

from funciones import generar_triangulo_pascal, guardar_en_txt


# Inicia un bucle para permitir al usuario crear múltiples triángulos.
continuar = 'S'
while continuar.upper() == 'S':
    # Pide al usuario ingresar el número de filas para el triángulo.
    num_filas = int(input('Ingresa el número de filas para el triángulo de Pascal: '))

    # Genera el triángulo de Pascal con el número de filas dado.
    triangulo = generar_triangulo_pascal(num_filas)

    # Define el nombre del archivo basado en el número de filas.
    nombre_archivo = f'triangulo_de_pascal_{num_filas}.txt'

    # Guarda el triángulo en el archivo de texto.
    guardar_en_txt(triangulo, nombre_archivo)
    print(f'El archivo "{nombre_archivo}" ha sido guardado en la misma carpeta donde se ejecuta este código.')

    # Pregunta al usuario si desea generar otro triángulo.
    continuar = input('¿Deseas calcular otro triángulo de Pascal? (S/N): ')

# Imprime un mensaje de agradecimiento al finalizar.
print("¡Gracias por utilizar nuestro generador del triángulo de Pascal!")







