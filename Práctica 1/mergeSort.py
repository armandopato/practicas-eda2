def mergeSort(arr):
    n = len(arr)

    if n > 1:
        r = n // 2
        izq = arr[0:r]
        der = arr[r:]
        mergeSort(izq)
        mergeSort(der)
        merge(arr, izq, der)


def merge(arr, izq, der):
    i = 0
    j = 0

    for k in range(len(arr)):
        if j >= len(der) or (i < len(izq) and izq[i] < der[j]):
            arr[k] = izq[i]
            i = i + 1
        else:
            arr[k] = der[j]
            j = j + 1
