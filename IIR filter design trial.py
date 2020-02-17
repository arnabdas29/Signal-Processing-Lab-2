# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:03:03 2020

@author: Arnab Das
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

wp=40
ws = 100
fs=1000
N,wn = signal.buttord(wp,ws,3,40,analog=True)#Return the order of the lowest order digital or analog Butterworth filter that loses no more than gpass dB in the passband and has at least gstop dB attenuation in the stopband.
b,a = signal.butter(N,wn,btype = 'low',analog=True,output='ba')#Design an Nth order digital or analog Butterworth filter and return the filter coefficients in (B,A) or (Z,P,K) form.
za,pa,ka = signal.butter(N,wn,btype = 'low',analog=True,output='zpk')

#digital transfer function
b1,a1 = signal.bilinear(b, a, fs)#Return a digital IIR filter from an analog one using a bilinear transform.
z2,p2,k2 = signal.bilinear_zpk(za, pa, ka, fs)#Return a digital IIR filter from an analog one using a bilinear transform.

#Compute frequency response of analog filter.
w, h = signal.freqs_zpk(za, pa, ka, worN=np.logspace(0, 2, 1000))#h->frequency response
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.xlabel('Frequency')
plt.ylabel('Amplitude response [dB]')
plt.grid()
plt.show()

#Compute frequency response of digital filter.
zd, pd, kd = signal.butter(N, wn/fs, output='zpk')
w, h = signal.freqz_zpk(zd, pd ,kd , fs=1000)
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('Digital filter frequency response')
ax1.plot(w, 20 * np.log10(abs(h)), 'b')
ax1.set_ylabel('Amplitude [dB]', color='b')
ax1.set_xlabel('Frequency [Hz]')
ax1.grid()
ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
ax2.plot(w, angles, 'g')
ax2.set_ylabel('Angle [radians]', color='g')
plt.axis('tight')
plt.show()

#to plot the poles and zeros in z-plane
plt.figure()
plt.plot(np.real(za), np.imag(za), 'xb')
plt.plot(np.real(pa), np.imag(pa), 'or')
plt.legend(['Zeros', 'Poles'], loc=2)
plt.title('Pole / Zero Plot')
plt.ylabel('Real')
plt.xlabel('Imaginary')
plt.grid()
plt.show()