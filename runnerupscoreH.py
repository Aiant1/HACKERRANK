# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:39:59 2020

@author: ASUS
"""
l=[]
n=int(input())
#for i in range(0,n):
#    n1=int(input())
#    l.append(n1)
#input in single line
l=list(map(int,input().split()))
l.sort()
print ("runnerup :",l[1])
    