# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 10:20:39 2022

@author: tomas
"""

#import os
import numpy as np
import math
import matplotlib.pyplot as plt
from skimage import io,data
from mpl_toolkits import mplot3d

#---------------------------------------

#imagen = io.imread('ImagenSintetica.jpg')
imagen = data.chelsea()
plt.figure(0)
plt.imshow(imagen)

rojo = imagen[:,:,0] #capa cero rojo
verde = imagen[:,:,1] #capa uno verde
azul = imagen[:,:,2] #capa dos azul

fig = plt.figure(1)#mostramos los datos de la imagen en un gráfico de agrupación
ejes = fig.add_subplot(111, projection = '3d')
ejes.scatter(rojo,verde,azul)

#muestras1 = int(input("Cuantas Muestras?"))

print("Primer set de muestras fondo")
plt.figure(2)
plt.imshow(imagen)
fondo1 = np.int32(plt.ginput(-1)) 

#ginput: entrada del mouse
#estas entradas no dan el valor del pixel, dan la posición del click, generando un vector

# Si quiero dar un número indeterminado de muestras, tengo que poner un -1 en 
# el argumento de ginput

valores1 = imagen[fondo1[:,1],fondo1[:,0]] #Tomar todas la filas de la segunda y primer columna
proval1 = np.mean(valores1,axis=0) #axis 0 significa promedio de datos vertical
#axis 1 significa promedio horizontal
print(valores1)


print("Segundo set de muestras rojo")
plt.figure(3)
plt.imshow(imagen)
fondo2 = np.int32(plt.ginput(-1)) 
valores2 = imagen[fondo2[:,1],fondo2[:,0]]
proval2 = np.mean(valores2,axis=0) 
print(valores2)

print("Tercer set de muestras verde")
plt.figure(4)
plt.imshow(imagen)
fondo3 = np.int32(plt.ginput(-1)) 
valores3 = imagen[fondo3[:,1],fondo3[:,0]]
proval3 = np.mean(valores3,axis=0) 
print(valores3)

print("Cuarto set de muestras azul")
plt.figure(4)
plt.imshow(imagen)
fondo4 = np.int32(plt.ginput(-1)) 
valores4 = imagen[fondo4[:,1],fondo4[:,0]]
proval4 = np.mean(valores4,axis=0) 
print(valores4)

filas = imagen.shape[0] 
columnas = imagen.shape[1] 
capas = imagen.shape[2] 
salida = np.zeros([filas,columnas,capas]) 



for i in range(0,filas,1):
    for j in range(0,columnas,1):
        pixel = imagen[i,j,:] #Se va a tomar cada pixel de la matriz
        d0 = np.sqrt(   (proval1[0]-pixel[0])**2+(proval1[1]-pixel[1])**2+
                      (proval1[2]-pixel[2])**2)
        d1 = np.sqrt(   (proval2[0]-pixel[0])**2+(proval2[1]-pixel[1])**2+
                      (proval2[2]-pixel[2])**2)
        d2 = np.sqrt(   (proval3[0]-pixel[0])**2+(proval3[1]-pixel[1])**2+
                      (proval3[2]-pixel[2])**2)
        d3 = np.sqrt(   (proval4[0]-pixel[0])**2+(proval4[1]-pixel[1])**2+
                      (proval4[2]-pixel[2])**2)
        pos = np.argmin([d0,d1,d2,d3])#de cada pixel toma la distancia mínima
        
        if pos == 0: #si la posición es 0, la salida es rojo
            salida[i,j,0] = 255
            salida[i,j,1] = 255
            salida[i,j,2] = 255
        elif pos == 1:
            salida[i,j,0] = 255
            salida[i,j,1] = 0
            salida[i,j,2] = 0
        elif pos == 2:
            salida[i,j,0] = 0
            salida[i,j,1] = 255
            salida[i,j,2] = 0
        elif pos == 3:
            salida[i,j,0] = 0
            salida[i,j,1] = 0
            salida[i,j,2] = 255
            
plt.figure(5)
plt.imshow(salida)            
            
            
            
            
            
            
            
            