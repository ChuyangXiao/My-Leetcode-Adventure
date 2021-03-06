# -*- coding: utf-8 -*-
"""1869. Longer Contiguous Segments of Ones than Zeros.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pb7GV7Sg0iRx2CI4WR1QRPhpBobXbSis
"""

s = "111000"

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        maxOne = 0
        i,j=0,0
        while j < len(s):
            if s[j] == '1':
                maxOne = max(j-i+1,maxOne)
                j+=1
            else:
                j+=1
                i=j
                
        maxzero = 0
        i,j=0,0
        while j < len(s):
            if s[j] == '0':
                maxzero = max(j-i+1,maxzero)
                j+=1
            else:
                j+=1
                i=j
        return maxzero<maxOne

