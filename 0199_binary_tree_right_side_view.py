# -*- coding: utf-8 -*-
"""199. Binary Tree Right Side View.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j_PO9vYCJidmmZ--oGdly7csEDNKbLIG
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        
        q = collections.deque([root])
        
        # Iterate through each layer until the queue is empty
        while q:
            rightside = None
            length = len(q)
            
            # Iterate through each element in one layer
            for i in range(len(q)):
                
                # Extract the left most element from the queue
                node = q.popleft()
                
                if node:
                    rightside = node
                    
                    # Append the elememt in the next layer to the queue
                    q.append(node.left)
                    q.append(node.right)
                    
            if rightside:
                res.append(rightside.val)
                
        return res