# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:07:56 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt

datos = np.array([[200,20,10],[185,31,30],[31,150,100],[20,145,98],[15,20,190],[19,31,170]])
n = datos.shape[0] #Cantidad de datos
car = datos.shape[1] #Características
clases = 3

#Paso 1
# V = np.random.rand(clases,car)*255.0 #Muestras aleatorias de los datos es lo más adecuado
V = np.floor(np.random.rand(clases)*n) #De los propios datos extraer los centroides
V = np.concatenate((datos[int(V[0]),:],datos[int(V[1]),:]), axis = 0) #_Revisar esto
D = np.zeros((clases,n))


#Distancia | Paso 2
for i in range(clases):
    for k in range(n):
        suma1 = 0
        for j in range(car):
            suma1 = ((datos[k,j] - V[i,j])**2) + suma1
        D[i,k] = suma1**(1/2)

#Paso 3
U = np.zeros((clases,n))
for k in range(n):
    pos = np.argmin(D[:,k])
    U[pos,k] = 1
    
#Paso 4
for i in range(clases):
    for j in range(car):
        suma2 = 0.00000000000001
        suma3 = 0
        for k in range(n):
            suma2 = U[i,k] + suma2
            suma3 = U[i,k]*datos[k,j] + suma3
        V[i,j] = suma3/suma2



# def kmeans(x,V):
#     clases = len(V)
#     n = len(x)
#     car = x.shape[1]

#     D = np.zeros((clases,n))
    
#     for epocas in range(1000):
#         for i in range(clases):
#             for k in range(n):
#                 suma1 = 0.00000001
#                 for j in range(car):
#                     suma1 = ((x[k,j] - V[i,j])**2) + suma1
#                 D[i,k] = np.sqrt(suma1)
        
#         U = np.zeros((clases,n))
#         for k in range(n):
#             pos = np.argmin(D[:,k])
#             U[pos,k] = 1
            
#         for i in range(clases):
#             for j in range(car):
#                 suma2 = 0.0000001
#                 suma3 = 0
#                 for k in range(n):
#                     suma2 = len(U)
#                     suma3 = U[i,k] + suma3
#                 V[i,j] = suma3/suma2
                
#         print('Clases k-means:',len(V)) 
#         return D,U,V











            

