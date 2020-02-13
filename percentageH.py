# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:00:11 2020

@author: ASUS
"""

n=int(input())
lst=[]
for i in range(n):
    A=input().split()
    lst.append(A)
B=input()

    
for i in lst:
    if i[0]==B:
        l=i[1:]
        e=list(map(float,i[1:]))
        
avg=sum(e)/len(e)
print ("%.2f" %avg)
        
    
