def linearSearch(arr, toSearch):
    for i in range(0, len(arr)):
        if arr[i] == toSearch:
            return i

    return -1
