# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 20:18:35 2019

@author: Arnab Das
"""

import numpy as np

x1n = [1,2,3,4]
x2n = [5,6,7,8]

xn = x1n + np.multiply(1j,x2n)
print("xn: "+str(xn))

"""DFT """
N = len(xn)
dft = []
for k in range(N):
    mult = 0
    mult1 = 0
    for n in range(N):
        exp = np.exp((-1j*2*np.pi*n*k)/N)
        mult += np.dot(xn[n],exp)
    dft.append(np.around(mult))
print("Xk: "+str(dft))
    
"""X*(N-k)"""
result_dft = []
result_dft.append(np.conjugate(dft[0]))
for i in range(1,N,1):
    result_dft.append(np.conjugate(dft[N-i]))
print("X*[N-K]: "+str(result_dft))
    
"""X1k ans X2k"""
a = np.add(dft,result_dft)
sum1 = np.multiply(a,0.5)
b = np.subtract(result_dft,dft)
sum2 = np.multiply(b,0.5j)

print("X1k: "+str(sum1))
print("X2k: "+str(sum2))