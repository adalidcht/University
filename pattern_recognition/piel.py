# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:48:06 2022

@author: adalc
"""

import skfuzzy as fuzzy
import numpy as np
import matplotlib.pyplot as plt
from skimage import io,color

def defuzzy(rango,valor):
    numerador = np.sum(rango*valor)
    denominador = np.sum(valor)
    centro = numerador/denominador
    return centro


plt.close("all")



personas = io.imread('piel1.jpg') 
fil = personas.shape[0]
col = personas.shape[1]

binario = np.zeros((fil,col))

plt.figure(0)
plt.imshow(personas)

hsv = color.rgb2hsv(personas)

plt.figure(1)
plt.imshow(hsv)

#fuzzyfication
# valor = np.linspace(0,1,255)
# hbajo = fuzzy.zmf(valor,0.2,0.5) #Z membership function | 0.2 parte alta, 0.5 parte baja
# hmedio = fuzzy.gbellmf(valor,0.1,1,0.5)
# halto = fuzzy.smf(valor,0.8,0.9)

# sbajo = fuzzy.zmf(valor,0.2,0.5) 
# smedio = fuzzy.gbellmf(valor,0.1,1,0.5)
# salto = fuzzy.smf(valor,0.8,0.9)

# vbajo = fuzzy.zmf(valor,0.2,0.5) 
# vmedio = fuzzy.gbellmf(valor,0.1,1,0.5)
# valto = fuzzy.smf(valor,0.8,0.9)

# #Defuzzyficution
valor = np.linspace(0,1,200)
no_piel = fuzzy.gaussmf(valor,0.25,0.075)
piel = fuzzy.gaussmf(valor,0.75,0.75)

#mainloop
r = np.zeros(27) # 27 = 3^3
for i in range(fil):
    for j in range(col):
        h = np.array([hsv[i,j,0]])
        s = np.array([hsv[i,j,1]])
        v = np.array([hsv[i,j,2]])
        
        #fuzzyfication
        hbajo = fuzzy.zmf(h,0.2,0.5) #Z membership function | 0.2 parte alta, 0.5 parte baja
        hmedio = fuzzy.gbellmf(h,0.1,1,0.5)
        halto = fuzzy.smf(h,0.8,0.9)

        sbajo = fuzzy.zmf(s,0.2,0.5) 
        smedio = fuzzy.gbellmf(s,0.1,1,0.5)
        salto = fuzzy.smf(s,0.8,0.9)

        vbajo = fuzzy.zmf(v,0.2,0.5) 
        vmedio = fuzzy.gbellmf(v,0.1,1,0.5)
        valto = fuzzy.smf(v,0.8,0.9)
        
        #Relación difusa
        r[0] = np.min([hbajo,sbajo,vbajo]) # np.min genera un escalar
        r[1] = np.min([hbajo,sbajo,vmedio])
        r[2] = np.min([hbajo,sbajo,valto])
        r[3] = np.min([hbajo,smedio,vbajo])
        r[4] = np.min([hbajo,smedio,vmedio])
        r[5] = np.min([hbajo,smedio,valto])
        r[6] = np.min([hbajo,salto,vbajo])
        r[7] = np.min([hbajo,salto,vmedio])
        r[8] = np.min([hbajo,salto,valto])
        r[9] = np.min([hmedio,sbajo,vbajo])
        r[10] = np.min([hmedio,sbajo,vmedio])
        r[11] = np.min([hmedio,sbajo,valto])
        r[12] = np.min([hmedio,smedio,vbajo])
        r[13] = np.min([hmedio,smedio,vmedio])
        r[14] = np.min([hmedio,smedio,valto])
        r[15] = np.min([hmedio,salto,vbajo])
        r[16] = np.min([hmedio,salto,vmedio])
        r[17] = np.min([hmedio,salto,valto])
        r[18] = np.min([halto,sbajo,vbajo])
        r[19] = np.min([halto,sbajo,vmedio])
        r[20] = np.min([halto,sbajo,valto])
        r[21] = np.min([halto,smedio,vbajo])
        r[22] = np.min([halto,smedio,vmedio])
        r[23] = np.min([halto,smedio,valto])
        r[24] = np.min([halto,salto,vbajo])
        r[25] = np.min([halto,salto,vmedio])
        r[26] = np.min([halto,salto,valto])
        
        
        R0 = np.minimum(r[0],no_piel) #compara todos los calores y genera un vector
        R1 = np.minimum(r[1],no_piel)
        R2 = np.minimum(r[2],no_piel)
        R3 = np.minimum(r[3],no_piel)
        R4 = np.minimum(r[4],no_piel)
        R5 = np.minimum(r[5],piel)
        R6 = np.minimum(r[6],no_piel)
        R7 = np.minimum(r[7],no_piel)
        R8 = np.minimum(r[8],no_piel)
        R9 = np.minimum(r[9],no_piel)
        R10 = np.minimum(r[10],no_piel)
        R11 = np.minimum(r[11],no_piel)
        R12 = np.minimum(r[12],no_piel)
        R13 = np.minimum(r[13],no_piel)
        R14 = np.minimum(r[14],no_piel)
        R15 = np.minimum(r[15],no_piel)
        R16 = np.minimum(r[16],no_piel)
        R17 = np.minimum(r[17],no_piel)
        R18 = np.minimum(r[18],no_piel)
        R19 = np.minimum(r[19],no_piel)
        R20 = np.minimum(r[20],no_piel)
        R21 = np.minimum(r[21],no_piel)
        R22 = np.minimum(r[22],no_piel)
        R23 = np.minimum(r[23],no_piel)
        R24 = np.minimum(r[24],no_piel)
        R25 = np.minimum(r[25],no_piel)
        R26 = np.minimum(r[26],no_piel)
        
        salida = np.max([R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26], axis = 0)
        real = defuzzy(np.linspace(0.0,1.0,200),salida)
        
        if(real < 0.5):
            binario[i,j] = 1
        else:
            binario[i,j] = 0

plt.figure(2)
plt.plot(binario)

plt.figure(3)
plt.plot(salida)

plt.figure(4)
plt.plot(real)

# plt.figure(2)
# plt.plot(valor,hbajo)
# plt.plot(valor,hmedio)
# plt.plot(valor,halto)
  

# plt.legend(['1','2'])


