# Author:cfmorris
# Source: Codewars 
# Title: Sort binary tree by levels
# Challenge: Return the list with elements from tree sorted by levels, which means 
# the root element goes first, then root children (from left to right) are second and 
# third, and so on. Return empty list if root is None.
# https://www.codewars.com/kata/52bef5e3588c56132c0003bc


def tree_by_levels(node):
    bento=[node]
    box=[]
    if node == None:
        return  box
    for items in bento:
        if items != None:
            if items.left != None: bento.append(items.left)
            if items.right!= None: bento.append(items.right)
    for items in bento: box.append(items.value)
    return box

# Testing code below
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

a = (tree_by_levels(None))
if a != []: print(False)
else: print("Success!")
b = (tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))
if b != [1, 2, 3, 4, 5, 6]: print(False)
else: print("Success!")