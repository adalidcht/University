# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 10:43:09 2022

@author: adalc
"""

from scipy.io import wavfile
from winsound import *
from matplotlib import pyplot as plt
import numpy as np
import time


muestreo, datos = wavfile.read('c://..//audio.wav')
datos = datos/(2.**15) #Normalizado
PlaySound(r'grabacion.wav', SND_FILENAME|SND_ASYNC) #Reproducir sonido

plt.figure()
plt.plot(datos)
ventana = np.int(0.02*muestreo) #2% de la señal

dispx = datos - np.mean(datos) #Offset
energia  = []
tiempo = []

#Energía
for i in range(0, len(dispx) - ventana, ventana): #Muestreo del tamaño de ventana
    y = dispx[i:(i + ventana)]  
    energia.append((1/ventana)*np.sum(y**2)) #Energía por ventana
    tiempo.append((i)*(1/muestreo))

ener_sig = energia/np.max(energia) #Normalizado


#cruces por cero
cruce = []
for i in range(0,len(dispx) - ventana,ventana):
    contador = 0
    y = dispx[i:(i + ventana)]
    for j in range(1,ventana,1):
        if(y[j] >= 0 and y[j-1] < 0):
            contador = contador + 1
        elif(y[j] < 0 and y[j-1] >= 0):
            contador = contador + 1
    cruce.append(contador*(1/ventana))
    
patron = np.array([ener_sig,cruce])
            
    


    




