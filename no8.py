# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 02:08:17 2020

@author: user
"""

x=input("輸入第一行正整數為:")
a=input("第二行中數列中的數字為:").split(" ")
l=[]
for i in range(0,int(x)):
    c=a.count(a[i])
    l.append(c)
if max(l)==1:
    print("每個數字剛好出現一次")
else:
    b=max(l)
    g = l.index(2)
    f = l.index(3)
    print("次數為2"+str(g))
    print("次數為3"+str(f))
    
    print("最大出現次數的數字為:"+str(a[l.index(b)])+"\n"+"出現次數:"+str(b))
    
