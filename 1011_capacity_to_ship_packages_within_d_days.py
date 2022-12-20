# -*- coding: utf-8 -*-
"""1011. Capacity To Ship Packages Within D Days.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M_pLZipMykKWmwQUMYXvBJn4Y0bU2rDM
"""

class Solution:
    def shipWithinDays(self, a: List[int], d: int) -> int:
        lo, hi = max(a), sum(a)   
        while lo < hi:
            mid = (lo + hi) // 2
            tot, res = 0, 1
            for wt in a:
                if tot + wt > mid:
                    res += 1
                    tot = wt
                else:
                    tot += wt
            if res <= d:
                hi = mid
            else:
                lo = mid+1
        return lo