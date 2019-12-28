# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 14:57:44 2019

@author: Arnab Das
"""

"""
a -> centre of symmetry
c1 -> filter type
c2 -> window type
c3 -> mag respomse of linear phase FIR filter
"""

import numpy as np

def window(c2,N):
    n = np.linspace(0,N,N)
    if c2 == 1:
        print("Rectangular Window")
        w = np.zeros(N)
        ind = np.where(n>=0)
        w[ind] = 1
    elif c2 == 2:
        print("Hanning Window")
        w = 0.5 - 0.5*np.cos((2*np.pi*n)/N)
    elif c2 == 3:
        print("Hamming Window")
        w = 0.54 - 0.46*np.cos((2*np.pi*n)/N)
    else:
        print("Error 404!...Wrong Window Option!")
        quit()
    return w

def mag_res(c3,N,hn):
    Hw = []
    if c3 == 1:
        print("hn -> sym. N-> odd")
        for w in range(0,2*np.pi,1):
            temp1 = hn((N-1)/2)
            for n in range(1,(N-1)/2,1):
                temp2 = 2*hn(((N-1)/2)-n)*np.cos(w*n)
            Hw.append(np.add(temp1,temp2))
    elif c3 == 2:
        print("hn->sym. N->even")
        for w in range(0,2*np.pi,1):
            for n in range(1,N/2,1):
                temp = 2*hn(0.5*N-n)*np.cos((n-0.5)*w)
            Hw.append(temp)
    elif c3 == 3:
        print("hn-> antisym. N->odd")
        for w in range(0,2*np.pi,1):
            for n in range(1,N/2,1):
                temp = 2*hn(((N-1)/2)-n)*np.sin(w*n)
            Hw.append(temp)
    elif c3 == 4:
        print("hn->antisym. N->even")
        for w in range(0,2*np.pi,1):
            for i in range(1,N/2,1):
                temp = 2*hn((N/2)-n)*np.sin(w*(n-0.5))
            Hw.append(temp)
    else:
        print("Error 404!...Wrong Mag_res Option!")
        quit()
    return Hw       
            
                

def filter_type(c1,wl,wr,a,N):
    if c1 == 1:
        print("Designing a LPF")


"""Input"""
N = int(input("Enter N: "))
c1 = int(input("Enter filter type(1-3): "))
c2 = int(input("Enter window type(1-3): "))
c3 = int(input("Enter mag_res type(1-4): "))
a = (N-1)/2   #centre of symmetry

filter_type(c1,wl,wr,a,N)
window(c2,N)
mag_res(c3,N,hn)