def binarySearch(arr, toSearch):
    return binarySearchAux(arr, 0, len(arr), toSearch)


def binarySearchAux(arr, start, end, toSearch):
    if start > end:
        return -1

    halfIndex = (start + end) // 2
    if arr[halfIndex] == toSearch:
        return halfIndex
    elif arr[halfIndex] > toSearch:
        return binarySearchAux(arr, start, halfIndex - 1, toSearch)
    else:
        return binarySearchAux(arr, halfIndex + 1, end, toSearch)
