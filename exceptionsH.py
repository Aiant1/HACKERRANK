# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:50:05 2020

@author: ASUS
"""
n=int(input())


for i in range(n):
    a,b=input().split()

    try:
        print (int(a)//int(b))
    except Exception as e:
        print ("Error Code:",e)
        
    
        
    
    