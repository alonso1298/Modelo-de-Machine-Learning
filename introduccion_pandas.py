from funciones import *

# Importamos Pandas
import pandas as pd

# Creamos una serie de números y hallamos su media
numeros = pd.Series([1,2,3,5,67,35,235,62])
print(numeros.mean())
salto()

# Hallamos la suma de dichos números
print(numeros.sum())
guiones()

# Creamos una SERIE de tres colores diferentes
colores = pd.Series(['rojo', 'amarillo', 'verde'])

# Visualizamos la serie creada
print(colores)
guiones()

# Creamos una serie con tipos de autos, y la visualizamos
tipos_autos = pd.Series(['sedan', 'SUV', 'pick up'])
print(tipos_autos)
salto()

# Combinamos las series de tipos de autos y colores en un DATAFRAME
tabla_autos = pd.DataFrame({'Tipo de Auto': tipos_autos, 'Color': colores})
print(tabla_autos)
salto()
# Conectamos el cuaderno actual con nuestro Drive
# Importar "ventas-autos.csv" y convertirlo en un nuevo DATAFRAME
#Este será nuestro "Dataframe de Flujo Vehicular"
# Exportar el Dataframe como un archivo CSV a mi carpeta "/content/drive/MyDrive/Colab Notebooks/pruebas/"
# Analicemos los tipos de datos disponibles en el dataset de ventas autos
# Apliquemos estadística descriptiva (cantidad de valores, media, desviación estándar, valores mínimos y máximos, cuartiles) al dataset
# Obtenemos información del dataset utilizando info()
# Listamos los nombres de las columnas de nuestro dataset
# Averiguamos el "largo" de nuestro dataset
# Mostramos las primeras 5 filas del dataset
# Mostramos las primeras 7 filas del dataset
# Mostramos las últimas 5 filas del dataset
# Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame
# Utilizamos .iloc para seleccionar las filas 3, 7 y 9
#En la documentación podrás observar la diferencia entre el funcionamiento de .loc e .iloc.
# Seleccionar la columna "Kilometraje"
#15/10/24, 8:42 p.m. Python TOTAL - Pandas.ipynb - Colab
#https://colab.research.google.com/drive/1-E33EMCehgPnmqgwm13-SZSnVYOHMpuQ?usp=sharing#printMode=true 1/2
# Encontrar el valor medio de la columnas "Kilometraje"
# Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje
# Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas
# Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas
# Importamos Matplotlib y creamos un gráfico con los valores de la columna Kilometraje
# Puede que un gráfico más apropiado en este caso sea un histograma?
# Intentamos graficar la columna de precios
#No funcionó, verdad? Alguna idea de por qué esto puede ocurrir?
#Una pista es buscar: "cómo convertir strings de Pandas a números"
#Aqui hay un enlace a StackOverflow referido a este tema.
# Elimina la puntuación de la columna de precios
