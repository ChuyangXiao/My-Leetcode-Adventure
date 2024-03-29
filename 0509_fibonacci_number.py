# -*- coding: utf-8 -*-
"""509. Fibonacci Number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1602sZkYH8Uxh0b0-_LM8awrt5jmpZ_qN
"""

class Solution:
    def fib(self, n: int) -> int:
        
        res = [0, 1]
        
        for i in range(2, n+1):
            
            res.append(res[i-2]+res[i-1])
            
        
        return res[n]