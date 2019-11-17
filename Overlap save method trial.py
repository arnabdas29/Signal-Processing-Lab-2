# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 12:24:13 2019

@author: Arnab Das
"""

import numpy as np

xn = [1,2,3,4,5,6,7,8,9]
hn = [1,2,3]

m = len(hn)
l = 4
N = m+l-1

if(N<l):
    print("N is smaller than l......exiting")
    exit()
    
# creating subdomains
xn1=[];xn2=[];xn3=[];xn4=[]

#zero padding hn    
for j in range(N-m):
    hn.append(0)
    
    
for i in range(m-1):
    xn1.append(0)
try:
    for i in range(N-(m-1)):
        xn1.append(xn[i])
except:
    for i in range(N-len(xn1)):
        xn1.append(0)
    
for i in range(m-1):
    xn2.append(xn1[N-(m-1)+i])
try:
    for i in range(N-(m-1)):
        xn2.append(xn[N-(m-1)+i+0*l])
except:
    for i in range(N-len(xn2)):
        xn2.append(0)
    
for i in range(m-1):
    xn3.append(xn2[N-(m-1)+i])
try:
    for i in range(N-(m-1)):
        xn3.append(xn[N-(m-1)+1*l+i]) 
except:
    for i in range(N-len(xn3)):
        xn3.append(0)
    
for i in range(m-1):
    xn4.append(xn3[N-(m-1)+i])
for i in range(N-(m-1)):
    xn4.append(0) 

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
       mult1 += np.dot(xn1[n],temp[n])
       mult2 += np.dot(xn2[n],temp[n])
       mult3 += np.dot(xn3[n],temp[n])
       mult4 += np.dot(xn4[n],temp[n])
    y1.append(mult1)
    y2.append(mult2)
    y3.append(mult3)
    y4.append(mult4)

y1 = y1[(m-(l-1)):]; y2 = y2[(m-(l-1)):]; y3 = y3[(m-(l-1)):]; y4 = y4[(m-(l-1)):]
y = y1+y2+y3+y4
