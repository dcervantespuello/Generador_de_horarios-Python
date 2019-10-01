import pandas as pd
from py.funciones import *

df = pd.read_csv('csv/dataframe.csv')
df = dataframe_limpio(df)

cursos = total_cursos(df)
print('Total de cursos: {}\n'.format(len(cursos)))

contar_por_semestre(df)
