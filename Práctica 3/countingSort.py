def countingSort(arr):
    k = max(arr)
    n = len(arr)

    # Arreglo de índices
    idxArr = [0] * (k + 1)
    # Arreglo donde se colocarán los elementos ordenados
    final = [0] * n

    # Colocar numero de ocurrenciss de cada elemento
    for num in arr:
        idxArr[num] += 1

    # Calcular indices
    for i in range(1, k + 1):
        idxArr[i] += idxArr[i - 1]

    # Colocar los elementos en sus respectivas posiciones
    for j in range(n - 1, -1, -1):
        toAdd = arr[j]
        idxArr[toAdd] -= 1
        final[idxArr[toAdd]] = toAdd

    return final
