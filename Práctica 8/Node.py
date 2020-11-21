from typing import Optional


class TreeNode:
    def __init__(self, key: int, data: any = None):
        self.key: int = key
        self.data: any = data
        self.parent: Optional[TreeNode] = None
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
