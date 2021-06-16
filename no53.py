# -*- coding: utf-8 -*-
"""
Created on Tue May 11 00:13:54 2021

@author: user
"""

n=float(input("輸入路程公里數 :"))
n=int(n*1000)
ans=0
if(n>1500):
    if((n-1500)%250!=0):
        ans=(75+((n-1500)//250+1)*5)
    print(ans)
elif(n>1500):
    ans=(((n-1500)//250)*5)+75
    print(ans)
else:
    print("75")
    
