# -*- coding: utf-8 -*-
"""310. Minimum Height Trees.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a1yU0wvCaY7acooXiYyxiv6mrrqWENv9
"""

class Solution:
    
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # If there are less than 2 nodes
        # The MHTs are just the two nodes
        if n <= 2:
            return [x for x in range(n)]
        
        # Create a map recording connected neighbors of each node
        neighbors = [set() for x in range(n)] 
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)
        
        leaves = []
        for i in range(n):
            
            # Find the nodes with only one neightbor
            if len(neighbors[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            remaining_nodes -= len(leaves)
            temp = []
            
            for leaf in leaves:
                
                # Remove the nodes on the terminal
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor]) == 1:
                        temp.append(neighbor)
            leaves = temp
        
        return leaves