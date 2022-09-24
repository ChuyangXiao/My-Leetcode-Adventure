# -*- coding: utf-8 -*-
"""994. Rotting Oranges.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M1Wba65LZB_LSKYFI_gWUA7gOs8mgCf2
"""

import collections
class Solution:
    
    '''
    Core idea: use multi-source bfs algo
    Each rotten orange will contaminate all its fresh neighbours only once
    Then the newly contaminated oranges will repeat this process
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        # Create a queue to store the rotten oranges
        q = collections.deque()

        victims = 0
        
        time=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    victims += 1
        
        # Two ending conditions:
        while q and victims >0:
            for i in range(len(q)):
                r,c = q.popleft()
            
                coor = [(r-1, c), (r+1, c), (r, c-1), (r,c+1)]
            
                for row, col in coor:
                    if 0<=row< m and 0<=col<n and grid[row][col] == 1:
                        q.append((row, col))
                        grid[row][col] = 2
                        
                        victims -=1
            time +=1
        
        if victims == 0:
            return time
        else:
            return -1