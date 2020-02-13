# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:36:27 2020

@author: ASUS
"""

import numpy as np
N, M = map(int, input().split())
A = np.array([list(map(int, input().split()))])
B = np.array([list(map(int, input().split()))])
print(np.add(A,B)), 
print(np.subtract(A,B)) 
print(np.multiply(A,B,)) 
print (np.floor_divide(A,B)) 
print (np.mod(A,B))
print (np.power(A,B))





