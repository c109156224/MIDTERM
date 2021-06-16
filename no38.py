# -*- coding: utf-8 -*-
"""
Created on Mon May 10 01:49:10 2021

@author: user
"""

n=int(input("輸入n,輸出菱形:"))
for i in range(1,n+1,2):
    s=int((n-i)/2)
    print(" "*s,end="")
    print("*"*i)
for j in range(n-2,0,-2):
    t=int((n-j)/2)
    print(" "*t,end="")
    print("*"*j)