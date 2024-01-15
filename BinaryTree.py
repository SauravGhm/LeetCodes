class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def construct_binary_tree(keys):
    if not keys:
        return None

    root = Node(keys[0])
    queue = [root]
    i = 1

    while i < len(keys):
        current_node = queue.pop(0)

        left_key = keys[i]
        i += 1
        if left_key is not None:
            current_node.left = Node(left_key)
            queue.append(current_node.left)

        right_key = keys[i]
        i += 1
        if right_key is not None:
            current_node.right = Node(right_key)
            queue.append(current_node.right)

    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.key, end=' ')
        inorder_traversal(node.right)

# Example usage:
keys = [1, 2, 3, 4, None, 5, 6, None, None, None, None, 7, 8]
root = construct_binary_tree(keys)

print("Inorder Traversal of the constructed binary tree:")
inorder_traversal(root)
