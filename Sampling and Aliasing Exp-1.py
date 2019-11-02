# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt

"""generating x1"""
f1 = 5
t = np.arange(0,1,0.01)
x = np.sin(2*np.pi*f1*t)
plt.subplot(2,2,1)
plt.title("Analog signal to be discretised 5Hz")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.plot(t,x)

#fs3 = 20
fs3 = 20
n3 = np.arange(0,fs3,1)
x3 = np.sin(2*np.pi*(f1/fs3)*n3)
plt.subplot(2,2,2)
plt.title("Signal sampled @ 20Hz")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n3,x3)

#fs2 = 12
fs2 = 12
n2 = np.arange(0,fs2,1)
x2 = np.sin(2*np.pi*(f1/fs2)*n2)
plt.subplot(2,2,3)
plt.title("Signal sampled @ 12Hz")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n2,x2)

#fs1 = 8
fs1 = 8
n1 = np.arange(0,fs1,1)
x1 = np.sin(2*np.pi*(f1/fs1)*n1)
plt.subplot(2,2,4)
plt.title("Signal sampled @ 8Hz")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n1,x1)

"""fft"""
#fs1
y1 = np.fft.fft(x1)
y11 = np.abs(y1)
k1 = np.linspace(0,fs1,fs1)
plt.figure()
plt.subplot(3,1,1)
plt.title("Magnitude plot of Sampled signal @8Hz")
plt.xlabel("k")
plt.ylabel("Amplitude")
plt.stem(k1,y11)

#fs2
y2 = np.fft.fft(x2,fs2)
y22 = np.abs(y2)
k2 = np.linspace(0,fs2,fs2)
plt.subplot(3,1,2)
plt.title("Magnitude plot of Sampled signal @12Hz")
plt.xlabel("k")
plt.ylabel("Amplitude")
plt.stem(k2,y22)

#fs3
y3 = np.fft.fft(x3,fs3)
y33 = np.abs(y3)
k3 = np.linspace(0,fs3,fs3)
plt.subplot(3,1,3)
plt.title("Magnitude plot of Sampled signal @20Hz")
plt.xlabel("k")
plt.ylabel("Amplitude")
plt.stem(k3,y33)


"""ifft"""
plt.figure()
b1 = np.fft.ifft(y1)
plt.subplot(3,1,1)
plt.title("ifft of mag plot of 8Hz samples signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n1,b1)

b2 = np.fft.ifft(y2)
plt.subplot(3,1,2)
plt.title("ifft of mag plot of 12Hz samples signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n2,b2)

b3 = np.fft.ifft(y3)
plt.subplot(3,1,3)
plt.title("ifft of mag plot of 20Hz samples signal")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n3,b3)

"""Aliasing effect"""
f1 = 5
f2 = 17
fs = 12
plt.figure()
t = np.arange(0,1,0.01)
x1 = np.sin(2*np.pi*f1*t)
n = np.arange(0,fs,1)
x11 = np.sin(2*np.pi*(f1/fs)*n)
plt.subplot(3,1,1)
plt.title("Signal 5Hz sampled @12Hz")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n,x11)

f2 = 17
x2 = np.sin(2*np.pi*f2*t)
x22 = np.sin(2*np.pi*(f2/fs)*n)
plt.subplot(3,1,2)
plt.title("Signal 17Hz sampled @12Hz")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n,x22)

f3 = 29
x3 = np.sin(2*np.pi*f3*t)
x33 = np.sin(2*np.pi*(f3/fs)*n)
plt.subplot(3,1,3)
plt.title("Signal 29Hz sampled @12Hz")
plt.xlabel("n")
plt.ylabel("Amplitude")
plt.stem(n,x33)
