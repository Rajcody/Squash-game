# implementation + traversals, DFS AND BFS
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(root):
    if root:
        print(root.data, end=" "),
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" "),
        inOrder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")


def bst(root):
    h = height(root)
    for _ in range(1, h+1):
        currentLayer(root, _)


def currentLayer(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")

    elif level > 1:
        currentLayer(root.left, level-1)
        currentLayer(root.right, level-1)


def height(root):
    if root is None:
        return 0

    else:
        lheight = height(root.left)
        rheight = height(root.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('PreOrder')
preOrder(root)

print('\nInOrder')
inOrder(root)

print('\npostOrder')
postOrder(root)

print('\nBST')
bst(root)

'''
# inorder traversal without recursion
'''
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def inOrder(root):

  stack =[]
  current = root

  while True:
    if current is not None:
      stack.append(current)

      current = current.left

    elif  stack:
      current = stack.pop()
      print(current.data, end =" ")

      current = current.right

    else:
      break  

root = Node(1)   
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)

print('Inorder')
inOrder(root)
'''
