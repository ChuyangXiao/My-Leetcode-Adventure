# -*- coding: utf-8 -*-
"""3. Longest Substring Without Repeating Characters.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15P8qPaIJCNdLJdeCYuwvR_7zatrhBVjr
"""

class Solution:
    def lengthOfLongestSubstring(self, str: str) -> int:
        # Handle empty input
        if not str:
            return 0
        
        # Define result, start/end pointers, hashmap for seen characters
        length = 1
        start = 0
        end = 0
        seen = {}
        
        # Iterate through string using sliding window technique
        while end < len(str):
            
            # You don't have to do this, but slightly cleaner
            startChar = str[start]
            endChar = str[end]
            
            # If our end character has already been seen...
            if endChar in seen:
                # We should reset our start to the new end (+1), or the new start (if our last seen "end" char is before our current start)
                start = max(start, seen[endChar] + 1)
                
            # We set the length of our longest known substring w/out repeating characters
            length = max(length, end - start + 1)
                
            # We reset the index we've last seen end char at (or add it, if never seen before)
            seen[endChar] = end
                
            # Expand our window
            end += 1
        
        # Return our longest substring w/ no repeating characters
        return length