# -*- coding: utf-8 -*-
"""807. Max Increase to Keep City Skyline.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eZomm1X0hNQ72HOUw-CkeJFRo2DnoMT_
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, a: List[List[int]]) -> int:
        n=len(a)
        d=[max(a[j][i]for j in range(n))for i in range(n)]
        w=-sum(sum(i)for i in a)
        for i in range(n):
            p=max(a[i])
            w+=sum(min(d[j],p)for j in range(n))
        return w