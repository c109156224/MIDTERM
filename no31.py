# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:27:24 2020

@author: user
"""
chi=int(input("國文:"))
eng=int(input("英文:"))
mat=int(input("微積分:"))
tee=int(input("體育:"))
pyt=int(input("程式設計:"))
z=(chi+eng+mat+tee+pyt)/5
l={"國文":chi,"英文":eng,"微積分":mat,"體育":tee,"程式設計":pyt}
m=min(l,key=l.get)
x=max(l,key=l.get)
print("平均分數:",round(z,2))
print("最高分科目:",x,l[x],"分")
print("最低分科目:",m,l[m],"分")

