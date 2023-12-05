# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:28:35 2022

@author: joshu
"""

from skimage import io, color
import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fz

def defuzzy(rango,valor):
    numerador = np.sum(rango*valor)
    denominador = np.sum(valor)
    centro = numerador/denominador
    return centro      
        

personas = io.imread('piel_1.jpg')

fil = personas.shape[0]
col = personas.shape[1]
binario = np.zeros((fil,col))

plt.figure(0)
plt.imshow(personas)

hsv = color.rgb2hsv(personas)

plt.figure(1)
plt.imshow(hsv)

#----------fuzzyfication---------------#

valor = np.linspace(0,1,256)

hbajo = fz.zmf(valor,0.08,0.1)
hmedio = fz.gbellmf(valor,0.03,1,0.13)
halto = fz.smf(valor,0.15,0.17)

sbajo = fz.zmf(valor,0.07,0.3)
smedio = fz.gbellmf(valor,0.3,1,0.5)
salto = fz.smf(valor,0.7,0.9)

vbajo = fz.zmf(valor,0.04,0.07)
vmedio = fz.gbellmf(valor,0.2,2.5,0.2)
valto = fz.smf(valor,0.45,0.5)

plt.figure(2)
plt.plot(valor,vbajo)
plt.plot(valor,vmedio)
plt.plot(valor,valto)

#------------defuzzyfication-----------#

valor = np.linspace(0,1,200)
no_piel = fz.gaussmf(valor,0.25,0.075)
piel = fz.gaussmf(valor,0.75,0.075)

#------------------main loop------------------------#

r = np.zeros(27)
for i in range(fil):
    for j in range(col):
        print(i)
        print(j)
        h = hsv[i,j,0]
        s = hsv[i,j,1]
        v = hsv[i,j,2]
        
        hbajo = fz.zmf(np.array([h]),0.08,0.1)
        hmedio = fz.gbellmf(np.array([h]),0.03,1,0.13)
        halto = fz.smf(np.array([h]),0.15,0.17)

        sbajo = fz.zmf(np.array([s]),0.07,0.3)
        smedio = fz.gbellmf(np.array([s]),0.3,1,0.5)
        salto = fz.smf(np.array([s]),0.7,0.9)

        vbajo = fz.zmf(np.array([v]),0.04,0.07)
        vmedio = fz.gbellmf(np.array([v]),0.2,2.5,0.2)
        valto = fz.smf(np.array([v]),0.45,0.5)
        
        r[0] = np.min([hbajo,sbajo,vbajo])
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
        
        R0 = np.minimum(r[0],no_piel)
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
        
        Salida = np.max([R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R20,R21,R22,R23,R24,R25,R26],axis = 0)
        
        Real = defuzzy(np.linspace(0.0,1.0,200),Salida)
        
        if (Real < 0.5):
            binario[i,j] = 1
        else:
            binario[i,j] = 0
        

plt.figure(2)
plt.imshow(binario,cmap = 'gray')

plt.figure(3)
plt.plot(Salida)


        
        
        
        
        




