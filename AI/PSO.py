# -*- coding: utf-8 -*-
"""
Created on Thu May 18 08:45:03 2023

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt

#<==========================================================================>#

plt.close('all')

# Funcion Eggcrate
ax = plt.figure().add_subplot(projection = '3d')
X = np.arange(-5,5.1,0.1)
Y = np.arange(-5,5.1,0.1)
X,Y = np.meshgrid(X, Y)
Z = X**2 + Y**2 + 25*(np.sin(X)**2 + np.sin(Y)**2) 
ax.plot_surface(X,Y,Z,rstride = 8,cstride = 8,alpha = 0.9)
cset = ax.contour(X, Y, Z, zdir='z', offset=-10)

ax.set_xlabel('X')
ax.set_xlim(-5.5, 5.5)
ax.set_ylabel('Y')
ax.set_ylim(-5.5, 5.5)
ax.set_zlabel('Z')
ax.set_zlim(-10, 100)



def function_obj(particula):
    valor = particula[0]**2 + particula[1]**2 + 25*(np.sin(particula[0])**2 + np.sin(particula[1])**2)
    return valor

#------PSO------

#Parámetros iniciales
pob = 3 #Población
var_min = -5
var_max = 5
variable = 2

mejor = {'posicion':None,'costo':np.inf}
particula = {'posicion': None,'velocidad':None,'costo':None,'mejor_pos':None,'mejor_costo':np.inf}

#Enjambre
enjambre = []
for ii in range(pob):
    enjambre.append(particula.copy()) #.copy las partículas son diferentes
    
    #Iniciar posiciones
    enjambre[-1]['posicion'] = np.random.uniform(var_min,var_max,variable)
    
    #iniciar velocidad
    enjambre[-1]['velocidad'] = np.zeros(variable)
    
    #iniciar costos 
    enjambre[-1]['costo'] = function_obj(enjambre[-1]['posicion']) 
    
    #Memoria de la partícula
    if enjambre[-1]['costo'] < enjambre[-1]['mejor_costo']:
        enjambre[-1]['mejor_costo'] = enjambre[-1]['costo']
        enjambre[-1]['mejor_pos'] = enjambre[-1]['posicion']
        
        #No estoy seguro
        if enjambre[-1]['costo'] < mejor['mejor_costo']:
            mejor['mejor_costo'] = enjambre[-1]['costo']
            mejor['mejor_pos'] = enjambre[-1]['posicion']
            
            
w0 = 1 # coeficiente velocidad 
c1 = 2 # coeficiente personla
c2 = 2 # coeficeine global 
            
        
for it in range(150):
    for k in range(pob):
        enjambre[k]['velocidad'] = w0*enjambre[k]['velocidad'] + \
            c1*np.random.rand(variable)*(enjambre[k]['mejor_pos'] - enjambre[k]['posicion']) +\
                c2*np.random.rand(variable)*(mejor['mejor_pos'] - enjambre[k]['posicion']) 
        
        enjambre[k]['posicion'] = enjambre[k]['posicion'] + enjambre[k]['velocidad']
        enjambre[k]['posicion'] = np.minimum(enjambre[k]['posicion'], var_max)
        enjambre[k]['posicion'] = np.maximum(enjambre[k]['posicion'], var_min)
        
        enjambre[k]['costo'] = function_obj(enjambre[k]['posicion'])
        if enjambre[k]['costo'] < enjambre[k]['mejor_costo']:
            enjambre[k]['mejor_costo'] = enjambre[k]['costo']
            enjambre[k]['mejor_pos'] = enjambre[k]['posicion']
            
            if enjambre[k]['costo'] < mejor['mejor_cos']:
                mejor['mejor_costo'] = enjambre[k]['costo']
                mejor['mejor_pos'] = enjambre[k]['posicion']
        
    w0 *= 0.99
    print('iteración {} : global={:.5f}'.format(it, mejor['mejor.cos']))
  


