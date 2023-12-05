# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 09:29:27 2022

@author: adalc
"""

import pyaudio
import winsound
import numpy as np
import wave
import matplotlib.pyplot as plt

from scipy.fft import fft, ifft
from math import log

def Data(Fourier):
    entropy = []
    Max = []
    for j in range(len(Fourier)) :
        suma = 0
        for i in range(len(Fourier[j])):
            suma = suma + (1/Fourier[j][i])*(log(Fourier[j][i],2))
        Max = Fourier[j][800]
        entropy.append (suma)
        Max.append(Max)
    P = np.zeros([len(entropy),2])
    P[:,0] = np.array(entropy)
    P[:,1] = np.array(Max)
    return (P)

def Normalizacion(P,maximaentropy,MaximoMax): 
    #normalización de Data
    P[:,0] = P[:,0]/maximaentropy
    P[:,1] = P[:,1] / MaximoMax
    return (P)

plt.close('all')
Fourier = np.loadtxt('Fourier. txt' )
P = Data(Fourier)
maximaentropy = max(P[:,0])
MaximoMax = max(P[:,1])
P = Normalizacion(P,maximaentropy,MaximoMax)
    
Target = [[1,1],[1,1],[1,1],[0,0],[0,0],[0,0],[1,0],[1,0],[1,0]]
W = np.random.rand(2,2)
b = np.random.rand(2)
Epoca = 0

while 1:
    result = []
    for j in range(len(P)):
        #neurona
        n = np.dot(W,P[j]) + b
        Res = []
        for l in range(np.shape(P)[1]):
            if n[l] >= 0:
                a = 1
                Res.append(1)
            else:
                a=0
                Res .append (0)
            e = Target[j][l] - a
            W[l] = W[l] + e*(P[j])
            b[l] = b[l] + e
        result.append(Res)
    Epoca = Epoca + 1
    if result == Target or Epoca == 50000:
        print("Ya se llego a:", result)
        print("con W:".W)
        print("y una polarización de b:",b)
        print("En ", Epoca, "Epocas")
        break
    

P = Data(Fourier)
maximaentropy = max(P[:,0])
MaximoMax = max(P[:,1])
P = Normalizacion(P,maximaentropy,MaximoMax)

plt.figure()
for i in range(9):
    if i < 3:
        Color = "black"
        Marca = "o"
        elif iss:
        Color = "red»
        Marca
        else:
        Color = "blue"
        Marca
        =
        "y"
        plt.plot (Pli,o],Pli,1l, marker-Marca, color=Color)
        plt. show()
    #fronteras
    WEnp.loadtxt("W.txt*)
    b=np.loadtxt(*b. txt' )
    × = np. linspace(0,1,5)
    m1=(p2(1]) /(-pito])
    y=ml*(x-pi[o])
    plt.plot(x, y, 'g')
    = np. Linspace(0,1,5)
    p1 = np.array([-biai/wta]lol, 01)
    p2 = p.array([0, -bla]/willa]l)
    plt.plot(x,
    Y.
    'g')
    plt.xlabell-pi-
    size = 16,)
    plt.ylabel("p2", size = 16)
    
    
    
    
    