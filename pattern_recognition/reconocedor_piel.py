# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:01:30 2022

@author: guayo
"""

import numpy as np 
import math
import matplotlib.pyplot as plt
from skimage import io,data,color
import skfuzzy as fuzzy
 
#-------------------------------
plt.close('all')
persona=io.imread('persona1.jpg')
plt.figure(1)
plt.imshow(persona)
hsv=color.rgb2hsv(persona)
plt.figure(2)
plt.imshow(hsv)
fil=hsv.shape[0]
col=hsv.shape[1]

def defuzzy(rango,valor):
    numerador=np.sum(rango*valor)
    denomina=np.sum(valor)
    centro=numerador/denomina
    return centro
#::::::::::::::::FUZZYFICATION:::::::::::::::::::::::::::::

#----------Conjuntos fuzzy-------
valor=np.linspace(0,1,256) #de 0 a 1 con 256 divisiones para poder procesar h

#:::::::::::::Haciendo los conjuntos de entrada
# hbajo=fuzzy.zmf(valor,0.1,0.3)
# hmedio=fuzzy.gbellmf(valor,0.3,5,0.5) #en medio se controla la caída, al final donde se ubica la campana
# #principio lo que queremos que abra o cierre la campana 
# halto=fuzzy.smf(valor,0.8,0.9)

hbajo=fuzzy.zmf(valor,0.1,0.3)
hmedio=fuzzy.gbellmf(valor,0.15,5,0.45) #en medio se controla la caída, al final donde se ubica la campana
#principio lo que queremos que abra o cierre la campana 
halto=fuzzy.smf(valor,0.5,0.8)
plt.figure()
plt.plot(hbajo)
plt.plot(hmedio)
plt.plot(halto)


# sbajo=fuzzy.zmf(valor,0.1,0.3)
# smedio=fuzzy.gbellmf(valor,0.3,5,0.5) 
# salto=fuzzy.smf(valor,0.8,0.9)

# vbajo=fuzzy.zmf(valor,0.1,0.3)
# vmedio=fuzzy.gbellmf(valor,0.3,5,0.5) 
# valto=fuzzy.smf(valor,0.8,0.9)

# #:::::::::::::Defusificacion::::::::::::::::::::::::

# #Haciendo los conjuntos de salida
# valor=np.linspace(0,1,200) 
# no_piel=fuzzy.gaussmf(valor,0.25,0.75)
# piel=fuzzy.gaussmf(valor,0.75,0.075)

# #::::::::::::::::::::MAIN LOOP:::::::::::::::::::::::
# r=np.zeros(27) #regla difusa
# binario=np.zeros((fil,col))

# for i in range(fil):
#     for j in range(col):
#         h=hsv[i,j,0]
#         s=hsv[i,j,1]
#         v=hsv[i,j,2]
#         #::::::::::::::::fuzzyfication:::::::::::::
#         hbajo=fuzzy.zmf(np.array([h]),0.07,0.2)
#         hmedio=fuzzy.gbellmf(np.array([h]),0.3,5,0.5) #en medio se controla la caída, al final donde se ubica la campana
#         #principio lo que queremos que abra o cierre la campana 
#         halto=fuzzy.smf(np.array([h]),0.8,0.9)
        
        
#         sbajo=fuzzy.zmf(np.array([s]),0.1,0.3)
#         smedio=fuzzy.gbellmf(np.array([s]),0.1,5,0.5) 
#         salto=fuzzy.smf(np.array([s]),0.8,0.9)
        
#         vbajo=fuzzy.zmf(np.array([v]),0.1,0.3)
#         vmedio=fuzzy.gbellmf(np.array([v]),0.3,5,0.5) 
#         valto=fuzzy.smf(np.array([v]),0.85,0.95)
        
#         # #relaciones difusas
#         r[0]=np.min([hbajo, sbajo, vbajo])
#         r[1]=np.min([hbajo, sbajo, vmedio])
#         r[2]=np.min([hbajo, sbajo, valto])
#         r[3]=np.min([hbajo, smedio, vbajo])
#         r[4]=np.min([hbajo, smedio, vmedio])
#         r[5]=np.min([hbajo, smedio, valto])
#         r[6]=np.min([hbajo, salto, vbajo])
#         r[7]=np.min([hbajo, salto, vmedio])
#         r[8]=np.min([hbajo, salto, valto])
        
#         r[9]=np.min([hmedio, sbajo, vbajo])
#         r[10]=np.min([hmedio, sbajo, vmedio])
#         r[11]=np.min([hmedio, sbajo, valto])
#         r[12]=np.min([hmedio, smedio, vbajo])
#         r[13]=np.min([hmedio, smedio, vmedio])
#         r[14]=np.min([hmedio, smedio, valto])
#         r[15]=np.min([hmedio, salto, vbajo])
#         r[16]=np.min([hmedio, salto, vmedio])
#         r[17]=np.min([hmedio, salto, valto])
        
#         r[18]=np.min([halto, sbajo, vbajo])
#         r[19]=np.min([halto, sbajo, vmedio])
#         r[20]=np.min([halto, sbajo, valto])
#         r[21]=np.min([halto, smedio, vbajo])
#         r[22]=np.min([halto, smedio, vmedio])
#         r[23]=np.min([halto, smedio, valto])
#         r[24]=np.min([halto, salto, vbajo])
#         r[25]=np.min([halto, salto, vmedio])
#         r[26]=np.min([halto, salto, valto])
        
#         # #implicacion difusa
#         R0=np.minimum(r[0],no_piel)
#         R1=np.minimum(r[1],no_piel)
#         R2=np.minimum(r[2],no_piel)
#         R3=np.minimum(r[3],no_piel)
#         R4=np.minimum(r[4],no_piel)
#         R5=np.minimum(r[5],piel) # regla que implica piel cuan h:bajo s: medio v:alto
#         R6=np.minimum(r[6],no_piel)
#         R7=np.minimum(r[7],no_piel)
#         R8=np.minimum(r[8],no_piel)
#         R9=np.minimum(r[9],no_piel)
#         R10=np.minimum(r[10],no_piel)
#         R11=np.minimum(r[11],no_piel)
#         R12=np.minimum(r[12],no_piel)
#         R13=np.minimum(r[13],no_piel)
#         R14=np.minimum(r[14],no_piel)
#         R15=np.minimum(r[15],no_piel)
#         R16=np.minimum(r[16],no_piel)
#         R17=np.minimum(r[17],no_piel)
#         R18=np.minimum(r[18],no_piel)
#         R19=np.minimum(r[19],no_piel)
#         R20=np.minimum(r[20],no_piel)
#         R21=np.minimum(r[21],no_piel)
#         R22=np.minimum(r[22],no_piel)
#         R23=np.minimum(r[23],no_piel)
#         R24=np.minimum(r[24],no_piel)
#         R25=np.minimum(r[25],no_piel)
#         R26=np.minimum(r[26],no_piel)
#         salida=np.max([R0,R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12,R13,R14,R15,R16,R17,R18,R19,R20,R21,R22,R23,R24,R25,R26],axis=0)
#         Real=defuzzy(np.linspace(0.0,1.0,200),salida) #(rango de salida, salida que se mandara)
#         if(Real<0.5):
#             binario[i,j]=1
        












