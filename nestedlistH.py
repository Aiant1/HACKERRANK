# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:57:40 2020

@author: ASUS
"""
l=[]
l2=[]
n=int(input())
#for i in range(0,n):
#    
#    name=input()
#    score=float(input())
#    l.append([name,score])
l=[[input(),float(input())] for i in range(0,n)]
second= sorted(list(set([marks for name, marks in l])))[1]

for a,b in l:
    if b==second:
        print (a)
    
