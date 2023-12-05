# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:38:13 2022

@author: adalc
"""

import numpy as np
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier

 

plt.close('all')

 

file='Raton3.wav'
fs, data=waves.read(file)
audio=data[:,0]

 

#Señal en el dominio del tiempo
L=len(audio)
t=np.arange(0,L)/fs
plt.figure(0)
plt.plot(t,audio)
plt.title('Dominio del tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')

 

#Señal en el dominio de la frecuencia
T=1/fs
spec=np.abs(fourier.fft(audio))[:L//2]
freq=fourier.rfftfreq(L//2,T)[:L//2]
plt.figure(1)
plt.plot(freq, spec)
plt.title('Dominio de la frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')