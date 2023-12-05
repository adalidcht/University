# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 23:28:32 2022

@author: adalc
"""

import winsound #audio de windows
import pyaudio #librería para reproducción o edición de audio 
import wave #librería para manipular archivos WAV
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from numpy import arange,sin,pi

plt.close('all')

#Grabación
muestras = 512 # 512 muestras
formato = pyaudio.paInt16 # Resolucion de 16 bits
channels = 2 #Stereo
fs = 8000 #Frecuencia de muestreo 8000/s
seconds = 2 #Tiempo de grabacion
filename = 'martes_ra.wav' # Nombre del archivo

audio_obj = pyaudio.PyAudio() #objeto

input('Presionar Enter')
print('La grabación ha iniciado')

#Graba el audio
stream = audio_obj.open(format = formato,channels = channels,rate = fs,frames_per_buffer = muestras,input = True)

tramas = [] 
sonido = [] #Se lee del buffer los valores numericos

for i in range(0,int(fs/muestras*seconds)):
    datos = stream.read(muestras) #Lee muestras del stream
    tramas.append(datos)
    sonido.append(np.frombuffer(datos,dtype = np.int16))

#Detiene y cierra la grabación
stream.stop_stream()
stream.close()
audio_obj.terminate() #terminar el objeto de audio
print('La grabación ha terminado')


#Salvar el audio en formato WAV 
wf = wave.open(filename,'wb')
wf.setnchannels(channels)
wf.setsampwidth(audio_obj.get_sample_size(formato))
wf.setframerate(fs)
wf.writeframes(b''.join(tramas)) #b contenido en bytes
#wf.close()

#Reproduce audio
winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)

datos = np.hstack(sonido) 
Normalizado = datos/np.max(np.abs(datos))

plt.figure(0)
L = len(Normalizado)
t = np.arange(0,L)/fs
plt.plot(t/2,Normalizado)
plt.title('Dominio del tiempo')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')

T = 1/fs
L = len(datos)
spec = np.abs(fourier.fft(datos))[:L//2]
freq = fourier.rfftfreq(L//2,T)[:L//2]
plt.figure(1)
plt.plot(freq,spec) 
plt.title('Dominio de la frecuencia')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud')

# #Seno
# T = 1.0/6
# x = np.linspace(0.1, fs*T,fs) 
# y = np.sin(60.0*np.pi*x)
# y_f = np.fft.fft(y)
# x_f = np.linspace(0.0,fs,fs//2)

# freq1 = fourier.rfftfreq(len(x),T)

# plt.figure()
# plt.plot(x,y)
# plt.title('Dominio del tiempo')

# plt.figure()
# plt.plot(x_f, 2.0/fs* np.abs(y_f[:fs//2]))
# plt.title('Dominio de la frecuencia')