# -*- coding: utf-8 -*-
"""1748. Sum of Unique Elements.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17AoeVNwxy8p6i8izGro-LffnZ1VnoDBL
"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        count = Counter(nums)
        result = 0
        for i in set(nums):
            if count[i] == 1:
                result = result+i
        return result