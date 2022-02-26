from random import seed
from random import randint
import time
height = 0;

class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    #this searches the BST1
    def findval(self, lkpval):
        if lkpval < self.key:
            if self.left is None:
                return str(lkpval)+"Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.key:
            if self.right is None:
                return str(lkpval)+"Not Found"
            return self.right.findval(lkpval)
        else:
            return(str(self.key) + 'is found')

def count_nodes(node):
    if node is None:
        return 0
    return( 1 + count_nodes(node.left) +count_nodes(node.right))

# inorder traversal 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def inorder2(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

# postorder traversal
def printPostorder(root):
 
    if root:
 
        # First recur on left child
        printPostorder(root.left)
 
        # the recur on right child
        printPostorder(root.right)
 
        # now print the data of node
        print(root.key),

# preorder traversal 
def printPreorder(root):
 
    if root:
 
        # First print the data of node
        print(root.key),
 
        # Then recur on left child
        printPreorder(root.left)
 
        # Finally recur on right child
        printPreorder(root.right)


# new node with given key in BST
def insert(node, key):
 
    # If the tree is empty,
    # return a new node
    if node is None:
        return Node(key)
 
    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    # return the (unchanged) node pointer
    return node


# delete the key and returns the new root
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # Recursive calls for ancestors of
    # node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
 
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        return root
 
    # We reach here when root is the node
    # to be deleted.
     
    # If root node is a leaf node
     
    if root.left is None and root.right is None:
          return None
 
    # If one of the children is empty
 
    if root.left is None:
        temp = root.right
        root = None
        return temp
 
    elif root.right is None:
        temp = root.left
        root = None
        return temp
 
    # If both children exist
 
    succParent = root
 
    # Find Successor
 
    succ = root.right
 
    while succ.left != None:
        succParent = succ
        succ = succ.left
 
    # Delete successor.Since successor
    # is always left child of its parent
    # we can safely make successor's right
    # right child as left of its parent.
    # If there is no succ, then assign
    # succ->right to succParent->right
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
 
    # Copy Successor Data to root
 
    root.key = succ.key
 
    return root

# *slaps roof of function
# this bad boy can determine the height of a binary search tree
def height(root):
 
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0 
    # Recursively call height of each node
    leftAns = height(root.left)
    rightAns = height(root.right)
 
    # Return max(leftHeight, rightHeight) at each iteration
    return max(leftAns, rightAns) + 1








#BST2
class Node2:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.key2 = key
        self.left2 = None
        self.right2 = None

    #this searches the BST1
    def findval(self, lkpval):
        if lkpval < self.key:
            if self.left is None:
                return str(lkpval)+"Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.key:
            if self.right is None:
                return str(lkpval)+"Not Found"
            return self.right.findval(lkpval)
        else:
            return(str(self.key) + 'is found')

def inorder2(root):
    if root is not None:
        inorder2(root.left2)
        print(root.key2, end=" ")
        inorder2(root.right2)


def printPreorder2(root):
 
    if root:
 
        # First print the data of node
        print(root.key2),
 
        # Then recur on left child
        printPreorder2(root.left2)
 
        # Finally recur on right child
        printPreorder2(root.right2)

def printPostorder2(root):
 
    if root:
 
        # First recur on left child
        printPostorder2(root.left2)
 
        # the recur on right child
        printPostorder2(root.right2)
 
        # now print the data of node
        print(root.key),


def insert2(node, key):
    # If the tree is empty,
    # return a new node
    if node is None:
        return Node2(key)
 
    # Otherwise recur down the tree
    if key < node.key2:
        node.left2 = insert2(node.left2, key)
    else:
        node.right2 = insert2(node.right2, key)
 
    # return the (unchanged) node pointer
    return node






#this generates and inserts the random numbers into the binary search trees 
root = None
root2 = None
for _ in range(100):
    value = randint(1,200)
    root = insert(root, value)

tic = time.perf_counter()
for _ in range(10):
    value = randint(1,200)
    root2 = insert2(root2, value)
    root = deleteNode(root,value)
toc = time.perf_counter()
        
    
    
   
    

#this is the code to initiate the different traversals, I commented them in and out as needed

#task1
"""
tic = time.perf_counter()
print("Inorder traversal of the given tree")
printPreorder(root)
toc = time.perf_counter()
print(f"inorder traversal took {toc - tic:0.4f} seconds")
print("Height of the binary tree is: " + str(height(root)))
"""

# task 2
"""
tic = time.perf_counter()
print("inorder traversal of bst2")
printPreorder2(root2)
toc = time.perf_counter()
print(f"inorder traversal took {toc - tic:0.4f} seconds")
"""

"""
print("\nDelete 20")
root = deleteNode(root, 20)
"""

#task 3
"""
print("Inorder traversal of the modified tree")
inorder(root)
print("Height of the binary tree is: " + str(height(root)))
print(f"deletion took {toc - tic:0.4f} seconds")
numberOfNodes = count_nodes(root)
print(numberOfNodes)
"""
print("tree is not empty")
tic = time.perf_counter()
class newNode:
 
    # Construct to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 

def deleteTree( node) :
 
  if node != None:
    deleteTree(node.left)
    deleteTree(node.right)
    del node
 

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    deleteTree(root)
    root = None
 
    print("Tree deleted ")
toc = time.perf_counter()
print(f"deletion took {toc - tic:0.4f} seconds")
