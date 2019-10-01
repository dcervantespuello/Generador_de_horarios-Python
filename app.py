import pandas as pd
from py.funciones import *

df = pd.read_csv('csv/dataframe.csv')
df = limpiar_dataframe(df)
total_cursos(df)
