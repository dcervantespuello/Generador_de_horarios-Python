from py.cursos import arreglo_cursos


def dataframe_limpio(df):
    # Se quitan las filas con valor 'NULO' en columna 'Codigo_docente'
    df = df[df.Codigo_docente != 'NULO']

    # Quitar filas con valor 0 en 'Capacidad', 'Disponibles' y 'Ocupados'
    df = df[df[['Capacidad', 'Disponibles', 'Ocupados']].any(axis='columns')]

    # Cambiar valores de columna 'Disponibles' a 0
    df.Disponibles[df.Capacidad == 0] = 0

    # Copiar valores de columna 'Ocupados' en columna 'Capacidad'
    df.Capacidad[df.Capacidad == 0] = df.Ocupados

    # Organizar los indices del dataframe
    df = df.set_index(['Nombre_asignatura'])
    df = df.sort_index()

    return(df)


def total_cursos(df):
    cursos = set(df.index.get_level_values(0))
    return(cursos)


def contar_por_semestre(df):
    numero_semestre = 1
    suma_cursos = 0
    for semestre in arreglo_cursos:
        print('Semestre {}: {} cursos'.format(numero_semestre, len(semestre)))
        for curso in semestre:
            secciones = len(set(df.loc[curso, 'Nrc']))
            print('{}: {}'.format(curso, secciones))
        print("")
        numero_semestre += 1
