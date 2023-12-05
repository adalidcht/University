# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 08:35:41 2023

@author: adalc
"""

from skimage import io,data
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets


def DistEu(dato,centros):
    distancia = []
    clases = len(centros)
    caracteristicas = len(dato)
    for i in range(clases):
        suma = 0
        for j in range(caracteristicas):
            suma = ((dato[j] - centros[i][j])**2) + suma
            distancia.append(np.sqrt(suma))
    return distancia

color = datasets.load_iris().data #data.chelsea()
clases = 0
centros = []
umbral = 70



for i in range(color.shape[0]):
    for j in range(color.shape[1]):
        if (clases == 0):
            centros.append(np.float32(color[i,j])) #[i,j,:]
            clases = clases + 1
        dato = np.float32(color[i,j]) #[i,j,:]
        dis = DistEu(dato,centros)
        if (min(dis) <= umbral):
            for k in range(len(dato)):
                centros[dis.index(min(dis))][k] = (centros[dis.index(min(dis))][k] + dato[k])/2
                
            