import math

from color_enum import Color


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        self.color = Color.WHITE
        self.distance = math.inf
        self.parent = None

    def addNeighbor(self, newNeighbor):
        for neighbor in self.neighbors:
            if neighbor.name == newNeighbor.name:
                raise KeyError("Repeated key")

        self.neighbors.append(newNeighbor)

    def __neighborsToString(self):
        base = "[ "
        numNeighbors = len(self.neighbors)

        for i in range(numNeighbors - 1):
            base += str(self.neighbors[i].name) + ", "

        last = self.neighbors[numNeighbors - 1].name if numNeighbors > 0 else ""
        return base + str(last) + " ]"

    def __str__(self):
        return str(self.name) + " -> " + self.__neighborsToString()

    def __repr__(self):
        base = "Name: {0}\nColor: {1}\nDistance: {2}\n{3}\nNeighbors: {4}\n"
        hasParent = "Does not have a parent node" if self.parent is None else ("Parent name: " + str(self.parent.name))
        return base.format(self.name, self.color.value, self.distance, hasParent, self.__neighborsToString())
