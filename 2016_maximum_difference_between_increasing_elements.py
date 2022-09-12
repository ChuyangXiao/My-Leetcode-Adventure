# -*- coding: utf-8 -*-
"""2016. Maximum Difference Between Increasing Elements.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rkBZc-gJ6L6BQ8wbcw6fkHJJgyHS6hsd
"""

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prices = nums
        left = 0 #Buy
        right = 1 #Sell
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            
            if prices[left] < prices[right]:
                max_profit =max(currentProfit,max_profit)
            # Swap the two pointers if new minimal value appears
            else:
                left = right
            right += 1
            
        return max_profit if max_profit> 0 else -1