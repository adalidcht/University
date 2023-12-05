# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:00:13 2022

@author: adalc
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi, e

plt.close('all')

p = np.arange(-2.0,2.1,0.1)

T = 1 + sin(pi/4*p)
W1 = np.array(([-0.27,-0.41]))[:, np.newaxis] #Cambiar R: SxR
b1 = np.array(([-0.48,-0.13]))[:, np.newaxis]
W2 = np.array(([0.09],[-0.17])).T
b2 = np.array(([0.48]))[:, np.newaxis]

alpha = 0.1


Epoca = 500
salida = np.array([])
aprendizaje = []
aprendizaje1 = []
#Logsigmoide 1/(1+e**(-n))
for i in range(Epoca):
    suma1 = 0
    for j in range(len(p)):
        #Forward propagation
        a0 = p[j]
        n1 = W1.dot(a0) + b1
        a1 = 1/(1+e**(-n1)) 
        
        a2 = W2@a1 + b2
        error = T[j] - a2
        
        #Back propagation
        df2 = 1
        s2 = -2*df2*error
        df1 = np.diagflat(np.multiply((1 - a1),(a1)))
        s1 = (df1.dot(W2.T)).dot(s2)
        
        #Actualización
        W2 = W2 - (alpha*s2*a1.T)
        b2 = b2 - (alpha*s2)
        W1 = W1 - (alpha*s1*a0.T)
        b1 = b1 - (alpha*s1)
        salida = np.append(salida, a2)[:, np.newaxis]
        
        e2 = float(error**2)
        aprendizaje1.append(e2)
        

salida = np.zeros(np.size(p))

for ii in range(len(p)):
    a0 = p[ii]
    n1 = W1.dot(a0) + b1
    a1 = 1/(1+e**(-n1))
    print("\n",n1)
    n2 = W2.dot(a1) + b2
    
    salida[ii] = n2
    
    
plt.figure()
plt.plot(p,T,'-o')
plt.plot(p,salida)
plt.grid()

plt.figure()
plt.plot(np.arange(0,Epoca*len(p)),aprendizaje1)
# plt.plot(aprendizaje1)
        






