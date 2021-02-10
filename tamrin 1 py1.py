# -*- coding: utf-8 -*-
"""

@author: 1256
"""
mySentence = input("Enter a Sentence : ")
str2 = ""

for i in range(len(mySentence)):
    if(i % 2 == 0):
        str2 = str2 + mySentence[i]
print("Original String :  ", mySentence)
print("Final String :     ", str2)
