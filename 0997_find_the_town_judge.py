# -*- coding: utf-8 -*-
"""997. Find the Town Judge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w2cfdazaWhczjdZaSHMks07Sfkurmftr
"""

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        for pair in trust:
            a,b = pair
            graph[a].append(b)
      
        nominees = []
        for person in range(1,n+1):
            if person not in graph:
                nominees.append(person)
              
        if len(nominees) == 1:
            nominee = nominees[0]
            for person in graph:
                if nominee not in graph[person]:
                    return -1
            return nominee
      
        return -1