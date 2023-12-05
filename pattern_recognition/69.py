# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:13:21 2022

@author: adalc
"""


from mpl_toolkits import mplot3d
import numpy as np
from skimage import io,data,color,measure #io-Entrada y salida, data-minibase de datos
from scipy import ndimage
import math
import matplotlib.pyplot as plt

#-------------------------
print('Primera parte del programa: Entrenamiento del sistema')
bin1 = (io.imread('entrena6.bmp')>100).astype(int) #>100 hace la imagen binaria en blancos, astype(int) lo hace entero
bin2 = (io.imread('entrena9.bmp')>100).astype(int)
plt.close('all')
plt.figure(1)
plt.imshow(bin1)
#-------------------------
ima6,can6 = measure.label(bin1,return_num = True, connectivity = 2) #label etiqueta objetos y engloba, connectivity=1 vecindad 4, ''= 2 vecindad 8
ima9,can9 = measure.label(bin2,return_num = True, connectivity = 2)
plt.figure(2)
plt.imshow(ima9)
    
for j in range(1,3,1): #0,|1,2
    if j == 1:
        numero = ima6
        cantidad = can6
        print('Se procesa el número 6')
    else:
        numero = ima9
        cantidad = can9
        print('Se procesa el número 9')
    dato = []
    for i in range(1,cantidad,1):
        print('Objeto %s de %s' (i,cantidad))
        s1 = np.where(numero == i,1,0)#Aisla un 6 en particular y ko binariza|where, encuentra algo | (numero a encontrar,donde esté agrega un 1, donde no esté agrega 0)
        s2 = ndimage.binary_fill_holes(s1).astype(int) #Genera otra imagen con el 6 rellenado
        s3 = np.logical_xor(s1,s2) #solo dejará el circulo del 6
        
        
        
        