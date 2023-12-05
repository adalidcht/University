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

imagen=io.imread('figuras.jpeg')
plt.figure(0)
plt.imshow(imagen)

rojo=imagen[:,:,0]
verde=imagen[:,:,1]
azul=imagen[:,:,2]

fig=plt.figure(1)
ejes=fig.add_subplot(111,projection='3d')
ejes.scatter(rojo,verde,azul)

obj0 = proval0 # obj0 = [174,25,21]
obj1 = proval1 # obj1 = [23,112,80]
obj2 = proval2 # obj2 = [17,68,123]
obj3 = proval3 # obj3 = [164,171,164]

filas=imagen.shape[0]
columnas=imagen.shape[1]
capas=imagen.shape[2]
salida=np.zeros([filas,columnas,capas])

for i in range (0,filas,1):
    for j in range (0,columnas,1):
        pixel=imagen[i,j,:]
        d0=np.sqrt((obj0[0]-pixel[0])**2+(obj0[1]-pixel[1])**2+
             (obj0[2]-pixel[2])**2 )
        d1=np.sqrt((obj1[0]-pixel[0])**2+(obj1[1]-pixel[1])**2+
             (obj1[2]-pixel[2])**2 )
        d2=np.sqrt((obj2[0]-pixel[0])**2+(obj2[1]-pixel[1])**2+
             (obj2[2]-pixel[2])**2 )
        d3=np.sqrt((obj3[0]-pixel[0])**2+(obj0[1]-pixel[1])**2+
             (obj3[2]-pixel[2])**2 )
        pos=np.argmin([d0,d1,d2,d3])
        
        if pos==0:
            salida[i,j,0]=255
            salida[i,j,1]=0
            salida[i,j,2]=0
        elif pos==1:
            salida[i,j,0]=0
            salida[i,j,1]=255
            salida[i,j,2]=0
        elif pos==2:
           salida[i,j,0]=0
           salida[i,j,1]=0
           salida[i,j,2]=255
        elif pos==3:
            salida[i,j,0]=255
            salida[i,j,1]=255
            salida[i,j,2]=255
            
plt.figure(2)
plt.imshow(salida)
            
      
muestras = int(input(-1)) #plt.input si no funciona/Teclado
plt.figure(3)
plt.imshow(imagen)
fondo = np.int32(plt.ginput(muestras)) #ginput mouse, posicion /int32, el rango de valores es miles #-1, las que el usuario quiera hasta usar clic derecho o enter (-1)
valores0 = imagen[fondo[:,1],fondo[:,0]] #imagen[fondo[:,1],fondo[0],:] si no funciona
proval0 = np.mean(valores, axis = 0) #axis = 0 columnas, axis = 1 filas    
print(muestras) 
print(proval)

plt.figure(4)
plt.imshow(imagen)
objeto1 = np.int32(plt.ginput(muestras)) #ginput mouse, posicion /int32, el rango de valores es miles #-1, las que el usuario quiera hasta usar clic derecho o enter (-1)
valores1 = imagen[fondo[:,1],fondo[:,0]] #imagen[fondo[:,1],fondo[0],:] si no funciona
proval1 = np.mean(valores, axis = 0) #axis = 0 columnas, axis = 1 filas    
print(muestras) 
print(proval)

plt.figure(5)
plt.imshow(imagen)
objeto2 = np.int32(plt.ginput(muestras)) #ginput mouse, posicion /int32, el rango de valores es miles #-1, las que el usuario quiera hasta usar clic derecho o enter (-1)
valores2 = imagen[fondo[:,1],fondo[:,0]] #imagen[fondo[:,1],fondo[0],:] si no funciona
proval2 = np.mean(valores, axis = 0) #axis = 0 columnas, axis = 1 filas    
print(muestras) 
print(proval)

plt.figure(6)
plt.imshow(imagen)
objeto3 = np.int32(plt.ginput(muestras)) #ginput mouse, posicion /int32, el rango de valores es miles #-1, las que el usuario quiera hasta usar clic derecho o enter (-1)
valores3 = imagen[fondo[:,1],fondo[:,0]] #imagen[fondo[:,1],fondo[0],:] si no funciona
proval3 = np.mean(valores, axis = 0) #axis = 0 columnas, axis = 1 filas    
print(muestras) 
print(proval)
#Lo anterior para cada objeto 4

#Distancia en bloques o Manhattan, distancia en absolutos, no tiene valores flotantes
#Distancia euclidiana    
#Distancia Mahalanobis  
# A=B y B=A distancia, A=b y B!=A es divergencia
#En clasificacion es mas estable en mahalanobis (menos susceptible al ruido), manhattan da ruido

#Distancia de mahalanobis
 #Matriz de covarianza
#Linealmente independientes las caracteristicas de una matriz de covarianza con diagonal principal de ceros, caso contrario con 1 ya que son dependientes
#correlacionado = linealmente dependiente
    
            


































