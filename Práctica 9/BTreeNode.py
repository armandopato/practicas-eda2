class BTreeNode:
    def __init__(self, minimumDegree: int):
        self.numberOfKeys: int = 0
        self.isLeaf: bool = True
        self.keys: [int] = [None] * (minimumDegree * 2 - 1)
        self.pointersToChildren: [BTreeNode] = [None] * (minimumDegree * 2)
