# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:08:37 2022

@author: adalc
"""

import winsound
import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.close('all')

#Grabación
#8k muestras/s en paquetes de 512 de 16 bits
chunk = 512 #Tamaño del paquete. Paquete de información, ventanas de 512. Múltiplos de 2^n
sample_format = pyaudio.paInt16 #Valores de 16 bits
channels = 2 #Stereo
fs = 8000 #Frecuencia de muestre, 8000 muestras/s. 44k muestras/s (mp3)
seconds = 1.5
filename = 'comparacion1.wav' #Archivo crudo
audio_obj = pyaudio.PyAudio() #Objeto de audio

input('Presionar Enter')
print('La grabación ha iniciado')

#Inicia grabación
stream = audio_obj.open(format = sample_format,channels = channels,rate = fs,frames_per_buffer = chunk,input = True) #Formato de audio, bits de audio

tramas = [] #
sonido = [] #Se lee del buffer los valores numericos

for i in range(0,int(fs/chunk*seconds)): #Cantidad de datos a almacenar
    datos = stream.read(chunk) #Lee muestras del stream
    tramas.append(datos)
    sonido.append(np.frombuffer(datos,dtype = np.int16))

#Detiene y cierra la grabación
stream.stop_stream()
stream.close()
audio_obj.terminate() #Destruye el objeto de audio, libera la tarjeta de audio
#Se debe cerrar para desocupar la tarjeta de audio

print('La grabación ha terminado')

#Salvar el audio en formato WAV 
wf = wave.open(filename,'wb') #wb Archivo de escritura
wf.setnchannels(channels)
wf.setsampwidth(audio_obj.get_sample_size(sample_format)) #Ancho de muestreo
wf.setframerate(fs) #Velocidad de muestreo
wf.writeframes(b''.join(tramas)) #b contenido en bytes, como lo va a escribir
#wf.close()

#Reproduce audio
winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC) 

#Señal
signal = np.hstack(sonido) 
plt.figure()
plt.plot(signal)

signaln = signal/np.max(np.abs(signal)) #Normalizado
plt.figure()
plt.plot(signaln)

ventana1 = np.where(np.abs(signaln) >= 0.1,1,0) #cumple 1, no cumple 0
plt.figure()
plt.plot(ventana1)
#Ruido blanco no rebasa 10% de la señal
#Tiene problemas de frontera. Frecuencias fantasma

#Ventanas de 1%,5%,10% de la señal. 10% de la señal serán las usadas
#Ventanas de 10%, desplazamiento de 1% (shifting)
signal2 = []
for i in range(0,len(ventana1)-799,1): #10% de 8000
    signal2.append(np.mean(ventana1[i:i+800]))

plt.figure()
plt.plot(signal2)


ventana2 = np.where(np.array(signal) >= 0.1,1,0) #cumple 1, no cumple 0 | con np.abs() muestra la señal completa
signal3 = []
for i in range(0,len(ventana2)-399,1): #10% de 8000
    if(ventana2[i] == 1):
        signal3.append(signaln[i])  

plt.figure()
plt.plot(signal3)

#Filtro de preénfasis
corre = np.zeros(len(signal3))
corre[1:-1] = signal3[0:-2]
pre = corre - (0.95*np.array(signal3)) #coeficiente de preénfasis CP > 85% [0.95]
plt.figure()
plt.plot(pre)
#Hay problemas con picos de datos que no están en la señal original

#Eliminar picos
for i in range(0,len(pre),1):
    if(np.abs(np.float16(pre[i])) >= 0.9):
        pre[i] = 0
        
#Espectrograma de Fourier
frame = 400
overlap = 80
spec = []
k = 0
for i in range(0,len(pre) - (frame-1),overlap):
    k = k + 1
    FOU = np.abs(np.fft.fft(pre[i:frame-1 + i]*np.hamming(frame-1))) #Con la ventana de Hamming evitas problemas de frontera
    spec.append(FOU[0:200])


# x,y = np.meshgrid(range(0,k,1),range(0,200,1),sparse = True)
y = np.linspace(0,1,k)
x = np.linspace(0,1,200)
xv,yv = np.meshgrid(x,y,sparse = True)
z  = np.array(spec)
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
# ax = fig.gca(projection = '3d')
surf = ax.plot_surface(xv,yv,z,cmap = 'coolwarm', linewidth = 0)

    






