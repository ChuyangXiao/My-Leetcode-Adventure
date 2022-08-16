# -*- coding: utf-8 -*-
"""861. Score After Flipping Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w4IuwnDkyTY42-xCOqHpswR_YAgmYCgA
"""

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def _flippRow(grid,rdx):
            for i in range(len(grid[rdx])):grid[rdx][i]=1-grid[rdx][i]
            return grid
        
        def _flippCol(grid,cdx):
            for i in range(len(grid)):grid[i][cdx]=1-grid[i][cdx]
            return grid
        
        for rdx in range(len(grid)):
            if grid[rdx][0]==0:grid=_flippRow(grid,rdx)
        
        for cdx in range(len(grid[0])):
            zcnt=sum([1 if grid[r][cdx]==0 else 0 for r in range(len(grid))])
            if zcnt>len(grid)-zcnt:grid=_flippCol(grid,cdx)
        
        return sum([reduce(lambda x,y:x*2+y,r) for r in grid])