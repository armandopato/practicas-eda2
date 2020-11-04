import math
import random
import time

import numpy

from Database import Usuario
from HashTable import HashTable
from linearSearch import linearSearchUsers
from login import initializeHashTable

# Número de casos a analizar
NUMBER_OF_CASES = 10


# Función que calcula el tiempo utilizado por los algoritmos definidos
# Devuelve una tupla con los tiempos correspondientes
def searchAndGetTimes(arr, toSearch, table):
    print("Username:", toSearch)

    t1 = time.perf_counter()
    table.search(toSearch)
    t2 = time.perf_counter()
    tableSearchTime = t2 - t1
    print("Hash table search:", tableSearchTime)

    t1 = time.perf_counter()
    linearSearchUsers(arr, toSearch)
    t2 = time.perf_counter()
    linearSearchTime = t2 - t1
    print("Linear search:", linearSearchTime, "\n")

    return tableSearchTime, linearSearchTime


def testTimes():
    # Lista con los tiempos de ejecución para cada caso
    TIMES = []
    users = Usuario.GetUsuariosDB(math.inf)
    TOTAL_USERS = len(users)
    hashTable = HashTable(TOTAL_USERS)
    initializeHashTable(hashTable, users)

    # Calcular los tiempos de cada algoritmo y agregar la tupla respectiva a la lista
    for i in range(NUMBER_OF_CASES):
        randomUser = users[random.randint(0, TOTAL_USERS - 1)]
        TIMES.append(searchAndGetTimes(users, randomUser.username, hashTable))

    # Calcular el promedio de tiempo para cada algoritmo
    firstMean = numpy.mean([t[0] for t in TIMES])
    print("Tiempo promedio búsqueda por tabla hash", firstMean)
    secondMean = numpy.mean([t[1] for t in TIMES])
    print("Tiempo promedio búsqueda lineal", secondMean, "\n")
