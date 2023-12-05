# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:55:12 2022

@author: adalc
"""


#--------------------------------
#Distancia euclidiana
def DistEu(dato,centros): # dato: primer pixel que acaba de entrar, centros acumulados de las otras clases
    distancia = []
    clases = len(centros)
    caracterirsticas = len(dato)
    for i in range (clases):
        suma = 0
        for j in range(caracteristicas):
            suma = ((dato[j]-centros[i][j])**2) + suma
            distancia.append(nq.sqrt(suma))
            
    return distancia
#--------------------------------

imagen = io.imread()

clases = 0
centros = []
umbral = 100

for i in range(imagen.shape[0]):
    for j in range(imagen.shape[1]):
        if (clases == 0):
            centros.append(np.float32(imagen[i,j,:]))
            clases = clase