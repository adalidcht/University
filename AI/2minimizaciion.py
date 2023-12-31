# -*- coding: utf-8 -*-
"""
Created on Thu May 18 09:04:26 2023

@author: Eeduardo
"""

import numpy as np
import matplotlib.pyplot as plt
#<==========================================================================>#
# Funcion Eggcrate
plt.close('all')
ax   = plt.figure().add_subplot(projection='3d')
X    = np.arange(-5,5.1,0.1)
Y    = np.arange(-5,5.1,0.1)
X, Y = np.meshgrid(X, Y)
Z    = X**2 + Y**2 + 25*(np.sin(X)**2 + np.sin(Y)**2) 
ax.plot_surface(X, Y, Z, rstride=8, cstride=8,alpha=0.9)
cset = ax.contour(X, Y, Z, zdir='z', offset=-10)
ax.set_xlabel('X')
ax.set_xlim(-5.5, 5.5)
ax.set_ylabel('Y')
ax.set_ylim(-5.5, 5.5)
ax.set_zlabel('Z')
ax.set_zlim(-10, 100)

# def funtion_obj(partiula): 
#     valor =  partiula[0]**2 + partiula[1]**2 + 25*(np.sin(partiula[0])**2 + np.sin(partiula[1])**2) 
    
#     return valor
def funtion_obj(particula): 
    valor =  -(particula[1]+47)*np.sin(np.sqrt(np.abs(particula[1]+ particula[0]/2 + 47 ))) - particula[0]*np.sin(np.sqrt(np.abs(particula[0]-(particula[1]+47))))
    
    return valor




POB = 30
var_min= -512
var_max = 512
variable  = 2

particula={'posicion': None,
           'velocidad' :None,
           'costo': None,
           'mejor.pos': None,
           'mejor.cos': np.inf
           }
mejor={'mejor.pos': None,
           'mejor.cos': np.inf
           }
##  ---------- Generar enjambre

enjambre=[]
for ii in range(POB):
    enjambre.append(particula.copy())
    enjambre[-1]['posicion'] = np.random.uniform(var_min,var_max, variable)
    enjambre[-1]['velocidad'] = np.zeros(variable)
    enjambre[-1]['costo'] = funtion_obj(enjambre[-1]['posicion'])
    
    if enjambre[-1]['costo'] < enjambre[-1]['mejor.cos']:
        enjambre[-1]['mejor.cos'] = enjambre[-1]['costo']
        enjambre[-1]['mejor.pos'] = enjambre[-1]['posicion']
        
        if enjambre[-1]['costo'] < mejor['mejor.cos']:
            mejor['mejor.cos'] = enjambre[-1]['costo']
            mejor['mejor.pos'] = enjambre[-1]['posicion']
w0 = 1 # coeficiente velocidad 
c1 = 2 # coeficiente personla
c2 = 2 # coeficeine global 


for it in range(150):
    for k in range(POB):
        enjambre[k]['velocidad'] = w0*enjambre[k]['velocidad'] + \
            c1*np.random.rand(variable)*(enjambre[k]['mejor.pos'] - enjambre[k]['posicion']) +\
                c2*np.random.rand(variable)*(mejor['mejor.pos'] - enjambre[k]['posicion']) 
        
        enjambre[k]['posicion'] = enjambre[k]['posicion'] + enjambre[k]['velocidad']
        enjambre[k]['posicion'] = np.minimum(enjambre[k]['posicion'], var_max)
        enjambre[k]['posicion'] = np.maximum(enjambre[k]['posicion'], var_min)
        
        enjambre[k]['costo'] = funtion_obj(enjambre[k]['posicion'])
        if enjambre[k]['costo'] < enjambre[k]['mejor.cos']:
            enjambre[k]['mejor.cos'] = enjambre[k]['costo']
            enjambre[k]['mejor.pos'] = enjambre[k]['posicion']
            
            if enjambre[k]['costo'] < mejor['mejor.cos']:
                mejor['mejor.cos'] = enjambre[k]['costo']
                mejor['mejor.pos'] = enjambre[k]['posicion']
        
    w0 *= 0.99
    print('iteración {} : global={:.5f}'.format(it, mejor['mejor.cos']))
  
     
    