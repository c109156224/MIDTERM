# -*- coding: utf-8 -*-
"""
Created on Mon May 10 01:54:02 2021

@author: user
"""
f=1
s=0
x=int(input("搭電梯次數 :"))
for i in range(1,x+1):
    n=int(input("輸入樓層 :"))
    if(n>f):
        s=s+(n-f)*20
    elif(f>n):
        s=s+(f-n)*10
    f=n
print(s,"元")
    
