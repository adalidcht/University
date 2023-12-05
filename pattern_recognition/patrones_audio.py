
"""
Created on Mon Nov  7 10:15:55 2022

@author: Sala1
"""

import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from winsound import *
import time

#-------------------------------------------
muestreo1,cancion = wavfile.read('Senal.wav')
t1 = np.arange(len(cancion))/float(muestreo1)
cancion = cancion/(2.**15)

#PlaySound(r"senal.wav", SND_FILENAME| SND_ASYNC)
#time.sleep(30)

muestreo2,ruido = wavfile.read('Ruido_Lab.wav')
t2 = np.arange(len(ruido))/float(muestreo2)
ruido = ruido/(2.**15)

target = cancion+ruido

TARGET = target*(2.**15)
TARGET = np.array(TARGET, dtype=np.int16)
wavfile.write("mezcla.wav", muestreo1, TARGET)

muestreo3,mezcla = wavfile.read('mezcla.wav')
#PlaySound(r"mezcla.wav", SND_FILENAME| SND_ASYNC)
#time.sleep(30)

#-----------------------------------------
#Valores iiniciales red neuronal
w = [0.5,-0.5,0.25]
b = -0.4

patron = np.zeros((3,1))
alpha = 0.01
salida = np.zeros((len(ruido),1))

for t in range(len(cancion)):
    if (t == 1):
        patron[0] = ruido[t]
    elif (t == 2):
        patron[0] = ruido[t]
        patron[1] = ruido[t - 1]
    else:
        patron[0] = ruido[t]
        patron[1] = ruido[t - 1]
        patron[2] = ruido[t - 2]
    
    a1 = np.dot(w,patron) + b
    e1 = target[t] - a1
    salida[t] = e1
    #Regla delta
    w = w + (2*alpha*e1*patron.T)
    b = b + (2*alpha*e1)

#-----------------------------------------------------
    
salida = salida*(2.**15)
salida = np.array (salida, dtype = np.int16)
wavfile.write("recupera.wav", muestreo1, salida)


plt.figure()
plt.plot(cancion)
plt.figure()
plt.plot(mezcla)
plt.figure()
plt.plot(salida)


#PlaySound(r"recupera.wav", SND_FILENAME| SND_ASYNC)
#time.sleep(30)
