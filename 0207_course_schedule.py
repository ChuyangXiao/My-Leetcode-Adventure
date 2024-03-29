# -*- coding: utf-8 -*-
"""207. Course Schedule.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11K3nnzH4LSApgr2a8Wlp_KHJj06j9qmY
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = { i:[] for i in range(numCourses) }
        
        for pre, crs in prerequisites:
            premap[crs].append(pre)
        
        # Create a set to detect the cycle
        
        visited = set()
        
        def dfs(crs):
            
            # If a course is visited again we consider a cycle exist
            if crs in visited:
                return False
            
            # If no prerequisite
            elif premap[crs] == []:
                return True
            
            else:
                visited.add(crs)
                
                for pre in premap[crs]:
                    
                    # If one of the pres is not in a cycle
                    if dfs(pre)==False:
                        return False
                
                visited.remove(crs)
                
                premap[crs] = []
                
                return True
        for crs in range(numCourses):
            
            if dfs(crs) == False: return False
        
        return True