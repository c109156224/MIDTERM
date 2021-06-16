# -*- coding: utf-8 -*-
"""
Created on Tue May 11 01:07:01 2021

@author: user
"""

n=(input("輸入一組四位數字為"))
l=[]
for i in n:
    ans=(int(i)+7)%10
    l.append(ans)
print(l[2],l[3],l[0],l[1])