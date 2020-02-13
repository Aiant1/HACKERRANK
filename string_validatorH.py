# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:44:25 2020

@author: ASUS
"""

"""Python has built-in string validation methods for basic data. 
It can check if a string is composed of alphabetical characters,
alphanumeric characters, digits, etc
"""
s=input()
for fn in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
    print(any(fn(c) for c in s))

        
        