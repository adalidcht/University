# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 10:21:51 2022

@author: Sala8
"""
#Filtro Adaptativo
import numpy as np
import wave
import matplotlib.pyplot as plt
from scipy.io import wavfile


plt.close('all')
M1,Signal = wavfile.read('Raton3.wav')
T1 = np.arange(len(Signal))/float(M1)



plt.figure()
plt.plot(Signal)
plt.show()
Cancion = Signal/(2.**15)

#Ruido
fs = 800
T = 1.0/6
x = np.linspace(0.1, fs*T,fs) 
y = np.sin(60.0*np.pi*x)


M2, Ruido = wavfile.read("Ruido.wav")
T2 = np.arange(len(Ruido))/float(M2)

plt.figure()
plt.plot(Ruido)
plt.show() 
Cancion = Signal/(2.**15)
Ruido = Ruido/(2.**15)
Target = Cancion + Ruido
print(Target)

plt.figure()
plt.plot(Target)
plt.show()

w = [-0.5, 0.5, 0.3]
b = -0.4
patron = np.zeros((3,1))
salida = np.zeros((len(Ruido),1))
alfa = 0.1

#Entrenamiento
for i in range(len(Ruido)):
    if i==0:
        patron[0] = Ruido[i]
    elif i==1:
         patron[0] = Ruido[i]
         patron[1] = Ruido[i-1] # delay
    else:
         patron[0] = Ruido[i]
         patron[1] = Ruido[i-1] # delay
         patron[2] = Ruido[i-2]
    a = np.dot(w,patron) + b
    e = Target[i] - a
    salida[i] = e
    #Actualizacion
    w = w + (2*alfa*e*patron.T)
    b = b + (2*alfa*e)
SonidoRec = salida*(2.**15)
SonidoRec = np.array(SonidoRec, dtype = np.int16)
wavfile.write("Filtro.wav",M1,SonidoRec)
plt.figure()
plt.plot(SonidoRec)