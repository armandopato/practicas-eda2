from BinaryTree import BinaryTree


def test():
    tree = BinaryTree()
    tree.print()
    tree.insert(8)
    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(14)
    tree.insert(4)
    tree.insert(7)
    tree.insert(13)
    tree.print()
    try:
        tree.insert(14)  # Repetido, debe mostrar mensaje de error
    except KeyError:
        print("El nodo con llave 14 ya se encuentra en el árbol")
    try:
        tree.insert(1)  # Repetido, debe mostrar mensaje de error
    except KeyError:
        print("El nodo con llave 1 ya se encuentra en el árbol")
    print("Mínimo:", tree.minimum().key)
    print("Máximo:", tree.maximum().key)
    tree.search(4)
    tree.search(8)
    tree.search(13)
    tree.search(2)
    tree.search(15)
    tree.delete(7)  # Borrando el 7 (sin hijos)
    tree.print()
    tree.delete(10)  # Borrando el 10 (solo hijo der)
    tree.print()
    tree.delete(6)  # Borrando el 6 (solo hijo izq)
    tree.print()
    tree.delete(3)  # Borrando el 3 (ambos hijos)
    tree.print()
    try:
        tree.delete(3)  # Borrando el 3 (nodo no existe)
    except KeyError:
        print("El nodo con llave 3 no se encuentra en el árbol")
    tree.print()
    tree.delete(8)  # Borrando el 8 (raíz, ambos hijos)
    tree.print()
    tree.insert(100)
    tree.print()
