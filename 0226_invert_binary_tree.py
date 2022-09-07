# -*- coding: utf-8 -*-
"""226. Invert Binary Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qaAQzI7XbduSyCJbTq46JMD67Y0zRHky
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        def mirror_Tree(root):
            
            node=TreeNode()
            
            node.val=root.val
            if root.right:
                node.left=mirror_Tree(root.right)
            if root.left:
                node.right=mirror_Tree(root.left)
            return node
        return mirror_Tree(root)