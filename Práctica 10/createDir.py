import os


def createDir():
    # Crear directorio si no existe
    try:
        os.mkdir("PracticaResumen")
    except FileExistsError:
        print("El directorio PracticaResumen ya existe.")
