# -*- coding: utf-8 -*-
"""673. Number of Longest Increasing Subsequence.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c2U_rizwGGnHBdY7P8lWw6HMQWMOO7MA
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*(n)
        count=[1]*(n)
        
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i]<dp[j]+1:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[i]==dp[j]+1:
                        count[i]+=count[j]
        
        max_length=max(dp)
        
        return sum(count[i] for i in range(n) if dp[i]==max_length)