# -*- coding: utf-8 -*-
"""1409. Queries on a Permutation With Key.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QxJQ-tjDl2PVv494xbvLtW3dQQZSPWqK
"""

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1,m+1)]
        ans = []
        for query in queries:
            val = p.index(query)
            ans.append(val)
            p.pop(val)
            p.insert(0, query)
        return ans