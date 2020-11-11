from node import Node


class Graph:
    def __init__(self):
        self.vertices = {}

    def getVertex(self, nodeName):
        return self.vertices[nodeName]

    def addVertex(self, nodeName):
        if nodeName in self.vertices:
            raise KeyError("Repeated key")
        newVertex = Node(nodeName)
        self.vertices[nodeName] = newVertex

    def addEdge(self, nodeName1, nodeName2):
        if nodeName1 not in self.vertices or nodeName2 not in self.vertices:
            raise KeyError("Cannot add edge to non-existing node")
        node1 = self.getVertex(nodeName1)
        node2 = self.getVertex(nodeName2)
        node1.addNeighbor(node2)

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
