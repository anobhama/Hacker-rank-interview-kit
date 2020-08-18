"""
Function Description

Complete the function checkBST in the editor below. It must return a boolean denoting whether or not the binary tree is a binary search tree.

checkBST has the following parameter(s):

root: a reference to the root node of a tree to test
Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.
Output Format

Your function must return a boolean true if the tree is a binary search tree. Otherwise, it must return false.
"""
  
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    if root == None:
        return True
    if checkRight(root.right, root.data) and checkLeft(root.left, root.data) and checkBST(root.left) and checkBST(root.right):
        return True
    else:
        return False


def checkRight(root, data):
    if root == None:
        return True
    if root.data > data and checkRight(root.left, data) and checkRight(root.right, data):
        return True
    else:
        return False


def checkLeft(root, data):
    if root == None:
        return True
    if root.data < data and checkLeft(root.left, data) and checkLeft(root.right, data):
        return True
    else:
        return False
