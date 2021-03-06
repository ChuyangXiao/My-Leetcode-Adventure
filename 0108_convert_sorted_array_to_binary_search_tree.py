# -*- coding: utf-8 -*-
"""108. Convert Sorted Array to Binary Search Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TKp0c6a-4PKxV5Qe2xGydgBwlQG7902C
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def dfs(l,r):
            
            if l>r or l<0 or r<0 or l>=len(nums) or r>=len(nums):
                return None
            
            mid =(l+r)//2
            root=TreeNode(nums[mid])
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            
            return root
        
        return dfs(0,len(nums)-1)