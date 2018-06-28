# Print inorder traversal as a single line
def inOrder(root):
    if root == None:
        return
    inOrder(root.left)
    print root.info,
    inOrder(root.right)

# Print preorder traversal as a single line
def preOrder(root):
    if root == None:
        return
    print root.info,
    preOrder(root.left)
    preOrder(root.right)

# Print postorder traversal as a single line
def postOrder(root):
    if root == None:
        return    
    preOrder(root.left)
    preOrder(root.right)
    print root.info,

# Level order tree traversal
def levelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printLevel(root, i)

def printLevel(root, l):
    if root is None:
        return
    if l is 1:
        print root.info,
    printLevel(root.left, l-1)
    printLevel(root.right, l-1)

def height(root):
    if root == None:
        return 0
    return max(height(root.left), height(root.right)) + 1
