# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:04:33 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt


#Funciones

def gauss(x,c,sigma):
    #x = vector valores, c = centro
    g = np.exp(-(1/2)*((x-c)/sigma)**2)
    return g

def campana(x,a,b,c):
    #a = ancho, b = usualmente positivo
    camp = 1/(1+abs(((x-c)/a))**(2*b))
    return camp

def sigmoide(x,a,c,n):
    #a = razón de cambio de la pendiente
    #n = orientacion, [+] S, [-] Z
    sig = 1/(1+np.exp(-n*(x-c)))
    return sig

def triangular(x,a,b,c):
    #a = inicio triangulo
    #b = centro
    #c = termino triangulo
    tr = []
    for i in range(len(x)):
        if x[i] <= a:
            tr.append(0)
        if a < x[i] <= b:
            tr.append((x[i] - a)/(b - a))
        if b < x[i] <= c:
            tr.append((c - x[i])/(c - b))
        if c < x[i]:
            tr.append(0)
    return np.array(tr)
def trapezoidal(x,a,b,c,d):
    #A,bb,c,d Puntos del vertice en orden del trapecio
    tra = []
    for i in range(len(x)):
        if x[i] <= a:
            tra.append(0)
        if a < x[i] <= b:
            tra.append((x[i] - a)/(b - a))
        if b < x[i] <= c:
            tra.append(1)
        if c < x[i] <= d:
            tra.append((d - x[i])/(d - c))
        if d < x[i]:
            tra.append(0)
    return tra
        

plt.close('all')

x = np.arange(0,10,0.1)

plt.figure()
plt.plot(x,gauss(x,2,0.6))
plt.plot(x,campana(x,2,3,5))
plt.plot(x,sigmoide(x,3,8,4)) 
# plt.plot(x,sigmoide(x,3,8,-4)) #Función Z
plt.grid()

plt.figure()
plt.plot(x,triangular(x,1,3,5))
plt.plot(x,trapezoidal(x,4,6,7,9))
plt.grid()
