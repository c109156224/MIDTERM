# -*- coding: utf-8 -*-
"""
Created on Mon May 10 23:47:53 2021

@author: user
"""
a=int(input("輸入a :"))
b=int(input("輸入b :"))
c=int(input("輸入c :"))
ans=(-b+((b**2-4*a*c)**0.5))/(2*a)
ans1=(-b-((b**2-4*a*c)**0.5))/(2*a)
if(b**2-4*a*c<0):
    print("無解")
elif(ans==ans1):
    print(ans)
elif(ans!=ans1):
    print(ans,ans1)

