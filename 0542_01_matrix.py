# -*- coding: utf-8 -*-
"""542. 01 Matrix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_GNNaGSd7_N8NJ0bQBPpgybRRUR1hm_I
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # create a list to store the visited cells
        q = []
        
        # Swap all 1 into #
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = '#'
        
        for r,c in q:
            coor = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for row, col in coor:
                # Begin from each 0 in mat
                # Swap all # according if there is a non # nearby
                if 0<= row < m and 0<=col <n and mat[row][col] == "#":
                    mat[row][col] = mat[r][c]+1
                    q.append((row,col))
        
        return mat