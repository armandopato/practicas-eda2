import random

from BTree import BTree


def test():
    tree = BTree(2)
    toInsert = [3, 1, 4, 2, 5, 7, 6, 11, 15, 22, 35, 21]
    for key in toInsert:
        tree.insert(key)
    tree.printPreOrder()
    print()
    tree.printInOrder()
    print()
    toSearch = [3, 6, 15, 0, 13]
    for key in toSearch:
        found = tree.search(key)
        if found is None:
            print("No se encontró el elemento", key)
        else:
            print("Elemento", key, "encontrado")

    newTree = BTree(2)
    toInsertScrambled = toInsert.copy()
    random.shuffle(toInsertScrambled)
    for key in toInsertScrambled:
        newTree.insert(key)
    print()
    newTree.printPreOrder()
    print()

    randomElements = [random.randint(-100000, 100000) for _ in range(1000)]
    largeTree = BTree(6)
    for key in randomElements:
        largeTree.insert(key)
    largeTree.printPreOrder()
