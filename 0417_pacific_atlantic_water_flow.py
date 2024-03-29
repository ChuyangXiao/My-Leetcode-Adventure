# -*- coding: utf-8 -*-
"""417. Pacific Atlantic Water Flow.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rPLa-sV3sbh86C71GTtQImt7g6wpU2Ec
"""

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights: return []

        m = len(heights)
        n = len(heights[0])
    
        pacific = []
        atlantic = []

        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(x,y,directions,visited, last):

            if x < 0 or x > m-1 or y < 0 or y > n-1 or (x,y) in visited:
                return

            if heights[x][y] < last:
                return

            visited.append((x,y))

            for dx, dy in directions:
                newx = x + dx
                newy = y + dy

                dfs(newx,newy, directions, visited, heights[x][y])

        for i in range(m):
            dfs(i,0,directions, pacific,-1)
            dfs(i,n-1, directions, atlantic, -1)

        for i in range(n):
            dfs(0,i,directions, pacific, -1)
            dfs(m-1, i, directions, atlantic, -1)

        return list(set(pacific)&set(atlantic))