# -*- coding: utf-8 -*-
"""2022. Convert 1D Array Into 2D Array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13FZmeKRL3kIcTQ_jwt828kAa1KeoFWDO
"""

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        r=len(original)
        if(r!=m*n):
            return []
        ret=[]
        x=0
        for i in range(m):
            a=[]
            for j in range(n):
                a.append(original[x])
                x+=1
            ret.append(a)
        return ret
