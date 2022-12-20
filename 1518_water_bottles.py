# -*- coding: utf-8 -*-
"""1518. Water Bottles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vdjb-h474Rt0LMS16DiF7GiYQFiixiuI
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            new = numBottles // numExchange
            numBottles = new + numBottles%numExchange
            res +=new
        return res