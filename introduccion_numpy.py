# Importar numpy son abreviación "np"
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

# Para cada uno de estos arrays, podemos obtener sus propiedades, tales como su "forma", número de dimensiones, tipos de datos y tamaño.

# Atributos del array unidimensional (forma, número de dimensiones, tipos de datos, tamaño, y tipo)
array_unidim.shape, array_unidim.ndim, array_unidim.dtype, array_unidim.size, type(array_unidim)

# Atributos del array bidimensional

# Atributos del array tridimensional

# Importamos pandas como pd, y creamos un DataFrame a partir del array bidimensional