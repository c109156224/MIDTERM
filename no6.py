# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 15:59:23 2020

@author: user
"""

x=int(input("輸入一數值"))
y=list(str(x))
z=list(str(x))
y.sort()
z.sort(reverse=True)
y="".join(y)
z="".join(z)
y=int(y)
z=int(z)
n=z-y
print(n)



