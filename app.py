# Se importa Pandas y Numpy
import pandas as pd
from py.cursos import arreglo_cursos

# Se lee el dataframe
df = pd.read_csv('csv/dataframe.csv')

# Se quitan las filas con valor 'NULO' en columna 'Codigo_docente'
df = df[df.Codigo_docente != 'NULO']

# Quitar filas con valor 0 en columnas 'Capacidad', 'Disponibles' y 'Ocupados'
df = df[df[['Capacidad', 'Disponibles', 'Ocupados']].any(axis='columns')]

# Cambiar valores de columna 'Disponibles' a 0
df.Disponibles[df.Capacidad == 0] = 0

# Copiar valores de columna 'Ocupados' en columna 'Capacidad'
df.Capacidad[df.Capacidad == 0] = df.Ocupados

# Conteo de cuantos cursos hay en total
cursos = set(df.Nombre_asignatura)
print('Hay {} cursos en el segundo semestre del 2019\n'.format(len(cursos)))

# Organizar los indices del dataframe
df = df.set_index(['Nombre_asignatura'])
df = df.sort_index()

print('SECCIONES POR CURSO:\n')
semestre = 1

# cursos = set(df.index.get_level_values(0))
# Numero de secciones por curso
for grupo in arreglo_cursos:
    print('Semestre {}:'.format(semestre))
    for curso in grupo:
        print('{}: {}'.format(curso, len(df.loc[curso, 'Nrc'])))
    print("")
    semestre += 1
