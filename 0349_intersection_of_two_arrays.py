# -*- coding: utf-8 -*-
"""349. Intersection of Two Arrays.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13clqQfw_m-MqxBenjLURmc287yQP3VsC
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))