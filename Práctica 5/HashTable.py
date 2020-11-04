# pip install pycryptodome
import random

from Crypto.Util.number import getPrime

# Longitud del número primo a escoger
PRIME_BITS = 200


class HashTable:
    def __init__(self, initialSize=10):
        self.list = [None] * initialSize
        self.size = 0

        # Obtener a, b y p
        self.LARGE_PRIME = getPrime(PRIME_BITS)
        self.MAX_KEY_VALUE = self.LARGE_PRIME - 1
        self.A = random.randint(1, self.MAX_KEY_VALUE)
        self.B = random.randint(0, self.MAX_KEY_VALUE)
        print("Valor para a:", self.A)
        print("Valor para b:", self.B)
        print("Valor para p:", self.LARGE_PRIME)
        print("Valor key máximo:", self.MAX_KEY_VALUE, "\n")

    class Node:
        def __init__(self, key, satelliteInformation):
            self.key = key
            self.satelliteInformation = satelliteInformation

    def getNumberOfElements(self):
        return self.size

    def getListSize(self):
        return len(self.list)

    def doubleSizeAndRehash(self):
        newHashTable = HashTable(self.size * 2)
        for node in self:
            newHashTable.insertNodeWithoutSizeChecking(node)
        self.list = newHashTable.list
        self.LARGE_PRIME = newHashTable.LARGE_PRIME
        self.MAX_KEY_VALUE = newHashTable.MAX_KEY_VALUE
        self.A = newHashTable.A
        self.B = newHashTable.B

    def __iter__(self):
        for nodeList in self.list:
            if nodeList is not None:
                for node in nodeList:
                    yield node

    def insert(self, key, value):
        if self.search(key) is not None:
            raise ValueError("Duplicate key")
        newNode = self.Node(key, value)
        # Asegurarnos de que el factor de carga
        # siempre sea menor o igual a uno
        if self.size == self.getListSize():
            self.doubleSizeAndRehash()

        self.insertNodeWithoutSizeChecking(newNode)

    def insertNodeWithoutSizeChecking(self, node):
        computed_hash = self.getHash(node.key)

        if self.list[computed_hash] is None:
            self.list[computed_hash] = []

        self.list[computed_hash].append(node)
        self.size += 1

    @staticmethod
    def keyToInt(key):
        j = 1
        totalSum = 0
        for character in key:
            totalSum += ord(character) * j
            j += 1
        return totalSum

    def getHash(self, key):
        prehash = self.keyToInt(key)
        if prehash > self.MAX_KEY_VALUE:
            raise ValueError("Key exceeds max value")
        return (((self.A * prehash) + self.B) % self.LARGE_PRIME) % self.getListSize()

    def search(self, key):
        computed_hash = self.getHash(key)

        if self.list[computed_hash] is None:
            return None

        for node in self.list[computed_hash]:
            if node.key == key:
                return node.satelliteInformation

        return None

    def getLoadFactor(self):
        return self.getNumberOfElements() / self.getListSize()

    def getMaxCollisions(self):
        maxCollisions = 0
        for l in self.list:
            if l is not None:
                maxCollisions = max(len(l), maxCollisions)
        return maxCollisions
