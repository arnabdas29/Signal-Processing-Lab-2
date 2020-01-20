# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

N = 9
a = (N-1)/2
n = np.arange(0,1,0.001)
hdn=[]
for i in range(0,1000,1):
    hdw = lambda w:np.exp(-1j*w*a)*np.exp(1j*w*i)
    temp = scipy.integrate.quad(hdw,-1.2,1.2)
    temp1 = temp[0]/6.28
    hdn.append(temp1)

w = [];hn=[]
for i in range(0,N,1):
    w.append(1)
for i in range(N,len(hdn),1):
    w.append(0)
result = np.multiply(hdn,w)
for i in range(len(result)):
    if result[i]!=0:
        hn.append(result[i])