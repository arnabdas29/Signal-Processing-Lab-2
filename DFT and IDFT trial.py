# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:51:09 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

xn = np.asarray([0,1,2,3])
N = len(xn)
result_dft = []
result_idft = []
a = np.arange(0,N,1)
plt.subplot(3,1,1)
plt.title("Signal")
plt.stem(a,xn)

"""DFT"""
for k in range(N):
    mult = 0
    mult1 = 0
    for n in range(N):
        exp = np.exp((-1j*2*np.pi*n*k)/N)
        mult += np.dot(xn[n],exp)
        mult1 = int(np.abs(mult))
    result_dft.append(mult1)
print(result_dft)

plt.subplot(3,1,2)
plt.title("DFT")
plt.stem(a,result_dft)

xk = result_dft
    
"""IDFT"""
for n in range(N):
    mult = 0
    mult1 = 0
    for k in range(N):
        exp = np.exp((1j*2*np.pi*n*k)/N)
        mult += np.dot(xk[k],exp)
        mult1 = int(np.abs(mult))
    result_idft.append(mult/N)
print(result_idft)
plt.subplot(3,1,3)
plt.title("IDFT")
plt.stem(a,result_idft)

plt.show()
