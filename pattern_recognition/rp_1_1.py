# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:07:37 2022

@author: adalc
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

"""

from mpl_toolkits import mplot3d
import numpy as np
from skimage import io,data #io-Entrada y salida, data-minibase de datos
import math
import matplotlib.pyplot as plt


def dMaha(promedio, covarianza, pixel):
    d1 = (pixel-promedio).dot(np.linalg.inv(covarianza))
    d2 = d1.dot((pixel-promedio).T)
    d3 = np.sqrt(d2)
    return d3

imagen = data.coffee()
plt.figure(0)
plt.imshow(imagen)

rojo=imagen[:,:,0]
verde=imagen[:,:,1]
azul=imagen[:,:,2]

fig=plt.figure(1)
ejes=fig.add_subplot(111,projection='3d')
ejes.scatter(rojo,verde,azul)

obj0=[174,25,21]
obj1=[23,112,80]
obj2=[17,68,123]
obj3=[164,171,164]

filas=imagen.shape[0]
columnas=imagen.shape[1]
capas=imagen.shape[2]

##############
#Distancia de Mahalanobis
#sqrt((prom-pixel)T*cov-1(prom-pixel))

salida = np.zeros((filas,columnas,3))

plt.figure(2)
plt.imshow(imagen)
muestra0 = np.int32(plt.ginput(-1)) #ginput mouse, posicion /int32, el rango de valores es miles #-1, las que el usuario quiera hasta usar clic derecho o enter (-1)
valores0 = imagen[muestra0[:,1],muestra0[:,0],:] #imagen[fondo[:,1],fondo[0],:] si no funciona
proval0 = np.mean(valores0, axis = 0) #axis = 0 columnas, axis = 1 filas   
cova0 = np.cov(valores0.T, ddof = 1) # .T transpuesta, ddof = 1 fila 

for ii in range(filas):
    for jj in range(columnas):
        pixel = imagen[ii,jj,:]
        DIS = dMaha(proval0,cova0,pixel)
        if (DIS < 5): #5 es el radio:
            salida[ii,jj,:] = imagen[ii,jj,:]
            print(salida[ii,jj,:])
        

plt.figure(3)
plt.imshow(salida)


#TAREA
#Linear Vector Quantization (LVQ)
'''
Obtener el umbarl de distancia

seleccionar un pixel, hacerlo una clase
segundo pixel, distancia euclidiana entre clase 1 y el pixel,
si la distancia es menor al umbral pertenece a la clase, si no es así, se crea otra clase
si es así, se toma el promedio ntre el pixel y la clase, será la nueva clase.
Así con todas las clases que vaya creando
'''


    
    
    
    
    
    
    
    
    
    
    
    
    