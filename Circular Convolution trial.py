# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:42:05 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

xn1 = np.asarray([2,1,2,1])
xn2 = np.asarray([1,2,3,4])
xn3 = []
N1 = len(xn1)
N2 = len(xn2)

n1 = np.linspace(0,N1,N1)
n2 = np.linspace(0,N2,N2)

"""Circular Convolution"""
for m in range(N1):
    temp = np.roll(xn2,-m) # Circular Shift
    mult = 0
    for n in range(N2):
       mult += np.dot(xn1[n],temp[n])
    xn3.append(mult)

a =np.linspace(0,N1,N1)
plt.subplot(2,2,1)
plt.title("x1[n]")
plt.stem(a,xn1)
plt.subplot(2,2,2)
plt.title("x2[n]")
plt.stem(a,xn2)
plt.subplot(2,2,3)
plt.title("x3[n] - Circular Convolution")
plt.stem(a,xn3)
plt.show()

"""Check"""
dft1 = []
dft2 = []
xk = []
idft = []

for k in range(N1):
    mult = 0
    mult1 = 0
    for n in range(N1):
        exp = np.exp((-1j*2*np.pi*n*k)/N1)
        mult += np.dot(xn1[n],exp)
    dft1.append(mult)
    
for k in range(N2):
    mult = 0
    mult1 = 0
    for n in range(N2):
        exp = np.exp((-1j*2*np.pi*n*k)/N2)
        mult += np.dot(xn2[n],exp)
    dft2.append(mult)

for i in range(N1):
    xk.append(np.dot(dft1[i],dft2[i]))

for n in range(N1):
    mult = 0
    mult1 = 0
    for k in range(N1):
        exp = np.exp((1j*2*np.pi*n*k)/N1)
        mult += np.dot(xk[k],exp)
    idft.append(mult/N1)

plt.subplot(2,2,4)
plt.title("X1[k]*X2[k]")
plt.stem(a,idft)

plt.show()
