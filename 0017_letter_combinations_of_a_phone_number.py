# -*- coding: utf-8 -*-
"""17. Letter Combinations of a Phone Number.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EVr5qp6h1gQ2az5XRmjZRNKV_XjPPOdT
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return ''
        
        set_letters = []
        num={'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}
        
        for i in digits:
            set_letters.append(num[i])
        
        for i in range(1, len(set_letters)):
            new_list = []
            for j in range(len(set_letters[0])):
                for k in range(len(set_letters[i])):
                    new_list.append(set_letters[0][j] + set_letters[i][k])
            set_letters[0] = new_list
            
        return set_letters[0]