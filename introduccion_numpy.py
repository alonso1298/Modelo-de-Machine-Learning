# Importar numpy son abreviación "np"
from funciones import *
import numpy as np

# Podemos crear arrays de una dimensión con la función np.array()
array_unidim = np.array([1,2,3,4,5])

# O un array de dos dimensiones (bidimensional)
array_bidim = np.array([[1, 2, 3], 
                       [4, 5, 6]])

# O un array de tres dimensiones (tridimensional)
array_tridim = np.array([[[1, 2, 3], 
                       [4, 5, 6]],
                       [[7, 8, 9],
                        [10, 11, 12]]])

# /** Para cada uno de estos arrays, podemos obtener sus propiedades, tales como su "forma", número de dimensiones, tipos de datos y tamaño. **/

# Atributos del array unidimensional (forma, número de dimensiones, tipos de datos, tamaño, y tipo)
print(array_unidim.shape, array_unidim.ndim, array_unidim.dtype, array_unidim.size, type(array_unidim))

# Atributos del array bidimensional
print(array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_bidim))

# Atributos del array tridimensional
print(array_tridim.shape, array_tridim.ndim, array_tridim.dtype, array_tridim.size, type(array_tridim))

# Importamos pandas como pd, y creamos un DataFrame a partir del array bidimensional
import pandas as pd
guiones()

datos = pd.DataFrame(array_bidim)
print(datos)

# Creamos un array de tamaño 4x3, formado únicamente por unos (1)
unos = np.ones((4, 3))
print(unos)

# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)
cero = np.zeros((2, 4, 3))
print(cero)
guiones()

# Creamos un array de números en el rango de 0 a 100, con un paso de 5
array_1 = np.arange(0, 100, 5)
print(array_1)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)
array_2 = np.random.randint(0, 10, (2, 5))
print(array_2)

# Creamos un array de números aleatorios decimales comprendidos en entre 0 y 1, de tamaño (3, 5)
array_3 = np.random.random((3, 5))
print(array_3)
guiones()

# Establecemos la "semilla" de números aleatorios en 27
np.random.seed(27)

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (3, 5)
array_4 = np.random.randint(0, 10, (3, 5))
print(array_4)
guiones()

# /** ¿Qué ocurre al correr la última celda nuevamente, a diferencia de las anteriores? **/

# Encontramos los valores únicos del array_4

# Extraemos el elemento de índice 1 del array_4

# Extraemos las primeras dos filas del array_4

# Extraemos los dos primeros datos de las primeras dos filas del array_4

# Creamos dos arrays de tamaño 3x4: uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos

# invocamos el array_5

# invocamos el array_6

# Sumamos los dos arrays

# Creamos ahora un array de tamaño (4,3) lleno de unos

# Intentaremos sumar los arrays 6 y 7