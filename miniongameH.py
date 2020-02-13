## -*- coding: utf-8 -*-
#"""
#Created on Thu Feb 13 18:34:37 2020
#
#@author: ASUS
#"""
#
#vowel=["a","e","i","o","u"]
#s=input()
#kelvin=0
#stuart=0
#
#for i in range(len(s)):
#    if s[i] in vowel:
#        kelvin=kelvin+(len(s)-i)
#    else:
#        stuart=stuart+(len(s)-i)
#if kelvin>stuart:
#    print ("Kelvin "+ str(kelvin))
#elif kelvin<stuart:
#    print ("Stuart "+ str(Stuart))
#else:
#    print ("draw")
vowel=["a","e","i","o","u"]
def minion_game(s):

    # your code goes here
  
    kelvin=0
    stuart=0
    s=s.lower()
    for i in range(len(s)):
        if s[i] in vowel:
            kelvin=kelvin+(len(s)-i)
        else:
            stuart=stuart+(len(s)-i)
    if kelvin>stuart:
        print ("Kelvin "+ str(kelvin))
    elif kelvin<stuart:
        print ("Stuart "+ str(stuart))
    else:
        print ("draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    
    

        
        
        
