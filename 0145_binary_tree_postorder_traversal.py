# -*- coding: utf-8 -*-
"""145. Binary Tree Postorder Traversal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19lS_HKTZSRu4_71bP3ONh2PhTYlx8X6t
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        if root:
            
            output += self.postorderTraversal(root.left)
            
            output += self.postorderTraversal(root.right)
            
            output.append(root.val)
        return output