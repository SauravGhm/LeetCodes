from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right  = right

class BinaryTree:
    def rightsideview(self, root: Optional[TreeNode])->List[int]:
        

