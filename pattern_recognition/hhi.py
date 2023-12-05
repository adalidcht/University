# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:07:00 2022

@author: Eeduardo
"""

import winsound 
import pyaudio 
import wave
import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from time import sleep

chunk  = 512 #Tamaño de paquete 
sample_format = pyaudio.paInt16
chanels = 2
fs = 8000
seconds = 15
filename = 'palabra.wav'

audio_obj = pyaudio.PyAudio()
input('Precione tecla ')
print('inica grabación')
stream = audio_obj.open(format= sample_format, channels = chanels, rate= fs, frames_per_buffer = chunk, input=True )
tramas =[]
sonido = []
for i in range(0, int(fs/(chunk*seconds))):
    datos = stream.read(chunk)
    tramas.append(datos)
    sonido.append(np.frombuffer(datos,dtype = np.int16))
stream.stop_stream()
stream.close()
audio_obj.terminate()
print('termina la grabación')

wf = wave.open(filename,'wb')
wf.setnchannels(chanels)
wf.setsampwidth(audio_obj.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(tramas))
wf.close

winsound.PlaySound(filename, winsound.SND_FILENAME | winsound.SND_ASYNC)

senal = np.hstack(sonido)
plt.figure()
plt.plot(senal)