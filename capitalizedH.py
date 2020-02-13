# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 23:29:51 2020

@author: ASUS
"""

s=input()

l=[]
def solve(s):


    s1=s.split(" ")
    [l.append(s1[i].capitalize()) for i in range(len(s1))]
    return " ".join(l)
    
        
        
        
        
    
print (solve(s))
#    
#
