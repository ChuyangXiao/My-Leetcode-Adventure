# -*- coding: utf-8 -*-
"""269. Alien Dictionary.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z9FbggCvzenM5YytxMtSjsyU0TdHA6aJ
"""

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # create a dict to store the adjecent characters
        # w[j] is the set containing the letter bigger than 
        adj = {c:set() for w in words for c in w}
        
        for i in range(len(words)-1):
            
            w1,w2 = words[i], words[i+1]
            
            minL = min(len(w1), len(w2))
            
            # if two continuous words have same prefix yet the former is longer
            # we consider it an invalid order
            if w1[:minL] == w2[:minL] and len(w1) > len(w2):
                return ""
            
            for j in range(minL):
                
                # find the first different character in two words
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        # create a dict to record the visiting status
        # Not in visited - has not been visited
        # True - current path, False - visited
        visited = {}
        res = []
        
        def dfs(c):
            
            # find whether c is visited
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for nei in adj[c]:
                
                # if one of the neighbors in the current path
                if dfs(nei):
                    return True
            
            # consider this character visited
            visited[c] = False
            
            res.append(c)
        
        for c in adj:
            # if dfs[c] = True, it indicates that there is a loop
            # and the original order is invalid
            if dfs(c):
                return ""
        
        res.reverse()
        
        return "".join(res)