# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:21:00 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
from scipy.fft import fftshift

rng  = np.random.default_rng()
plt.close('all')

muestreo1, numero1 = wavfile.read('uno1.wav')
t1 = np.arange(len(numero1))/float(muestreo1)
numero1 = numero1/(2.0**15) #Normalizado
frecuencia1,tiempo1,espectro1 = signal.spectrogram(numero1[:,0],muestreo1,mode = 'psd',nfft = 1024,noverlap = 900, nperseg = 1024)
#espectro = mode = 'psd' (densidad espectral), 'magnitud', 'phase'
#nfft puntos de fft

#plt.figure(0)
#plt.pcolormesh(tiempo1,frecuencia1[0:100],espectro1[0:100])
#plt.ylabel('Frecuencia [Hz]')
#plt.xlabel('Tiempo[sec]')
#plt.show()

#---------------------------------------

muestreo2, numero2 = wavfile.read('uno2.wav')
t1 = np.arange(len(numero2))/float(muestreo2)
numero1 = numero1/(2.0**15) #Normalizado
frecuencia2,tiempo2,espectro2 = signal.spectrogram(numero2[:,0],muestreo2,mode = 'psd',nfft = 1024,noverlap = 900, nperseg = 1024)


#plt.figure(1)
#plt.pcolormesh(tiempo2,frecuencia2[0:100],espectro2[0:100])
#plt.ylabel('Frecuencia [Hz]')
#plt.xlabel('Tiempo[sec]')
#plt.show()

fig,ax = plt.subplots(1, 2)
ax[0].pcolormesh(tiempo1,frecuencia1[0:100],espectro1[0:100])
ax[0].set_ylabel('Frecuencia [Hz]')
ax[0].set_xlabel('Tiempo[sec]')
ax[1].pcolormesh(tiempo2,frecuencia2[0:100],espectro2[0:100])
ax[1].set_ylabel('Frecuencia [Hz]')
ax[1].set_xlabel('Tiempo[sec]')


plt.show()


