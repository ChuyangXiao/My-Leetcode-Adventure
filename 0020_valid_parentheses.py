# -*- coding: utf-8 -*-
"""20. Valid Parentheses.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ch29aI6b2TFWKwc3fVFXk6sir2mDNL9V
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mpp = {')': '(', '}': '{', ']': '['}
        # create a list to store the possible 
        stk = []
        for e in s:
            if e in mpp:

                if stk and stk[-1] == mpp[e]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(e)
        
        if(len(stk) > 0):
            return False
        return True
