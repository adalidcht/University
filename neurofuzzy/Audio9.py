# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 00:40:04 2022

@author: Saul
"""

import numpy as np
import pyaudio
import wave
import matplotlib.pyplot as plt
import winsound
from scipy.fft import fft, ifft
from math import log

def EntropiaShannon(Audios):
    H = 0
    for i in range(len(Audios[:546])):
        H -= Audios[i]*log(Audios[i])
        
    H1 = 0
    for i in range(546,len(Audios[:1340])):
        H1 -= Audios[i]*log(Audios[i])
        
    H2 = 0
    for i in range(1340,len(Audios)):
        H2 -= Audios[i]*log(Audios[i])
    return(H,H1,H2)
    
def Data(Fourier):
    Entropy=[]
    MaxData=[]
    for j in range(len(Fourier)):
        suma=0
        for i in range(len(Fourier[j])):
            suma=suma+(1/Fourier[j][i])*(log(Fourier[j][i],2))
        Max=Fourier[j][1250]
        
        Entropy.append(suma)
        MaxData.append(Max)
    P=np.zeros([len(Entropy),2])
    P[:,0]=np.array(Entropy)
    P[:,1]=np.array(MaxData)
    return(P)

def Norm(P, EntropyMax, MaximoMax):
    P[:,0]=P[:,0]/EntropyMax
    P[:,1]=P[:,1]/MaximoMax
    return(P)
plt.close('all')

paquete=512
sample=pyaudio.paInt16
canales=1
fs=8000
segundos=2

words=[]

Fourier=[]
T = 1.0 / 6
x = np.linspace(0.0, fs*T,fs)
y = np.sin(60.0*np.pi*x)

y_f = fft(y)

x_f = np.linspace(0.0, 1.0/(2.0*T), fs//2)
plt.figure(1)
plt.title('Seno FFT')




plt.plot(x_f, 2.0/fs* np.abs(y_f[:fs//2]))

plt.figure(2)
plt.title('Seno sin FFT')
plt.plot(x,y)

for j in range(9):
    archive=str(j)+'patron.wav'
    obj_audio=pyaudio.PyAudio()
    
    input('Presiona na tecla \n')
    
    streaming = obj_audio.open(format=sample, channels=canales,  rate=fs,
                               frames_per_buffer=paquete, input=True)
    tramas=[]
    sonido=[]
    
    for i in range(0,int(fs/paquete*segundos)):
        datos=streaming.read(paquete)
        tramas.append(datos)
        sonido.append(np.frombuffer(datos, dtype=np.int16))
        
        
    streaming.stop_stream()
    streaming.close()
    
    obj_audio.terminate()
    
    
    wf=wave.open(archive, 'wb')
    wf.setnchannels(canales)
    wf.setsampwidth(obj_audio.get_sample_size(sample))
    wf.setframerate(fs)
    wf.writeframes(b''.join(tramas))
    wf.close()
    winsound.PlaySound(archive, winsound.SND_FILENAME | winsound.SND_ASYNC)
    
    
    Palabra=np.hstack(sonido)
    Frec=fft(Palabra)
    Tamaño=len(Frec)
    Fourier.append(abs(Frec[0:int(Tamaño/2)]))
    print('Palabra número ',j+1,' grabada')
    
    np.savetxt('sonido.txt', sonido, fmt='%.18g', delimiter=' ')

    np.savetxt('Fourier.txt', Fourier, fmt='%.18g', delimiter=' ')

print('Sali del for')
    
Fourier=np.loadtxt('Fourier.txt')
Palabra=np.loadtxt('sonido.txt')

plt.figure(3)

plt.title('Perro 1 sin FFT')
plt.plot(Palabra[0])

plt.figure(4)

plt.title('Perro 1 FFT')
plt.plot(Fourier[0])


plt.figure(5)
plt.title('Gato 1 sin FFT')
plt.plot(Palabra[3])

plt.figure(6)
plt.title('Gato 1 FFT')
plt.plot(Fourier[3])

plt.figure(7)
plt.title('Japón 1 sin FFT')
plt.plot(Palabra[6])

plt.figure(8)
plt.title('Japón 1 FFT')
plt.plot(Fourier[6])

plt.figure(9)

plt.title('Perro 2 sin FFT')
plt.plot(Palabra[1])

plt.figure(10)

plt.title('Perro 2 FFT')
plt.plot(Fourier[1])

plt.figure(11)
plt.title('Gato 2 sin FFT')
plt.plot(Palabra[4])

plt.figure(12)
plt.title('Gato 2 FFT')
plt.plot(Fourier[4])

plt.figure(13)
plt.title('Japón 2 sin FFT')
plt.plot(Palabra[7])

plt.figure(14)
plt.title('Japón 2 FFT')
plt.plot(Fourier[7])

plt.figure(15)

plt.title('Perro 3 sin FFT')
plt.plot(Palabra[2])

plt.figure(16)

plt.title('Perro 3 FFT')
plt.plot(Fourier[2])

plt.figure(17)
plt.title('Gato 3 sin FFT')
plt.plot(Palabra[5])

plt.figure(18)
plt.title('Gato 3 FFT')
plt.plot(Fourier[5])

plt.figure(19)
plt.title('Japón 3 sin FFT')
plt.plot(Palabra[8])
    
plt.figure(20)
plt.title('Japón 3 FFT')
plt.plot(Fourier[8])


fig=plt.figure(21)
ax = fig.add_subplot(111,projection = '3d')
s=[]
for i in (0,8,1):
    s[i] = EntropiaShannon(Fourier[i])
    ax.scatter(s[i,0],s[i,1],s[i,2], color = 'mediumorchid')
  
    
print('Fin del programa')

