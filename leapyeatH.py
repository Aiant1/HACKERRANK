# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:24:24 2020

@author: ASUS
"""

def leap_year(year):
    if ((year%4==0 & year%100!=0) or year%400==0):
        print ("leapyear")
    else:
        print ("not a leapyear")
    
result=leap_year(2400)

    