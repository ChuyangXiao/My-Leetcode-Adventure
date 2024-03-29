# -*- coding: utf-8 -*-
"""888. Fair Candy Swap.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iumwiLUVPzS0ZLt6VXvtg8MDjTyYWtcI
"""

from collections import Counter
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)     
        
        m = (sumAlice + sumBob) // 2
        
        differencea = m - sumAlice
        
        aC, bC = Counter(aliceSizes), Counter(bobSizes)
        
        for i in aC:
            if bC[i+differencea]:
                return [i, i+differencea]