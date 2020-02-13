# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:19:55 2020

@author: ASUS
"""
l=[]
string=input()
i,c = input().split()
def mutate_string(string,i,c):
    [l.append(m) for m in string]
    i=int(i)
    l[i]=c
        
        
    return "".join(l)
    
print (mutate_string(string,i,c))