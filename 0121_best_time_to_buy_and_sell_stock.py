# -*- coding: utf-8 -*-
"""121. Best Time to Buy and Sell Stock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ggoA0m_tyX6MFG9LfliBNV46Huz_YXsp
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
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
        return max_profit