# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy.integrate

def fil_coeff(hdn,wn):
    h = []
    result = np.multiply(hdn,wn)
    for i in range(len(result)):
        if result[i]!=0:
            h.append(result[i])
    return h
    
    
   
def filter_type(c1,N,a):
    hdn = []
    if c1 == 1:
        print("\n...LPF filter designing...")
        wc = float(input("Enter cutoff Freq.: "))
        for n in range(0,1000,1):
            hdw = lambda w:np.exp(-1j*w*a)*np.exp(1j*w*n)
            temp = scipy.integrate.quad(hdw,-wc,wc)
            temp1 = temp[0]/6.28
            hdn.append(temp1)
    elif c1 == 2:
        print("\n...HPF filter designing...")
        wc = float(input("Enter cutoff Freq.: "))
        for n in range(0,1000,1):
            hdw = lambda w:np.exp(-1j*w*a)*np.exp(1j*w*n)
            temp = scipy.integrate.quad(hdw,-3.14,-wc) + scipy.integrate.quad(hdw,wc,3.14)
            temp1 = temp[0]/6.28
            hdn.append(temp1)
    elif c1 == 3:
        print("\n...BPF filter designing...")
        wc1 = float(input("Enter cutoff Freq 1.: "));wc2 = float(input("Enter cutoff Freq2.: "))
        for n in range(0,1000,1):
            hdw = lambda w:np.exp(-1j*w*a)*np.exp(1j*w*n)
            temp = scipy.integrate.quad(hdw,-wc2,-wc1) + scipy.integrate.quad(hdw,wc1,wc2)
            temp1 = temp[0]/6.28
            hdn.append(temp1)
    elif c1 == 4:
        print("\n...BSP filter designing...")
        wc1 = float(input("Enter cutoff Freq 1.: "));wc2 = float(input("Enter cutoff Freq2.: "))
        for n in range(0,1000,1):
            hdw = lambda w:np.exp(-1j*w*a)*np.exp(1j*w*n)
            temp = scipy.integrate.quad(hdw,-3.14,-wc2) + scipy.integrate.quad(hdw,-wc1,wc1) + scipy.integrate.quad(hdw,wc2,3.14)
            temp1 = temp[0]/6.28
            hdn.append(temp1)
    
    return hdn

def window_type(c2,N,a,hdn):
    w = [];hn=[]
    if c2 == 1:
        print("\n...Creating a REACTANGULAR window...")
        for i in range(0,N,1):
            w.append(1)
        
        
    if c2 == 2:
        print("\n...Creating a HANNING window...")
        for n in range(0,N,1):
            func = 0.5 - 0.5*np.cos((2*np.pi*n)/(N-1))
            w.append(func)
    if c2 == 3:
        print("\n...Creating a HAMMING window...")
        for n in range(0,N,1):
            func = 0.54 - 0.46*np.cos((2*np.pi*n)/(N-1))
            w.append(func)
    for i in range(N,len(hdn),1):
            w.append(0)
    hn = fil_coeff(hdn,w)
    return hn
        
        
#choices
N = int(input("Enter N: "))
a = (N-1)/2
c1 = int(input("Enter type of filter(1-4): "))
c2 = int(input("Enter type of window(1-3): "))
fil_type = filter_type(c1,N,a)
win_result = window_type(c2,N,a,fil_type)
print("\nThe filter coefficients are: ")
print(win_result)
