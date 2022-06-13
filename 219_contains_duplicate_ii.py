# -*- coding: utf-8 -*-
"""219. Contains Duplicate II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Dxw6UQrqjbc2KxOQz_imaCtmdpQXSEHS
"""



class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # check whether the duplicate item exists or not
        if len(nums) == len(set(nums)):
            return False
            
        else:
            count = {}
            for i in range(len(nums)):
                if nums[i] not in count.keys():
                    count.update({nums[i]: i})
                else:
                    dis = i - count[nums[i]]
                    if dis <= k:
                        return True
                    else:
                        count[nums[i]] = i
            return False