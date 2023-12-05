# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:14:12 2022

@author: adalc
"""

from mpl_toolkits import mplot3d
import numpy as np
from skimage import io,data,color #io-Entrada y salida, data-minibase de datos
import math
import matplotlib.pyplot as plt

plt.close('all')

imagen = io.imread('placac.jpeg')
plt.figure(0)
plt.imshow(imagen)

gris = color.rgb2gray(imagen)
plt.figure(1)
plt.imshow(gris,cmap = 'gray')

binario = gris < 0.5
plt.figure(2)
plt.imshow(binario,cmap = 'gray')

grafica1 = np.sum(binario,axis = 1) #axis = 1, suma por filas
plt.figure(3)
plt.plot(grafica1)

recorte1 = binario[46:116,:]

plt.figure(4)
plt.imshow(recorte1,cmap = 'gray')

grafica2 = np.sum(recorte1,axis = 0)
plt.figure(5)
plt.plot(grafica2)

numero = recorte1[:,245:270]*1.0
numero2 = recorte1[:,274:307]*1.0
plt.figure(6)
plt.imshow(numero,cmap = 'gray')


perfil = []
for i in range(numero.shape[0]):
    for j in range(numero.shape[1]):
        if numero[i,j] == 1:
            perfil.append(j)
            break
        
plt.figure(7)
plt.plot(perfil)


for i in range(numero.shape[0]):
    for j in range(numero.shape[1]-1,0,-1):
        if numero[i,j] == 1:
            perfil.append(j)
            break

plt.figure(8)
plt.plot(perfil)

perfil = perfil/np.max(perfil)
#pl



perfil2 = []
for i in range(numero2.shape[0]):
    for j in range(numero2.shape[1]):
        if numero2[i,j] == 1:
            perfil2.append(j)
            break
        
plt.figure(10)
plt.plot(perfil2)


for i in range(numero2.shape[0]):
    for j in range(numero2.shape[1]-1,0,-1):
        if numero2[i,j] == 1:
            perfil2.append(j)
            break

plt.figure(11)
plt.plot(perfil2)

perfil2 = perfil2/np.max(perfil2)
plt.figure(12)
plt.plot(perfil2)

plt.figure(13)
plt.plot(perfil)
plt.plot(perfil2)

a = np.corrcoef(perfil,perfil2)#revisar doc
#Polinomio de Lagrange
#Expansion y compresion de una grafica



