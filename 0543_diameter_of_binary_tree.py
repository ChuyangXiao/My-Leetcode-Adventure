# -*- coding: utf-8 -*-
"""543. Diameter of Binary Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-fukD3MbxQOB8IYwRrTNPj33JFyup883
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # Time complexity: O(n) (only iterate through each node once )
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        
        def dfs(node):
            if not node:
                return -1
            else:
                left = dfs(node.left)
                right = dfs(node.right)
                
                res[0] = max(res[0], 2+left+right)
                
                return 1+max(left,right)
        dfs(root)
        
        return res[0]