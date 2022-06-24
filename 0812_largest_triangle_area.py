# -*- coding: utf-8 -*-
"""812. Largest Triangle Area.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vJCWVDuwsJN1uNmzvEkaV38DNr85JA56
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)
        for i in range(n):
            for j in range(i , n):
                for k in range(j , n):
                    d1 = math.dist(points[i] , points[j])
                    d2 = math.dist(points[j] , points[k])
                    d3 = math.dist(points[k] , points[i])
                    s = (d1 + d2 + d3)/2
                    area = abs(s*(s-d1)*(s-d2)*(s-d3))**0.5
                    max_area = max(max_area , area)
                    
        return max_area