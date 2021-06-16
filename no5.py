# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:21:15 2020

@author: user
"""

M=int(input("請輸入階層值M:"))
x=1
i=1
while(x<M):
        i=i+1
        x=x*i
print("超過M為",M,"的最小階層值為:",i)