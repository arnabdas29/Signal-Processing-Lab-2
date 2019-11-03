# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:51:09 2019

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

xn = np.asarray([0,1,2,3])
xk = np.asarray([1,2,3,4])
N = len(xn)
result_dft = []
result_idft = []

"""DFT"""
for k in range(N):
    mult = 0
    for n in range(N):
        exp = np.exp((-1j*2*np.pi*n*k)/N)
        mult += xn[n]*exp
    result_dft.append(mult)
print(result_dft)
    
"""IDFT"""
for n in range(N):
    mult = 0
    for k in range(N):
        exp = np.exp((1j*2*np.pi*n*k)/N)
        mult += xk[n]*exp
    result_idft.append(mult/N)
print(result_idft)