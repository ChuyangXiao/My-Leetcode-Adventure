# -*- coding: utf-8 -*-
"""2160. Minimum Sum of Four Digit Number After Splitting Digits.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XfMopE9re12xQD6zvc1pQ-90PJ6r0yZQ
"""

class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num),reverse=True)
        return int(num[0]) + int(num[1]) + int(num[2])*10 + int(num[3])*10