# -*- coding: utf-8 -*-
"""832. Flipping an Image.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aswEdCCZCQJj7lzrdMNGO7ATgOFZ39Be
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]
            for j in range(len(image[i])):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        return image