# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:13:45 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import scipy.spatial.distance as dist #Distancias 

plt.close('all')


def dtw(matriz_distancia):
    matriz_costos = np.zeros((matriz_distancia.shape[0]+1,matriz_distancia.shape[1]+1))
    for i in range(1,matriz_distancia.shape[0]+1):
        matriz_costos[i,0] = np.inf
    for i in range(1,matriz_distancia.shape[1]+1):
        matriz_costos[0,i] = np.inf
    
    for i in range(matriz_distancia.shape[0]):
        for j in range(matriz_distancia.shape[1]):
            valor = [matriz_costos[i,j],
                     matriz_costos[i,j+1],
                     matriz_costos[i+1,j]]
            pos = np.argmin(valor) #Dónde ocurre el mínimo
            matriz_costos[i+1,j+1] = matriz_distancia[i,j] + valor[pos]
    matriz_costos = matriz_costos[1:,1:]
    
    return matriz_costos

#%%

muestreo1, numero1 = wavfile.read('base.wav')
t1 = np.arange(len(numero1))/float(muestreo1)
numero1 = numero1/(2.0**15) #Normalizado
frecuencia1,tiempo1,espectro1 = signal.spectrogram(numero1[:,0],muestreo1,mode = 'psd',nfft = 1024)#,noverlap = 900, nperseg = 1024)

muestreo2, numero2 = wavfile.read('comparacion1.wav')
t2 = np.arange(len(numero2))/float(muestreo2)
numero2 = numero2/(2.0**15) #Normalizado
frecuencia2,tiempo2,espectro2 = signal.spectrogram(numero2[:,0],muestreo2,mode = 'psd',nfft = 1024)#,noverlap = 900, nperseg = 1024)

fig,ax = plt.subplots(1, 2)
ax[0].pcolormesh(tiempo1,frecuencia1[0:100],espectro1[0:100])
ax[0].set_ylabel('Frecuencia [Hz]')
ax[0].set_xlabel('Tiempo[sec]')
ax[1].pcolormesh(tiempo2,frecuencia2[0:100],espectro2[0:100])
ax[1].set_ylabel('Frecuencia [Hz]')
ax[1].set_xlabel('Tiempo[sec]')

md = dist.cdist(np.log(espectro1.T),np.log(espectro2.T), 'cosine') #Compara las columnas, por eso es .T
distancia = dtw(md)
print('Valor de distancia: {:.4f}'.format(distancia[-1,-1]))










