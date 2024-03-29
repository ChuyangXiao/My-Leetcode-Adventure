# -*- coding: utf-8 -*-
"""366. Find Leaves of Binary Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1abxAK1NJ5gzwnN6Bz2c6HPjKwpUpZ83j
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        while root.val != "End":
            leaves = []
            self.leaf_search(root, leaves)
            result.append(leaves)
         
        return result
        

    def leaf_search(self, root, leaves):
        if root.val != "End": 
            if root.val != "End" and (root.left is None or root.left.val == "End") and (root.right is None or root.right.val == "End"):
                leaves.append(root.val)
                root.val = "End"
            elif root.left or root.right:
                if root.left and root.left.val != "End":
                    self.leaf_search(root.left, leaves)
                if root.right and root.right.val != "End":
                    self.leaf_search(root.right, leaves)