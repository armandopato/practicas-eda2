from graph import Graph


def test():
    graph = Graph()
    for i in range(8):
        graph.addVertex(i)

    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(0, 3)
    graph.addEdge(1, 0)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 1)
    graph.addEdge(2, 3)
    graph.addEdge(3, 0)
    graph.addEdge(3, 2)
    graph.addEdge(3, 4)
    graph.addEdge(4, 3)
    graph.addEdge(4, 5)
    graph.addEdge(4, 6)
    graph.addEdge(5, 4)
    graph.addEdge(5, 6)
    graph.addEdge(6, 4)
    graph.addEdge(6, 5)

    print(graph)

    # Agregar vértice repetido a grafo
    try:
        graph.addVertex(0)
    except KeyError:
        print("No es posible agregar un nodo repetido al grafo")

    # Agregar vecino repetido a nodo
    try:
        node0 = graph.getVertex(0)
        node1 = graph.getVertex(1)
        node0.addNeighbor(node1)
    except KeyError:
        print("No es posible agregar un vecino repetido al nodo")

    # Agregar arista a nodo inexistente
    try:
        graph.addEdge(-1, 0)
    except KeyError:
        print("No es posible agregar una arista a un nodo inexistente")
