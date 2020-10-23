import random
import time

import matplotlib.pyplot as plt
import numpy

import binarySearch
import linearSearch

ALG1 = linearSearch.linearSearch
ALG2 = binarySearch.binarySearch
ALG1_NAME = "Linear search"
ALG2_NAME = "Binary search"

# Valores de n a analizar
X_ARR = [200000, 500000, 1000000]


# Función que busca el elemento deseado en la lista
# utilizando el algoritmo proporcionado
def searchAndComputeTime(searchAlg, arr, toSearch):

    # Buscar el elemento y calcular el tiempo de ejecución
    t1 = time.perf_counter()
    searchAlg(arr, toSearch)
    t2 = time.perf_counter()

    # Devolver el tiempo utilizado
    return t2 - t1


# Función que calcula el tiempo utilizado por los algoritmos definidos
# Devuelve una tupla con los tiempos correspondientes
def searchAndGetTimes(arr, toSearch):
    print("N =", len(arr))
    print("key =", toSearch)

    firstAlgTime = searchAndComputeTime(ALG1, arr, toSearch)
    print(ALG1_NAME, ":", firstAlgTime)

    sortedCopy = arr.copy()
    sortedCopy.sort()

    secondAlgTime = searchAndComputeTime(ALG2, sortedCopy, toSearch)
    print(ALG2_NAME, ":", secondAlgTime, "\n")

    return firstAlgTime, secondAlgTime


# Función que retorna una lista de tuplas
# con los tiempos promedio de búsqueda para cada n
def computeAvgTimesArr():
    # Lista con las tuplas de tiempos promedios para cada n.
    AVG_TIMES = []
    # Calcular los tiempos promedio para cada n y agregar la tupla respectiva a la lista
    for n in X_ARR:
        # Lista que contendrá 3 tuplas con los tiempos obtenidos para n
        TIMES_FOR_N = []
        # Calcular 3 veces el tiempo de los algoritmos
        for i in range(3):
            arr = [random.randint(0, n // 2) for j in range(n)]
            TIMES_FOR_N.append(searchAndGetTimes(arr, random.randint(0, n // 2)))

        # Calcular el promedio de tiempo para cada algoritmo
        firstMean = numpy.mean([t[0] for t in TIMES_FOR_N])
        print("Tiempo promedio", ALG1_NAME, "para", n, "elementos:", firstMean)
        secondMean = numpy.mean([t[1] for t in TIMES_FOR_N])
        print("Tiempo promedio", ALG2_NAME, "para", n, "elementos:", secondMean, "\n")
        # Agregar la tupla de tiempo promedio obtenida
        AVG_TIMES.append((firstMean, secondMean))
    return AVG_TIMES


# Función que se encarga de realizar el test para
# el caso correspondiente.
# Obtiene una lista de tuplas con los tiempos promedios para cada n,
# y finalmente la grafica.
def testAndPlot(title):
    print(title, "\n")
    AVG_TIMES = computeAvgTimesArr()

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Tamaño del arreglo")
    ax.set_ylabel("Tiempo de ejecución")
    ax.plot(X_ARR, [y[0] for y in AVG_TIMES])
    ax.plot(X_ARR, [y[1] for y in AVG_TIMES])
    ax.legend([ALG1_NAME, ALG2_NAME])


testAndPlot("Algoritmos de búsqueda")
plt.show()
