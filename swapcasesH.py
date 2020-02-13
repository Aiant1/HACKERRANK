# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:01:22 2020

@author: ASUS
"""
string=input()
def swap(strn):
    s=""

    for i in strn:
        if i.isupper()==True:
            s=s+i.lower()
            
        else:
            
            s=s+i.upper()
    return s

     
            
print (swap(string))
        

