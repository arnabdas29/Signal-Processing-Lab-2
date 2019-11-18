# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 08:50:44 2019

@author: cb.en.u4ece18106
"""
"""for L = 5"""

import numpy as np
import matplotlib.pyplot as plt

xn = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
a = np.arange(0,4,1)
hn=np.zeros(4)
ind1 = np.where(a==0)
hn[ind1] = 1
ind2 = np.where(a==2)
hn[ind2] = -1*2
ind3 = np.where(a==3)
hn[ind3] = 3
hn = list(hn)

m = len(hn)
l = 5
N = l+m-1

if(N<l):
    print("N is smaller than l......exiting")
    exit()
    
# creating subdomains
xn1=[];xn2=[];xn3=[];xn4=[];xn5 = []

#zero padding hn    
for j in range(N-m):
    hn.append(0)
    
#xn1
for i in range(m-1):
    xn1.append(0)
try:
    for i in range(N-(m-1)):
        xn1.append(xn[i])
except:
    for i in range(N-len(xn1)):
        xn1.append(0)

#xn2
for i in range(m-1):
    xn2.append(xn1[N-(m-1)+i])
try:
    for i in range(N-(m-1)):
        xn2.append(xn[N-(m-1)+i+0*l])
except:
    for i in range(N-len(xn2)):
        xn2.append(0)
    
#xn3
for i in range(m-1):
    xn3.append(xn2[N-(m-1)+i])
try:
    for i in range(N-(m-1)):
        xn3.append(xn[N-(m-1)+1*l+i]) 
except:
    for i in range(N-len(xn3)):
        xn3.append(0)
    
#xn4
for i in range(m-1):
    xn4.append(xn3[N-(m-1)+i])
try:
    for i in range(N-(m-1)):
        xn4.append(xn[N-(m-1)+2*l+i]) 
except:
    for i in range(N-len(xn3)):
        xn4.append(0)

#xn5
for i in range(m-1):
    xn5.append(xn4[N-(m-1)+i])
for i in range(N-(m-1)):
    xn5.append(0) 
    
    
"""Circular Convolution"""
y11 = [];y22=[];y33=[];y44=[];y55=[]
temp = np.copy(hn)
hn1 = np.copy(temp)
#to invert
for i in range(1,N,1):
    hn1[i] = temp[N-i]

for m in range(N):
    temp = np.roll(hn1,m) # Circular Shift
    mult1 = mult2 = mult3 = mult4 = mult5=0
    for n in range(N):
       mult1 += np.dot(xn1[n],temp[n])
       mult2 += np.dot(xn2[n],temp[n])
       mult3 += np.dot(xn3[n],temp[n])
       mult4 += np.dot(xn4[n],temp[n])
       mult5 += np.dot(xn5[n],temp[n])
    
    y11.append(mult1)
    y22.append(mult2)
    y33.append(mult3)
    y44.append(mult4)
    y55.append(mult5)

y1 = y11[(m-(l-1)):]; y2 = y22[(m-(l-1)):]; y3 = y33[(m-(l-1)):]; y4 = y44[(m-(l-1)):];y5 = y55[(m-(l-1)):]
y = y1+y2+y3+y4+y5

"""plotting"""
plt.figure()
plt.subplot(2,1,1)
plt.title("xn")
plt.stem(xn)

plt.subplot(2,1,2)
plt.title("hn")
plt.stem(hn)

plt.figure()
plt.subplot(2,3,1)
plt.title("xn1")
plt.stem(xn1)
plt.subplot(2,3,2)
plt.title("xn2")
plt.stem(xn2)
plt.subplot(2,3,3)
plt.title("xn3")
plt.stem(xn3)
plt.subplot(2,3,4)
plt.title("xn4")
plt.stem(xn4)
plt.subplot(2,3,5)
plt.title("xn5")
plt.stem(xn5)

plt.figure()
plt.subplot(2,3,1)
plt.title("yn1")
plt.stem(y11)
plt.subplot(2,3,2)
plt.title("yn2")
plt.stem(y22)
plt.subplot(2,3,3)
plt.title("yn3")
plt.stem(y33)
plt.subplot(2,3,4)
plt.title("yn4")
plt.stem(y44)
plt.subplot(2,3,5)
plt.title("yn5")
plt.stem(y55)

plt.figure()
plt.title("yn")
plt.stem(y)

plt.show()
