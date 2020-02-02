import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack as ft


def butterfly(a,b,i,l=8):
    s = np.zeros(2)
    s = np.complex128(s)
    w = np.exp(-1*(2/l)*1j*np.pi*i)
    s[0] = a+(b*w)
    s[1] = a-(b*w)
    return s

def binrev(n,lb):
    t = bin(n)
    p = []
    for i in range(2,len(t),1):
        p.append(t[i])
    for i in range(0,lb-len(p),1):
        p.insert(0,0)
    m = 0
    for i in range(0,len(p),1):
        m = (10*m)+int(p[len(p)-1-i])
    m = str(m)
    return(int(m,2))

x = [1,-1,-1,-1,1,1,1,-1]
l = len(x)
l1 = int(l/2)
l2 = int(l/4)
v = np.zeros((l1,2))
v = np.complex128(v)
f = np.zeros((l2,4))
f = np.complex128(f)
lb = len(bin(l-1))-2

xbin = np.zeros(len(x))
for i in range(0,l,1):
    j = binrev(i,lb)
    xbin[j] = x[i]

count = 0
flag = 0
"""2 point dft"""
for i in range(0,l1,1):
    k = butterfly(xbin[count],xbin[count+1],flag*i)
    count+=2
    v[i][0] = k[0]
    v[i][1] = k[1]

flag+=2
count = 0
"""4 point dft"""
for i in range(0,l2,1):
    for j in range(0,int(l/l1),1):
        k = butterfly(v[count][j],v[count+1][j],flag*j)
        f[i][j] = k[0]
        f[i][j+int(l/l1)] = k[1]
    count+=int(l/l1)

xk = np.zeros(l)
xk = np.complex128(x)
count = 0
for i in range(0,int(l/l2),1):
    k = butterfly(f[count][i],f[count+1][i],i)
    xk[i] = k[0]
    xk[i+int(l/l2)] = k[1]
xk = np.around(xk)

xk2 = ft.fft(x)
xk2 = np.around(xk2)

""" xk and xk2 are thr outputs
where xk is without builtin function
and xk2 is with builtin function"""
