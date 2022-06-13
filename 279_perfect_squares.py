# -*- coding: utf-8 -*-
"""279. Perfect Squares.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CwGuufUwa75J3v38rMyiOCNLu-xsLB7j
"""

import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Lagrange's four-square theorem: 
        # any positive integer could be written as the sum of atmost 4 other integers
        # And n is the sum of exactly 4 integers' squares iff n = 4^a * (8b+7)
        while n%4 == 0:
            n = n/4

        if n % 8 == 7:
            return 4
        
        a = 0
        while (a * a) <= n:
            b = int(math.sqrt(n-a*a))
            if a * a + b * b == n:
                if a != 0 and b != 0:
                    return 2
                else:
                    return 1
            a = a +1
        return 3

"""In this case, we employed the established  that states that """