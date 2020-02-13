# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:41:19 2020

@author: ASUS
"""

strn=input()
def split_join(strn):
    strn1=strn.split(" ")
    return "_".join(strn1)
print (split_join(strn))
    