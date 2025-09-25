# Binary Tree Node class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

# Build Tree
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.left.right = Node(7)

print("Inorder Traversal:")
inorder(root)
