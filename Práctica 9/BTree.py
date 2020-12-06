from BTreeNode import BTreeNode


class BTree:
    def __init__(self, minimumDegree: int):
        self.minimumDegree = minimumDegree
        self.root = BTreeNode(minimumDegree)

    def search(self, key: int):
        return self.__searchAux(key, self.root)

    def __searchAux(self, key: int, toSearchIn: BTreeNode):
        i = 0
        while i < toSearchIn.numberOfKeys and key > toSearchIn.keys[i]:
            i += 1
        if i < toSearchIn.numberOfKeys and key == toSearchIn.keys[i]:
            return toSearchIn, i
        elif toSearchIn.isLeaf:
            return None
        else:
            return self.__searchAux(key, toSearchIn.pointersToChildren[i])

    def __splitChild(self, parent: BTreeNode, toSplitIndex: int):
        newSibling = BTreeNode(self.minimumDegree)
        toSplitNode: BTreeNode = parent.pointersToChildren[toSplitIndex]
        newSibling.isLeaf = toSplitNode.isLeaf
        newSibling.numberOfKeys = self.minimumDegree - 1

        for i in range(self.minimumDegree - 1):
            newSibling.keys[i] = toSplitNode.keys[i + self.minimumDegree]

        if not toSplitNode.isLeaf:
            for j in range(self.minimumDegree):
                newSibling.pointersToChildren[j] = toSplitNode.pointersToChildren[j + self.minimumDegree]
        toSplitNode.numberOfKeys = self.minimumDegree - 1

        for i in range(parent.numberOfKeys, toSplitIndex, -1):
            parent.pointersToChildren[i + 1] = parent.pointersToChildren[i]
        parent.pointersToChildren[toSplitIndex + 1] = newSibling

        for i in range(parent.numberOfKeys - 1, toSplitIndex - 1, -1):
            parent.keys[i + 1] = parent.keys[i]
        parent.keys[toSplitIndex] = toSplitNode.keys[self.minimumDegree - 1]
        parent.numberOfKeys += 1

    def __insertNonFull(self, toInsertIn: BTreeNode, key: int):
        i = toInsertIn.numberOfKeys - 1
        if toInsertIn.isLeaf:
            while i >= 0 and key < toInsertIn.keys[i]:
                toInsertIn.keys[i + 1] = toInsertIn.keys[i]
                i -= 1
            toInsertIn.keys[i + 1] = key
            toInsertIn.numberOfKeys += 1
        else:
            while i >= 0 and key < toInsertIn.keys[i]:
                i -= 1
            i += 1
            if toInsertIn.pointersToChildren[i].numberOfKeys == 2 * self.minimumDegree - 1:
                self.__splitChild(toInsertIn, i)
                if key > toInsertIn.keys[i]:
                    i += 1
            self.__insertNonFull(toInsertIn.pointersToChildren[i], key)

    def insert(self, key):
        root = self.root
        if root.numberOfKeys == 2 * self.minimumDegree - 1:
            newRoot = BTreeNode(self.minimumDegree)
            newRoot.isLeaf = False
            newRoot.numberOfKeys = 0
            newRoot.pointersToChildren[0] = root
            self.root = newRoot
            self.__splitChild(newRoot, 0)
            self.__insertNonFull(newRoot, key)
        else:
            self.__insertNonFull(root, key)

    def printPreOrder(self):
        self.__printPreOrderAux(self.root, "")

    def __getAllKeysString(self, node: BTreeNode):
        keysString = ""
        for i in range(node.numberOfKeys):
            keysString += str(node.keys[i]) + " "
        return keysString

    def __printPreOrderAux(self, root: BTreeNode, initialString: str):
        if root is None:
            return
        allKeysString = self.__getAllKeysString(root)
        print(initialString + allKeysString)
        for i in range(root.numberOfKeys + 1):
            self.__printPreOrderAux(root.pointersToChildren[i], initialString + " " * (len(allKeysString) - 1))

    def printInOrder(self):
        orderedList = []
        self.__printInOrderAux(self.root, orderedList)
        listString = ""
        for key in orderedList:
            listString += str(key) + " "
        print(listString)

    def __printInOrderAux(self, node: BTreeNode, orderedList: [int]):
        if node is None:
            return
        for i in range(node.numberOfKeys):
            self.__printInOrderAux(node.pointersToChildren[i], orderedList)
            orderedList.append(node.keys[i])

        self.__printInOrderAux(node.pointersToChildren[node.numberOfKeys], orderedList)
