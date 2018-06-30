#Check if a tree is BST

MAX = 4294967296
MIN = -4294967296

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isBST(root):
    return isBST(root, MAX, MIN)

def isBSTHelper(root, maxi, mini):
    if root is None:
        return True

    if root.data > maxi or root.data < mini:
        return False
    return isBST(root.left, root.data-1, mini) and isBST(root.right, maxi, root.data+1)
