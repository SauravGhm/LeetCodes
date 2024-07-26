class TreeNode:
    def __init__(self, val = 0, left = None, right = None): 
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
    if root is None:
        return None
    #Swap the left and the right children
    root.left, root.right = root.right, root.left #Main logic for swapping/reversing the elements of the tree. This logic should be called continuously.
    #Recursively invert the left and the right subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    return root
#########################################################
def list_to_tree(lst):
    if not lst: #lst = [1,2,3,4,5,6,7]
        return None
    root = TreeNode(lst[0]) #after this line, 'root' is a TreeNode object with 'val = 1', left= None and right = None , 
    queue = [root] #we are initializing the queue that will be used to facilitate level-order (BFS) traversal and construction of Binary tree
    i = 1
    while i < len(lst):
        current = queue.pop(0) #Retrieve and remove the first element from the queue, queue becomes [] but the current is TreeNode(1)
        if lst[i] is not None:
            current.left = TreeNode(lst[i]) #according to the first iteration, which will continuously change ofc, TreeNode(2) will be the left child of treenode(1)
            queue.append(current.left) #queue becomes [TreeNode(2)]
        i+=1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i+=1
    return root
########################################################
def tree_to_list(root): 
    if not root:
        return []
    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
#Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result


#Input 
lst = [1,2,3,4,5,6,7]

#Construct the binary tree from the input list
listvalue = list_to_tree(lst)

#Invert the binary tree
inverted_root = invert_tree(listvalue)

#Convert the inverted binary tree back to a list
output_list = tree_to_list(inverted_root)

print("Output:", output_list)









    