# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:25:04 2019

@author: Arnab Das
"""

import numpy as np

x = [1,2,3,4,5,6,7,8]
xe = [];xo = []

for i in range(0,len(x),2):
    xe.append(x[i]) 
    xo.append(x[i+1])
    
xn = xe + np.multiply(1j,xo)

"""DFT """
N = len(xn)
dft = []
for k in range(N):
    mult = 0
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

x1k = sum1;x2k = sum2
x1k = np.complex128(x1k) ; x2k = np.complex128(x2k)

print("X1k: "+str(sum1))
print("X2k: "+str(sum2))

"""to find G[k]"""
gk = np.complex128(np.zeros(2*N))
for i in range(N):
    wn = np.exp(-1j*2*np.pi*i/(2*N))
    gk[i] = np.around(x1k[i]+wn*x2k[i])
    gk[i+N] = np.around(x1k[i]-wn*x2k[i])
        
print("G[k]: " +str(gk))