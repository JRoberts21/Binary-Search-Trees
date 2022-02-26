"""
Jonathan Roberts
BST sort traversals and timer

This Program creates a binary search tree, and stores 1000 random
values. The tree is then traversed in either inorder, preorder or postorder.
The height of the tree plus the time the traversal took is diplayed. 

"""

from random import seed
from random import randint
import time
import sys

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


# determines the height of a binary search tree
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






root = None
root2 = None

#generates and inserts the random numbers into the binary search trees 
for _ in range(1000):
    value = randint(1,200)
    root = insert(root, value)
   

def inorderTraversal(): 

    tic = time.perf_counter()
    print("Inorder traversal of the given tree")
    inorder(root)
    toc = time.perf_counter()
    print(f"inorder traversal took {toc - tic:0.4f} seconds")
    print("Height of the binary tree is: " + str(height(root)))

def postorderTraversal():
    tic = time.perf_counter()
    print("Inorder traversal of the given tree")
    printPostorder(root)
    toc = time.perf_counter()
    print(f"Post order traversal took {toc - tic:0.4f} seconds")
    print("Height of the binary tree is: " + str(height(root)))

def preorder():
    tic = time.perf_counter()
    print("Inorder traversal of the given tree")
    printPreorder(root)
    toc = time.perf_counter()
    print(f"Pre-order traversal took {toc - tic:0.4f} seconds")
    print("Height of the binary tree is: " + str(height(root)))


#This is to select the traversal method of the BST    
val = input("Enter inorder, preorder, or postorder: ")

if (val == "inorder"):
    inorderTraversal()
if (val =="postorder"):
    postorderTraversal()
if (val == "preorder"):
    preorder()
    