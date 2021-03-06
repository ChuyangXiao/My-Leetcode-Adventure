# -*- coding: utf-8 -*-
"""821. Shortest Distance to a Character.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AyTlO3Q6GdZU7FgDODYhXa28kw6SQmAC
"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        prev_position = -1
        # set one pointer to first occurence of character c in s
        for next_position, char in enumerate(s):
            if char == c:
                break
        for i, char in enumerate(s):
            if i == next_position:
                result.append(0)
                # update the next and prev position
                prev_position = next_position
                next_position+=1
                while next_position < len(s) and s[next_position] != c:
                    next_position+=1
            else:
                if prev_position == -1:
                    result.append(abs(i-next_position))
                elif next_position == len(s):
                    result.append(abs(i-prev_position))
                else:
                    result.append(min(abs(i-prev_position), abs(i-next_position)))
        return result