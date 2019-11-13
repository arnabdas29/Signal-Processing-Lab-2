# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 19:42:05 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

xn1 = np.asarray([1,2,2,1])
xn2o = np.asarray([1,2,3])
xn2 = np.asarray([1,2,3,0])
N1 = len(xn1)
N2 = len(xn2)
   
temp = np.copy(xn2)
xn22 = np.copy(temp)

xn3 = []

#to invert
for i in range(1,N2,2):
    xn22[i] = temp[N2-i]
    
n1 = np.linspace(0,N1,N1)
n2 = np.linspace(0,N2,N2)

plt.figure()

"""Circular Convolution"""
for m in range(N1):
    temp = np.roll(xn22,m) # Circular Shift
    
    plt.subplot(2,2,m+1)
    plt.title("x2[m-n] where m = "+str(m))
    plt.ylabel("Amp.")
    plt.xlabel("n")
    plt.stem(n1,temp)
    
    mult = 0
    for n in range(N2):
       mult += np.dot(xn1[n],temp[n])
    xn3.append(mult)

plt.figure()
a =np.linspace(0,N1,N1)
plt.subplot(2,2,1)
plt.title("x1[n]")
plt.ylabel("Amp.")
plt.xlabel("n")
plt.stem(a,xn1)
plt.subplot(2,2,2)
plt.title("x2[n]")
plt.ylabel("Amp.")
plt.xlabel("n")
plt.stem(a,xn2)
plt.subplot(2,2,3)
plt.title("x3[n] - Circular Convolution")
plt.ylabel("Amp.")
plt.xlabel("n")
plt.stem(a,xn3)
plt.show()



"""Linear Convolution"""
N2 = len(xn2o)

l = N1+N2-1
lc = np.zeros(l)
for i in range(0,l,1):
    for j in range(0,i+1,1):
        if j<N1 and i-j<N2:
            lc[i] += xn1[j]*xn2o[i-j]

y = np.convolve(xn1,xn2o)
x = np.linspace(0,l,l)

plt.figure()
plt.subplot(2,1,1)
plt.title("Linear Convolution without builtin func.")
plt.ylabel("Amp.")
plt.xlabel("n")
plt.stem(x,lc)
plt.subplot(2,1,2)
plt.title("Linear Convolution with builtin func.")
plt.ylabel("Amp.")
plt.xlabel("n")
plt.stem(x,y)

"""dft using matrix method"""
r = 0
wn = np.matrix([[0,0,0,0],[1,2,3,4],[1,-1,1,-1],[1,1,-1,-1]],np.complex)
for i in range(4):
    for j in range(4):
        wn[i,j] = np.around(np.exp((-1j*2*np.pi)/N1*i*j))
    r += 1
print("W[n]")
print(wn)

wn_inv = wn**(-1)
print("W-1[n]")
print(wn_inv)
plt.figure()
xn1 = np.transpose(np.matrix(xn1))
xn2 = np.transpose(np.matrix(xn2))

xk1 = wn*xn1
xk2 = wn*xn2
xk3 = np.multiply(xk1,xk2)

x3n = np.matmul(wn_inv,xk3)

plt.subplot(2,2,1)
plt.title("X1[k]")
plt.ylabel("Amp.")
plt.xlabel("K")
plt.stem(a,xk1)
plt.subplot(2,2,2)
plt.title("X2[k]")
plt.ylabel("Amp.")
plt.xlabel("K")
plt.stem(a,xk2)
plt.subplot(2,2,3)
plt.title("X3[k]")
plt.ylabel("Amp.")
plt.xlabel("K")
plt.stem(a,xk3)
plt.subplot(2,2,4)
plt.title("x3[n]- idft of X3[k]")
plt.ylabel("Amp.")
plt.xlabel("n")
plt.stem(a,x3n)

plt.show()
