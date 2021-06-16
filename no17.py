# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:02:09 2020

@author: user
"""
L=[]
for i in range(5):
  x=input("分別輸入五張撲克牌")
  if( x=="A"):
    x=1
  elif (x=="J"):
    x=11
  elif (x=="Q"):
    x=12
  elif (x=="K"):
    x=13
  L.append(int(x))
print("總合為",sum(L))