from graph import Graph
from metro import lineas


def test():
    graph = Graph()
    # Inicializar lineas (NOTA: se añadió la estación faltante Oceanía en su posición respectiva en la línea B)
    for linea in lineas:

        current = linea[0]
        if not graph.hasVertex(current):
            graph.addVertex(current)

        for i in range(1, len(linea)):
            current = linea[i]
            if not graph.hasVertex(current):
                graph.addVertex(current)
            graph.addEdge(linea[i - 1], current)
            graph.addEdge(current, linea[i - 1])

    graph.findPathBFS("Aquiles Serdán", "Iztapalapa")
    graph.findPathDFS("Aquiles Serdán", "Iztapalapa")
    print()

    graph.findPathBFS("San Antonio", "Aragón")
    graph.findPathDFS("San Antonio", "Aragón")
    print()

    graph.findPathBFS("Vallejo", "Insurgentes")
    graph.findPathDFS("Vallejo", "Insurgentes")
    print()
