# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:34:03 2022

@author: tomas
"""

#import os
import numpy as np
import math
import matplotlib.pyplot as plt
from skimage import io,data
from mpl_toolkits import mplot3d

#---------------------------------------
#Función distancia de mahalanobis
def dMaha (promedio, covarianza, pixel):
   
    d1 = (pixel-promedio).dot(np.linalg.inv(covarianza))
    d2 = d1.dot((pixel-promedio).T)
    d3 = np.sqrt(d2)
    
    return d3
#---------------------------------------

#imagen = io.imread('ImagenOriginal.jpg')
imagen = data.astronaut()
plt.figure(0)
plt.imshow(imagen)

rojo = imagen[:,:,0] #capa cero rojo
verde = imagen[:,:,1] #capa uno verde
azul = imagen[:,:,2] #capa dos azul

fig = plt.figure(1)#mostramos los datos de la imagen en un gráfico de agrupación
ejes = fig.add_subplot(111, projection = '3d')
ejes.scatter(rojo,verde,azul)


plt.figure(2)
plt.imshow(imagen)
muestra = np.int32(plt.ginput(-1)) 
valores = imagen[muestra[:,1],muestra[:,0]]
prom_val = np.mean(valores,axis=0)
cova = np.cov(valores.T,ddof = 1) 

#matriz de covarianza para la distancia de mahalanobis 

filas = imagen.shape[0] #número de filas
columnas = imagen.shape[1] #número de columnas
capas = imagen.shape[2] #número de capas
salida = np.ones([filas,columnas,capas]) #arreglo de zeros de (240,320,3)

for i in range(0,filas,1):
    for j in range(0,columnas,1):
        pixel = imagen[i,j,:] 
        DIS = dMaha(prom_val,cova,pixel)
        if DIS < 5:
            salida[i,j,0] = 0
            salida[i,j,1] = 0
            salida[i,j,2] = 0
            

plt.figure(3)
plt.imshow(salida)        
        
        
