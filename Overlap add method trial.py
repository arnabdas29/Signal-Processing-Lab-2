# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:54:17 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

xn = [1,2,3,4,5,6,7,8,9]
hn = [1,2,3]

m = 3  #length of each subdomain
l = len(hn)
N = m+l-1

if(N<l):
    print("N is smaller than l......exiting")
    exit()
# creating subdomains
xn1 = xn[0:m]
xn2 = xn[m:2*m]
xn3 = xn[2*m:3*m]

a = N-m ; z = 0    #zero padding for xn
b = N-l ; z = 0    #zero padding for xn
for i in range(a):
    xn1.append(z)
    xn2.append(z)
    xn3.append(z)
for j in range(b):
    hn.append(z)

"""Circular convolution""" 
y1 = [];y2 = [];y3 = []; y = []
n1 = np.linspace(0,N,N)

temp = np.copy(hn)
hn1 = np.copy(temp)
for i in range(1,N,1):
    hn1[i] = temp[N-i]

for m1 in range(N):
    temp = np.roll(hn1,m1) # Circular Shift 
    mult1 = 0
    mult2 = 0
    mult3 = 0
    for n in range(N):
       mult1 += np.dot(xn1[n],temp[n])
       mult2 += np.dot(xn2[n],temp[n])
       mult3 += np.dot(xn3[n],temp[n])
    y1.append(mult1)
    y2.append(mult2)
    y3.append(mult3)
