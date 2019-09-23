# Se importa Pandas y Numpy
import pandas as pd

# Se lee el dataframe
df = pd.read_csv('./conteo-de-cursos/dataframe.csv')

#Se quitan las filas con valor 'NULO' en columna 'Codigo_docente'
df = df[df.Codigo_docente != 'NULO']

# Quitar filas con valor 0 en columnas 'Capacidad', 'Disponibles' y 'Ocupados'
df = df[df[['Capacidad', 'Disponibles', 'Ocupados']].any(axis='columns')]

# Cambiar valores de columna 'Disponibles' a 0
df.Disponibles[df.Capacidad == 0] = 0
"""df[(df.Capacidad == 0) & (df.Disponibles < 0)] ????????????"""

# Copiar valores de columna 'Ocupados' en columna 'Capacidad'
df.Capacidad[df.Capacidad == 0] = df.Ocupados

# Conteo de cuantos cursos hay en total
cursos = set(df.Nombre_asignatura)
print('Hay {} cursos en el segundo semestre del 2019'.format(len(cursos)))