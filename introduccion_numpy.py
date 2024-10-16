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
salto()

# Atributos del array bidimensional
print(array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_bidim))
salto()

# Atributos del array tridimensional
print(array_tridim.shape, array_tridim.ndim, array_tridim.dtype, array_tridim.size, type(array_tridim))

# Importamos pandas como pd, y creamos un DataFrame a partir del array bidimensional
import pandas as pd
guiones()

datos = pd.DataFrame(array_bidim)
print(datos)
salto()

# Creamos un array de tamaño 4x3, formado únicamente por unos (1)
unos = np.ones((4, 3))
print(unos)
salto()

# Creamos un array de tamaño 2x4x3, formado únicamente por ceros (0)
cero = np.zeros((2, 4, 3))
print(cero)
guiones()

# Creamos un array de números en el rango de 0 a 100, con un paso de 5
array_1 = np.arange(0, 100, 5)
print(array_1)
salto()

# Creamos un array de números aleatorios enteros comprendidos en entre 0 y 10, de tamaño (2, 5)
array_2 = np.random.randint(0, 10, (2, 5))
print(array_2)
salto()

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
print(np.unique(array_4))

# Extraemos el elemento de índice 1 del array_4
print(array_4[1])
salto()

# Extraemos las primeras dos filas del array_4
print(array_4[:2])
salto()

# Extraemos los dos primeros datos de las primeras dos filas del array_4
print(array_4[:2, :2])
guiones()

# Creamos dos arrays de tamaño 3x4: uno relleno de números aleatorios entre 0 y 10, y otro relleno de unos
array_5 = np.random.randint(0, 10, (3, 4))
array_6 = np.ones((3, 4))

# invocamos el array_5
print(array_5)
salto()

# invocamos el array_6
print(array_6)
salto()

# Sumamos los dos arrays
print(array_5 + array_6)
guiones()

# Creamos ahora un array de tamaño (4,3) lleno de unos
array_7 = np.ones((4, 3))
print(array_7)
guiones()

# Intentaremos sumar los arrays 6 y 7
# print(array_6 + array_7)

# /** ¿A qué se debe el error anterior? ¿Qué deberíamos tener en cuenta para que no suceda? **/ 

# Entonces crearemos otro array de tamaño (4,3) lleno de unos
array_8 = np.ones((4, 3))
print(array_8)
salto()

# Restamos el array_8 al array_7
print(array_8 - array_7)
guiones()

# Creamos otros dos arrays de tamaño 3x3 con números aleatorios del 1 al 5
array_9 = np.random.randint(1, 5, (3,3))
array_10 = np.random.randint(1, 5, (3,3))

# invocamos el array_9
print(array_9)
salto()

# invocamos el array_10
print(array_10)
salto()

# Multiplicamos los últimos dos arrays entre sí
print(array_9 * array_10)
salto()

# Elevamos el array_9 al cuadrado
print(array_9**2)
salto()

# Buscamos la raíz cuadrada del array_10
print(np.sqrt(array_10))
salto()

# Hallamos el promedio de los valores del array_9
print(array_9.mean())
salto()

# Hallamos el valor máximo de los valores del array_9
print(array_9.max())
salto()

# Hallamos el valor mínimo de los valores del array_9
print(array_9.min())
guiones()

# Cambiamos la forma del array_9 por una de 9x1, y lo almacenamos como array_11
array_11 = array_9.reshape((9, 1))

# invocamos el array_11
print(array_11)
salto()

# Transponemos el array_11
print(array_11.T)
guiones()

# Comparamos el array_9 y el array_10, para saber cuáles elementos del array_9 son mayores a los del array_10
array_12 = array_9 > array_10


# /** ¿Qué tipos de datos forman parte del array de resultados? **/ 

# Veamos sus nuevos tipos de datos
print(array_12.dtype)
salto()

# Alguno de los elementos del array_9 es igual su equivalente del array_10?
print(array_9 == array_10)
salto()

# Comparamos nuevamente ambos arrays, en esta ocasión con >=
print(array_9 >= array_10)
salto()

# Buscamos los elementos del array_9 que son mayores a 2
print(array_9 > 2)
salto()

# Ordenamos de menor a mayor los elementos dentro del array_9
np.sort(array_9)