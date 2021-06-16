# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:31:05 2020

@author: user
"""
x=input("輸入查詢學號為:")
st={"123":"Tom DTGD","456":"Cat CSIE","789":"Nana ASIE","321":"Lim DBA","654":"Won FDD"}
if x in st:
    print("學生資料為:"+x,st[x])
else:
    print("無該名學生")