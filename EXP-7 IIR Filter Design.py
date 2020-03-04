# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 08:54:48 2020

@author: cb.en.u4ece18106
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

c = int(input("Type of filter(1-4): "))
N = int(input("Enter N: "))
fs = int(input("Enter fs: "))
if c==1 or c==2:
    fc = int(input("Enter fc: "))    
    wc = (2*np.pi*fc)/fs
    fc1=fc2=wc1=wc2=0
else:
    fc1 = int(input("Enter fc1: "))
    fc2 = int(input("Enter fc2: "))
    wc1 = (2*np.pi*fc1)/fs
    wc2 = (2*np.pi*fc2)/fs
    fc=0;wc=0


def iir(c,N,fs,fc=0,wc=0,fc1=0,fc2=0,wc1=0,wc2=0):
    if c==1:
        b,a = signal.butter(N,wc,btype = 'low',analog=True,output='ba')#Design an Nth order digital or analog Butterworth filter and return the filter coefficients in (B,A) or (Z,P,K) form.
        za,pa,ka = signal.butter(N,wc,btype = 'low',analog=True,output='zpk')
        num,den = signal.zpk2tf(za,pa,ka)
    elif c==2:
        b,a = signal.butter(N,wc,btype = 'high',analog=True,output='ba')#Design an Nth order digital or analog Butterworth filter and return the filter coefficients in (B,A) or (Z,P,K) form.
        za,pa,ka = signal.butter(N,wc,btype = 'high',analog=True,output='zpk')
        num,den = signal.zpk2tf(za,pa,ka)
    elif c==3:
        b,a = signal.butter(N,[wc1,wc2],btype = 'bandpass',analog=True,output='ba')#Design an Nth order digital or analog Butterworth filter and return the filter coefficients in (B,A) or (Z,P,K) form.
        za,pa,ka = signal.butter(N,[wc1,wc2],btype = 'bandpass',analog=True,output='zpk')
        num,den = signal.zpk2tf(za,pa,ka)
    elif c==4:
        b,a = signal.butter(N,[wc1,wc2],btype = 'bandstop',analog=True,output='ba')#Design an Nth order digital or analog Butterworth filter and return the filter coefficients in (B,A) or (Z,P,K) form.
        za,pa,ka = signal.butter(N,[wc1,wc2],btype = 'bandstop',analog=True,output='zpk')
        num,den = signal.zpk2tf(za,pa,ka)
    #Compute frequency response of analog filter.
    w, h = signal.freqs(b,a)#h->frequency response
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude response [dB]')
    plt.grid()
    plt.show()
    
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.set_title('Analog filter frequency response')
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
    
    print("Num: ");print(num)
    print("Den: ");print(den)
    

iir(c,N,fs,fc,wc,fc1,fc2,wc1,wc2)
