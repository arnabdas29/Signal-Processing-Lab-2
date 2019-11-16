# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:39:03 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

xn = [1,2,3,4,5,6,7,8,9]
hn = [1,2,3]

m = 3 #length of each subdomain
l = len(hn)
N = m+l-1
n_final = len(xn) + l - 1

if(N<l):
    print("N is smaller than l......exiting")
    exit()
    
# creating subdomains
xn1 = xn[0:m]
xn2 = xn[m:2*m]
xn3 = xn[2*m:3*m]

xn11 = [] ; xn22 = [] ; xn33 = [] ; xn44 = []
for i in range(N-m):
    xn11.append(0)
for i in range(m):
    xn11.append(xn1[i])
    
for j in range(N-m,0,-1):
    xn22.append(xn11[N-j])
for j in range(m):
    xn22.append(xn2[j])
    
for k in range(N-m,0,-1):
    xn33.append(xn22[N-k])
for k in range(m):
    xn33.append(xn3[k])

for a in range(N-m,0,-1):
    xn44.append(xn33[N-a])
for a in range(m):
    xn44.append(0)
    

for i in range(N-l):
    hn.append(0)
    
temp = np.copy(hn)
hn1 = np.copy(temp)

"""Circular Convolution"""
y11 = [] ; y22 = [] ; y33 = [] ; y44 = []
#to invert
for i in range(1,N,1):
    hn1[i] = temp[N-i]
    
n = np.linspace(0,N,N)

for m in range(N):
    temp = np.roll(hn1,m) # Circular Shift
    mult1 = mult2 = mult3 = mult4 = 0
    for n in range(N):
       mult1 += np.dot(xn11[n],temp[n])
       mult2 += np.dot(xn22[n],temp[n])
       mult3 += np.dot(xn33[n],temp[n])
       mult4 += np.dot(xn44[n],temp[n])
    y11.append(mult1);y22.append(mult2);y33.append(mult3);y44.append(mult4)
    
#removing m-1 data points
y1=[];y2=[];y3=[];y4=[]
for i in range(N-(m-1),N,1):
    y1.append(y11[i]);y2.append(y22[i]);y3.append(y33[i]);y4.append(y44[i])
    
y = y1+y2+y3+y4
      
