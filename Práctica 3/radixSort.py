import math


def radixSort(arr):
    k = max(arr)
    d = int(math.log10(k) + 1)

    for i in range(d):
        arr = countingSortPosicion(arr, i)

    return arr


def countingSortPosicion(arr, posicion):
    n = len(arr)
    k = 9

    def obtenerDigito(numero):
        return (numero // 10 ** posicion) % 10

    idxArr = [0] * (k + 1)
    final = [0] * n

    for num in arr:
        idxArr[obtenerDigito(num)] += 1

    for i in range(1, k + 1):
        idxArr[i] += idxArr[i - 1]

    for j in range(n - 1, -1, -1):
        toAdd = arr[j]
        digito = obtenerDigito(toAdd)
        idxArr[digito] -= 1
        final[idxArr[digito]] = toAdd

    return final
