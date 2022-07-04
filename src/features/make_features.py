"""
Módulo de preparación de datos para pronóstico.
-------------------------------------------------------------------------------
Desde la ruta data_lake/business/ se crea una copia del archivo precios-diarios.csv en la ruta data_lake/business/features/ con el nombre precios_diarios.csv incluyendo la fecha y el precio que se desea pronosticar (variable dependiente).
"""


def make_features():
    """Prepara datos para pronóstico.
    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).
    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.
    """
    import shutil

    shutil.copy(
        "data_lake/business/precios-diarios.csv",
        "data_lake/business/features/precios_diarios.csv",
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    try:

        import doctest

        doctest.testmod()

        make_features()

    except:
        raise NotImplementedError("Implementar función para preparar datos de Pronóstico")
