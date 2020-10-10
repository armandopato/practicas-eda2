import random
import sys
import time
import matplotlib.pyplot as plt
import numpy

import quickSort
import insertionSort

ALG1 = quickSort.quickSort
ALG2 = insertionSort.insertionSort
ALG1_NAME = "QuickSort"
ALG2_NAME = "InsertionSort"

sys.setrecursionlimit(6000)

# Valores mínimo y máximo de los elementos en el arreglo a ordenar
MIN_VALUE = -100000
MAX_VALUE = 100000

# Valores de n a analizar
X_ARR = [500, 1000, 2000, 5000]


# Función que ordena una lista con el algoritmo
# proporcionado y calcula el tiempo utilizado por éste
def sortAndComputeTime(sortingAlg, arr):
    # Mantener una copia ordenada
    sortedArr = arr.copy()
    sortedArr.sort()

    # Realizar una copia para evitar mutaciones en el arreglo original
    copy = arr.copy()

    # Ordenar la lista y calcular su tiempo de ejecución
    t1 = time.time()
    sortingAlg(copy)
    t2 = time.time()

    # Comprobar que el algoritmo ordenó correctamente la lista
    assert copy == sortedArr

    # Devolver el tiempo utilizado
    return t2 - t1


# Función que calcula el tiempo utilizado por quickSort
# e insertionSort para ordenar la misma lista.
# Devuelve una tupla con los tiempos correspondientes:
# (tiempoQuickSort, tiempoInsertionSort)
def sortAndGetTimes(arr):
    print("N =", len(arr))

    firstAlgTime = sortAndComputeTime(ALG1, arr)
    print(ALG1_NAME, ":", firstAlgTime)

    secondAlgTime = sortAndComputeTime(ALG2, arr)
    print(ALG2_NAME, ":", secondAlgTime, "\n")

    return firstAlgTime, secondAlgTime


# Función que retorna una lista de tuplas
# con los tiempos promedio de ordenamiento para cada n,
# utilizando el generador de listas proporcionado. Éste último
# es el que determina el tipo de caso presentado (mejor, peor o promedio).
# Es decir, retorna:
# [(Tiempo QuickSort promedio para 1000 elementos, Tiempo InsertionSort promedio para 1000 elementos),
#  (Tiempo QuickSort promedio para 2000 elementos, Tiempo InsertionSort promedio para 2000 elementos),
#  (Tiempo QuickSort promedio para 5000 elementos, Tiempo InsertionSort promedio para 5000 elementos),
#  (Tiempo QuickSort promedio para 10000 elementos, Tiempo InsertionSort promedio para 10000 elementos)]
def computeAvgTimesArr(listGenerator):
    # Lista con las tuplas de tiempos promedios para cada n.
    AVG_TIMES = []
    # Calcular los tiempos promedio para cada n y agregar la tupla respectiva a la lista
    for n in X_ARR:
        # Lista que contendrá 3 tuplas con los tiempos obtenidos para n
        TIMES_FOR_N = []
        # Calcular 3 veces el tiempo de los algoritmos, ordenando
        # listas diferentes en cada iteración (utilizando el generador dado)
        for i in range(3):
            arr = listGenerator(n)
            TIMES_FOR_N.append(sortAndGetTimes(arr))

        # Calcular el promedio de tiempo para cada algoritmo
        firstMean = numpy.mean([t[0] for t in TIMES_FOR_N])
        print("Tiempo promedio", ALG1_NAME, "para", n, "elementos:", firstMean)
        secondMean = numpy.mean([t[1] for t in TIMES_FOR_N])
        print("Tiempo promedio", ALG2_NAME, "para", n, "elementos:", secondMean, "\n")
        # Agregar la tupla de tiempo promedio obtenida
        AVG_TIMES.append((firstMean, secondMean))
    return AVG_TIMES


# Función que se encarga de realizar el test para
# el caso correspondiente (determinado por el generador de listas).
# Obtiene una lista de tuplas con los tiempos promedios para cada n,
# y finalmente la grafica.
def testAndPlot(listGenerator, title):
    print(title, "\n")
    AVG_TIMES = computeAvgTimesArr(listGenerator)

    fig, ax = plt.subplots()
    ax.set_title(title)
    ax.set_xlabel("Tamaño del arreglo")
    ax.set_ylabel("Tiempo de ejecución")
    ax.plot(X_ARR, [y[0] for y in AVG_TIMES])
    ax.plot(X_ARR, [y[1] for y in AVG_TIMES])
    ax.legend([ALG1_NAME, ALG2_NAME])


# Casos con sus respectivos generadores de listas

def casoPromedio():
    # Devuelve una lista aleatoria de tamaño n
    def listGenerator(n):
        return [random.randint(MIN_VALUE, MAX_VALUE) for j in range(n)]

    testAndPlot(listGenerator, "CASO PROMEDIO")


def mejorCaso():
    # Devuelve una lista aleatoria ordenada de tamaño n
    def listGenerator(n):
        arr = [random.randint(MIN_VALUE, MAX_VALUE) for j in range(n)]
        arr.sort()
        return arr

    testAndPlot(listGenerator, "MEJOR CASO")


def peorCaso():
    # Devuelve una lista aleatoria ordenada de forma inversa, de tamaño n
    def listGenerator(n):
        arr = [random.randint(MIN_VALUE, MAX_VALUE) for j in range(n)]
        arr.sort()
        arr.reverse()
        return arr

    testAndPlot(listGenerator, "PEOR CASO")


casoPromedio()
mejorCaso()
peorCaso()
plt.show()
