import pandas as pd


def dataframe_limpio():
    # Recibimos el archivo csv
    df = pd.read_csv('csv/dataframe.csv')

    # Se quitan las filas con valor 'NULO' en columna 'Codigo_docente'
    df = df[df.Codigo_docente != 'NULO']

    # Quitar filas con valor 0 en 'Capacidad', 'Disponibles' y 'Ocupados'
    df = df[df[['Capacidad', 'Disponibles', 'Ocupados']].any(axis='columns')]

    # Cambiar valores de columna 'Disponibles' a 0
    df.Disponibles[df.Capacidad == 0] = 0

    # Copiar valores de columna 'Ocupados' en columna 'Capacidad'
    df.Capacidad[df.Capacidad == 0] = df.Ocupados

    return(df)


def indexar_columnas(df):
    df2 = df[['Nrc',
              'Nombre_asignatura',
              'Capacidad',
              'Disponibles',
              'Ocupados']]
    print(df2)


def mostrarAgregadas(agregadas):
    if(len(agregadas) > 0):
        print("\nMaterias agregadas:")
        for i in range(len(agregadas)):
            # Imprime solo el nombre y no la coordenada
            print("  - {}".format(agregadas[i][0]))
        print()
