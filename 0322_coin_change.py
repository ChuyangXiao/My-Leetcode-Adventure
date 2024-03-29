# -*- coding: utf-8 -*-
"""322. Coin Change.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lDSNQ_CWANsPzumhj1_M1XpkIn-HrXvN
"""

class Solution(object):

    def coinChange(self, coins, amount):
        def func(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                 return float('infinity')
            elif amount in dp:
                return dp[amount]
            dp[amount] = min([1+func(amount-coin) for coin in coins])
            return dp[amount]
        dp = {}
        ans = func(amount)
        return ans if ans != float('infinity') else -1