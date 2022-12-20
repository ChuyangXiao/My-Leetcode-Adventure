# -*- coding: utf-8 -*-
"""16. 3Sum Closest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18EG39kZJlDKGvbi4qeOzKkOj1t_sMZHl
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n= len(nums)
        
        min_sum=sys.maxsize
        for i in range(n-2):
            start,end= i+1,n-1
            while start < end:
                curr_sum= nums[i] + nums[start] + nums[end]
                if(curr_sum>target):
                    end-=1
                elif curr_sum<target:
                    start+=1
                else:
                    return curr_sum
                if abs(curr_sum-target)<abs(min_sum-target):
                    min_sum=curr_sum
        
        return min_sum