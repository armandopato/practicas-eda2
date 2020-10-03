def bubbleSort(a):
    n = len(a)

    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                swap = True
                a[j], a[j + 1] = a[j + 1], a[j]

        if not swap:
            break
