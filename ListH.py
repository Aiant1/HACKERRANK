# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:00:24 2020

@author: ASUS
"""
l=[5,8,9,7,8]
n=int(input())
for i in range(0,n):
    print (l)

    enter_operation=input().split()

    if enter_operation[0]=="insert":
        l.insert(int(enter_operation[1]),int(enter_operation[2]))
    if enter_operation[0]=="print":
        print (l)
    if enter_operation[0]=="remove":
        if len(l)!=0:
            l.remove(int(enter_operation[1]))
        else:
            print("the list is empty" )
    if enter_operation[0]=="append":
        l.append(int(enter_operation[1]))
    if enter_operation[0]=="sort":
        l.sort()
    if enter_operation[0]=="pop":
        
        l.pop()
    if enter_operation[0]=="reverse":
        l.reverse()
        