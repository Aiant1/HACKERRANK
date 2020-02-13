# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:07:16 2020

@author: ASUS
"""

a1="abcdecd"
b1="cd"
count=0
for i in range(len(a1)):
    if a1[i:i+len(b1)] == b1:
        count=count+1