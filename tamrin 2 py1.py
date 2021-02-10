# -*- coding: utf-8 -*-
"""

@author: 1256
"""
t = 4

  
def transpose(A,B): 
  
    for i in range(t): 
        for j in range(t): 
            B[i][j] = A[j][i] 
 
e = [ [4, 7, 3, 0], 
    [3, 0, 0, 1], 
    [5, 8, 10, 2], 
    [4, 10, 8, 3]] 
   
   
r = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]  
  
transpose(e, r) 
   
print("Result matrix is") 
for i in range(t): 
    for j in range(t): 
        print(r[i][j], " ", end='') 
    print() 



