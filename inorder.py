class Treenode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
    
class BinaryTreeInOrder:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Treenode(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key<node.val:
            if node.left is None:
                node.left = Treenode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                





