# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:02:52 2019

@author: Arnab Das
"""

import numpy as np

xn = [1,2,3,4,5,6,7,8,9]
hn = [1,2,3]

m = len(hn)
l = int(input("Input length of subdomain: "))
N = m+l-1

x1=xn[0:l];x2=xn[l:2*l];x3=xn[2*l:3*l]

#zero padding xn
for i in range(N-len(x1)):
    x1.append(0)
for i in range(N-len(x2)):
    x2.append(0)
for i in range(N-len(x3)):
    x3.append(0)

#zero padding hn    
for j in range(N-m):
    hn.append(0)
    
"""Circular Convolution"""
y1 = [];y2=[];y3=[];y4=[]
temp = np.copy(hn)
hn1 = np.copy(temp)
#to invert
for i in range(1,N,1):
    hn1[i] = temp[N-i]

for m in range(N):
    temp = np.roll(hn1,m) # Circular Shift
    mult1 = mult2 = mult3 = mult4 = 0
    for n in range(N):
       mult1 += np.dot(x1[n],temp[n])
       mult2 += np.dot(x2[n],temp[n])
       mult3 += np.dot(x3[n],temp[n])
    y1.append(mult1)
    y2.append(mult2)
    y3.append(mult3)
