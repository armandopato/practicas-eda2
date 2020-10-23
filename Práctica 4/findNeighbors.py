import math


# Wrapper de búsqueda binaria modificada
# Esta versión retorna el índice donde el elemento
# debería estar, en caso de no encontrarse
def modifiedBinarySearch(arr, toSearch):
    return binarySearchAux(arr, 0, len(arr) - 1, toSearch)


def binarySearchAux(arr, start, end, toSearch):
    if start > end:
        # Retornar índice correspondiente
        return start

    halfIndex = (start + end) // 2
    if arr[halfIndex] == toSearch:
        return halfIndex
    elif arr[halfIndex] > toSearch:
        return binarySearchAux(arr, start, halfIndex - 1, toSearch)
    else:
        return binarySearchAux(arr, halfIndex + 1, end, toSearch)


def findClosestNeighbors(arr, num_neighbors, max_range, toSearch):
    # Asegurarnos de que el arreglo está ordenado
    # para ejecutar la búsqueda
    copy = arr.copy()
    copy.sort()
    index = modifiedBinarySearch(copy, toSearch)
    neighbors = []

    def getDifference(idx):
        return abs(copy[idx] - toSearch)

    # Índices de los posibles elementos
    # más cercanos a agregar
    leftPointer = index - 1
    rightPointer = index

    # Diferencia entre los elementos anteriores
    # y el elemento buscado
    differenceRight = getDifference(rightPointer)
    differenceLeft = math.inf
    if leftPointer >= 0:
        differenceLeft = getDifference(leftPointer)

    # Añadir vecinos mientras aún no se haya cumplido con el número solicitado
    # y aún haya candidatos
    while len(neighbors) < num_neighbors and (differenceLeft <= max_range or differenceRight <= max_range):
        # En este punto ambos vecinos candidatos están dentro del rango

        # La distancia al vecino izquierdo es menor o igual
        if differenceLeft <= differenceRight:
            neighbors.append(copy[leftPointer])
            leftPointer -= 1
            # Si se ha llegado al principio del arreglo,
            # invalidar la diferencia izquierda
            if leftPointer == -1:
                differenceLeft = math.inf
            else:
                differenceLeft = getDifference(leftPointer)
        # La distancia al vecino derecho es mayor
        else:
            neighbors.append(copy[rightPointer])
            rightPointer += 1
            # Si se ha llegado al final del arreglo,
            # invalidar la diferencia derecha
            if rightPointer == len(copy):
                differenceRight = math.inf
            else:
                differenceRight = getDifference(rightPointer)

    neighbors.sort()
    return neighbors


print(findClosestNeighbors([10, 30, 60, 72, 80, 82, 84, 85, 86, 88, 90, 91, 92, 94, 97, 100], 10, 10, 84))
print(findClosestNeighbors([3, 5, 22, 40, 42, 43, 45, 47, 55], 5, 2, 41.5))
