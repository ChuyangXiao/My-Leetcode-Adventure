# -*- coding: utf-8 -*-
"""448. Find All Numbers Disappeared in an Array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fSJqVz5AtlOT_wvV5o3bO_rHgyKWWPiK
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = []
        nums = set(nums)
        for i in range(1, length+1):
            if i not in nums:
                result.append(i)
        return result