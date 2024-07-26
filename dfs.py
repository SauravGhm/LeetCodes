class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

def invert_tree(root):
    if root is None:
        return None
    #swap the left and the right children
    root.left, root.right = root.right, root.left
    #implement recursion for the changes to take into effect
    invert_tree(root.left)
    invert_tree(root.right)
    return root
def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i< len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i+=1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i+=1
    return root

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current:
            



    


    
