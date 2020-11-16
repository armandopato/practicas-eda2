import math

from color_enum import Color
from node import Node
from queue import Queue


class Graph:
    def __init__(self):
        self.vertices = {}
        self.time = 0

    def getVertex(self, nodeName):
        return self.vertices[nodeName]

    def hasVertex(self, nodeName):
        return nodeName in self.vertices

    def addVertex(self, nodeName):
        if self.hasVertex(nodeName):
            raise KeyError("Repeated key")
        newVertex = Node(nodeName)
        self.vertices[nodeName] = newVertex

    def addEdge(self, nodeName1, nodeName2):
        if not self.hasVertex(nodeName1) or not self.hasVertex(nodeName2):
            raise KeyError("Cannot add edge to non-existing node")
        node1 = self.getVertex(nodeName1)
        node2 = self.getVertex(nodeName2)
        node1.addNeighbor(node2)

    def __restore(self):
        self.time = 0
        for node in self.vertices.values():
            node.color = Color.WHITE
            node.distance = math.inf
            node.parent = None
            node.discovered = math.inf
            node.finished = math.inf

    def BFS(self, sourceNodeName):
        if not self.hasVertex(sourceNodeName):
            raise KeyError("Source node does not exist")
        self.__restore()
        source = self.getVertex(sourceNodeName)
        self.__BFSAux(source)

    def __BFSAux(self, source):
        source.distance = 0
        source.color = Color.GRAY
        queue = Queue()
        queue.put(source)

        while not queue.empty():
            current = queue.get()
            for neighbor in current.neighbors:
                if neighbor.color is Color.WHITE:
                    neighbor.color = Color.GRAY
                    neighbor.parent = current
                    neighbor.distance = current.distance + 1
                    queue.put(neighbor)
            current.color = Color.BLACK

    def DFS(self):
        self.__restore()
        for node in self.vertices.values():
            if node.color is Color.WHITE:
                self.__DFS_visit(node)

    def __DFS_visit(self, node):
        self.time += 1
        node.discovered = self.time
        node.color = Color.GRAY
        node.distance = 0 if node.parent is None else node.parent.distance + 1

        for neighbor in node.neighbors:
            if neighbor.color is Color.WHITE:
                neighbor.parent = node
                self.__DFS_visit(neighbor)

        node.color = Color.BLACK
        self.time += 1
        node.finished = self.time

    def __findPathAux(self, sourceNodeName, finalNodeName, searchAlg, algName):
        if not self.hasVertex(sourceNodeName):
            raise KeyError("Source node does not exist")

        if not self.hasVertex(finalNodeName):
            raise KeyError("Final node does not exist")

        self.__restore()
        source = self.getVertex(sourceNodeName)
        final = self.getVertex(finalNodeName)
        searchAlg(source)

        if final.distance is math.inf:
            return print("No existe ningún camino")

        print("Camino", algName, "de", sourceNodeName, "a", finalNodeName)
        print("Número de estaciones:", final.distance + 1)
        print(self.__getPathString(final))

    def __getPathString(self, node):
        if node.parent is None:
            return node.name
        base = self.__getPathString(node.parent)
        return base + " -> " + node.name

    def findPathBFS(self, sourceNodeName, finalNodeName):
        self.__findPathAux(sourceNodeName, finalNodeName, self.__BFSAux, "BFS")

    def findPathDFS(self, sourceNodeName, finalNodeName):
        self.__findPathAux(sourceNodeName, finalNodeName, self.__DFS_visit, "DFS")

    def __str__(self):
        base = ""
        for node in self.vertices.values():
            base += str(node) + "\n"
        return base

    def __repr__(self):
        base = ""
        for node in self.vertices.values():
            base += repr(node) + "\n"
        return base
