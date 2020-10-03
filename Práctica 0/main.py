import random

N = 10

# Retorna la suma de los valores en una lista
def sumaTotal(arr):
    total = 0
    for j in range(len(arr)):
        total += arr[j]
    return total

# Se crea la lista y se añaden 10 valores aleatorios
randomList = []
for i in range(N):
    randomList.append(random.randint(0, 10))

# Impresión de valores solicitados
print("N =", N)
print("Lista aleatoria:", randomList)
randomList.sort()
print("Lista ordenada:", randomList)
print("Suma total:", sumaTotal(randomList))
