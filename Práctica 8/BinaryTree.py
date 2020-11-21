from queue import Queue
from typing import Optional

from Node import TreeNode


class BinaryTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None

    def getRoot(self):
        return self.root

    def search(self, key: int):
        return self.__searchAux(self.root, key)

    def __searchAux(self, root: TreeNode, key: int):
        if root is None or root.key == key:
            return root
        elif key < root.key:
            return self.__searchAux(root.left, key)
        else:
            return self.__searchAux(root.right, key)

    def minimum(self, root: TreeNode = None):
        if root is None:
            if self.root is None:
                return None
            root = self.root

        while root.left is not None:
            root = root.left
        return root

    def maximum(self, root: TreeNode = None):
        if root is None:
            if self.root is None:
                return None
            root = self.root

        while root.right is not None:
            root = root.right
        return root

    def successor(self, node: TreeNode):
        if node is None:
            return None

        if node.right is not None:
            return self.minimum(node.right)

        trav = node.parent
        travChild = node

        while trav is not None and trav.right == travChild:
            travChild = trav
            trav = trav.parent

        return trav

    def predecessor(self, node: TreeNode):
        if node is None:
            return None

        if node.left is not None:
            return self.maximum(node.left)

        trav = node.parent
        travChild = node

        while trav is not None and trav.left == travChild:
            travChild = trav
            trav = trav.parent

        return trav

    def insert(self, key: int):
        if self.root is None:
            self.root = TreeNode(key)
            return

        parent = self.root
        if parent.key == key:
            raise KeyError("Repeated key")
        child = parent.left if key < parent.key else parent.right

        while child is not None:
            parent = child
            if parent.key == key:
                raise KeyError("Repeated key")
            child = child.left if key < child.key else child.right

        newNode = TreeNode(key)
        newNode.parent = parent

        if newNode.key < parent.key:
            parent.left = newNode
        else:
            parent.right = newNode

    def __transplant(self, original: TreeNode, replacement: Optional[TreeNode]):
        if original.parent is None:
            self.root = replacement
        elif original == original.parent.left:
            original.parent.left = replacement
        else:
            original.parent.right = replacement

        if replacement is not None:
            replacement.parent = original.parent

    def __deleteAux(self, node: TreeNode):
        if node.left is None:
            self.__transplant(node, node.right)
        elif node.right is None:
            self.__transplant(node, node.left)
        else:
            successor = self.minimum(node.right)
            if successor.parent != node:
                self.__transplant(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.__transplant(node, successor)
            successor.left = node.left
            successor.left.parent = successor

    def delete(self, key: int):
        toDelete = self.search(key)
        if toDelete is not None:
            self.__deleteAux(toDelete)
        else:
            raise KeyError("Key does not exist")

    def print(self):
        if self.root is None:
            return print("El árbol está vacío\n")
        preorder = self.__formatListStr(self.__preorder)
        inorder = self.__formatListStr(self.__inorder)
        postorder = self.__formatListStr(self.__postorder)
        breadth_first = self.__formatListStr(self.__breadth_first_traversal)
        print("Preorder:", preorder)
        print("Inorder:", inorder)
        print("Postorder:", postorder)
        print("Breadth first:", breadth_first, "\n")
        self.__printPretty()
        print()

    def __formatListStr(self, traversalAlg):
        return traversalAlg(self.root)[4:]

    def __inorder(self, root: TreeNode):
        if root is None:
            return ""
        base = self.__inorder(root.left)
        base += " -> " + str(root.key)
        return base + self.__inorder(root.right)

    def __preorder(self, root: TreeNode):
        if root is None:
            return ""
        base = " -> " + str(root.key)
        base += self.__preorder(root.left)
        return base + self.__preorder(root.right)

    def __postorder(self, root: TreeNode):
        if root is None:
            return ""
        base = self.__postorder(root.left)
        base += self.__postorder(root.right)
        return base + " -> " + str(root.key)

    def __breadth_first_traversal(self, root: TreeNode):
        if root is None:
            return ""

        queue: Queue[TreeNode] = Queue()
        base = ""
        queue.put(self.root)

        while not queue.empty():
            current = queue.get()
            base += " -> " + str(current.key)

            if current.left is not None:
                queue.put(current.left)

            if current.right is not None:
                queue.put(current.right)

        return base

    def __getDepth(self):
        if self.root is None:
            return 0

        queue: Queue[TreeNode] = Queue()
        queue.put(self.root)
        depth = 0

        while not queue.empty():
            size = queue.qsize()
            depth += 1

            for _ in range(size):
                current = queue.get()
                if current.left is not None:
                    queue.put(current.left)
                if current.right is not None:
                    queue.put(current.right)

        return depth - 1

    def __printPretty(self):
        if self.root is None:
            return
        maxDepth = self.__getDepth()
        largestLineLength = 2 ** (maxDepth + 2) - 3
        TOTAL_LINES = maxDepth + 1
        TOTAL_EDGE_LINES = 2**(maxDepth + 1) - 1 - maxDepth
        nodesLines = [[" "] * largestLineLength for _ in range(TOTAL_LINES)]
        edgesLines = [[" "] * largestLineLength for _ in range(TOTAL_EDGE_LINES)]

        def __computeEdge(depth: int, position: int, idxMutator, edge: str):

            finalDepth = int(2**(maxDepth + 1) * (-0.5**depth + 1) - depth)
            startDepth = finalDepth - 2**(maxDepth-depth+1) + 2
            currentCharIdx = position
            for currDepth in range(startDepth, finalDepth+1):
                currentCharIdx = idxMutator(currentCharIdx)
                edgesLines[currDepth][currentCharIdx] = edge

        def __computeEdgeLeft(depth: int, position: int):
            def indexMutator(idx: int):
                return idx - 1
            __computeEdge(depth, position, indexMutator, "/")

        def __computeEdgeRight(depth: int, position: int):
            def indexMutator(idx: int):
                return idx + 1
            __computeEdge(depth, position, indexMutator, "\\")

        def __computePrettySubtree(root: TreeNode, depth: int, position: int):
            nodesLines[depth][position] = str(root.key)

            if root.left is not None:
                __computeEdgeLeft(depth + 1, position)
                __computePrettySubtree(root.left, depth + 1, position - 2**(maxDepth - depth))

            if root.right is not None:
                __computeEdgeRight(depth + 1, position)
                __computePrettySubtree(root.right, depth + 1, position + 2**(maxDepth - depth))

        __computePrettySubtree(self.root, 0, largestLineLength // 2)
        print("".join(nodesLines[0]))
        i = 1
        for currentDepth in range(1, maxDepth+1):
            for _ in range(2**(maxDepth - currentDepth + 1) - 1):
                print("".join(edgesLines[i]))
                i += 1

            print("".join(nodesLines[currentDepth]))
