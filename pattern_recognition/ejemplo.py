# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 10:08:23 2022

@author: Sala1
"""
#import OS #operator system
import numpy as np
import math
import matplotlib.pyplot as plt
from skimage import io,data
from mpl_toolkits import mplot3d

imagen = io.imread('Figuras1.jpg')
plt.figure(0)
plt.imshow(imagen)

rojo = imagen[:,:,0]
verde = imagen[:,:,1]
azul = imagen[:,:2]

# fig = plt.figure(1) #objeto tipo plot
# ejes = fig.add_subplot(111, projection = '3d')
# ejes.scatter(rojo,verde,azul)

obj0 = [174,25,21]
obj1 = [23,112,80]
obj2 = [17,68,123]
obj3 = [164,171,164]

filas = imagen.shape[0] #size
columnas = imagen.shape[1]
capas = imagen.shape[2]

salida = np.zeros([filas,columnas,capas])

for i in range(0,filas,1):
    for j in range(0,columnas,1):
        pixel = imagen[i,j,:]
        d0 = np.sqrt((obj0[0]-pixel[0])**2+(obj0[1]-pixel[1])**2+(obj0[2]-pixel[2])**2)
        d1 = np.sqrt((obj1[0]-pixel[0])**2+(obj1[1]-pixel[1])**2+(obj1[2]-pixel[2])**2)
        d2 = np.sqrt((obj2[0]-pixel[0])**2+(obj2[1]-pixel[1])**2+(obj2[2]-pixel[2])**2)
        d3 = np.sqrt((obj3[0]-pixel[0])**2+(obj3[1]-pixel[1])**2+(obj3[2]-pixel[2])**2)
        pos = np.argmin([d0,d1,d2,d3]) #Minimo de dos objetos, [] = compara todo el arreglo

        if pos == 0:
            salida[i,j,0] = 255
            salida[i,j,1] = 0
            salida[i,j,2] = 0
        elif pos == 1:
            salida[i,j,0] = 0
            salida[i,j,1] = 255
            salida[i,j,2] = 0
        elif pos == 2:
            salida[i,j,0] = 0
            salida[i,j,1] = 0
            salida[i,j,2] = 255
        elif pos == 3:
            salida[i,j,0] = 255
            salida[i,j,1] = 255
            salida[i,j,2] = 255
        
plt.figure(2)
plt.imshow(salida)

muestras = int(input('Cuantas muestras tomaras?')) #plt.input si no funciona/Teclado
plt.figure(1)
plt.imshow(imagen)
fondo = np.int32(plt.ginput(muestras)) #ginput mouse, posicion /int32, el rango de valores es miles
valores = imagen[fondo[:,1],fondo[0]]
proval = np.mean(valores, axis = 0) #axis = 0 columnas, axis = 1 filas



    
