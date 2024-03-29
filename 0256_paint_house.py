# -*- coding: utf-8 -*-
"""256. Paint House.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1411sW6eDyl6qL-sjgV3HsnKu4a3Rb-7U
"""

class Solution:

  '''
  Core idea: us a 3 entries array to store the minimal cost to paint the i-th 
  House into each color
  '''
    def minCost(self, costs: List[List[int]]) -> int:
        
        dp = [0, 0, 0]
        
        for i in range(len(costs)):
            
            dp0 = costs[i][0] + min(dp[1], dp[2])
            dp1 = costs[i][1] + min(dp[0], dp[2])
            dp2 = costs[i][2] + min(dp[1], dp[0])
            
            dp = [dp0, dp1, dp2]
        
        return min(dp)