# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:39:54 2022

@author: adalc
"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, pi



plt.close('all')

p = np.array(([[0,0],[0,1],[1,0],[1,1]])).T
T = np.array(([0,1,1,0]))



W1 = np.random.rand(2,2)
b1 = np.random.rand(2,1)

W2 = np.random.rand(1,2)
b2 = np.random.rand(1,1)

alpha = 0.1
Epoca = 5000

salida = np.array([])
aprendizaje = []

for i in range(Epoca):
    suma = 0
    for j in range(np.shape(p)[1]):
        #Forward propagation
        print(i)
        print(j)
        a0 = p[:,j]
        n1 = W1.dot(a0)[:,np.newaxis] + b1
        a1 = 1/(1+np.exp(-n1)) 
        
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
        aprendizaje.append(e2)
        

salida = np.zeros(np.shape(p)[1])

for ii in range(np.shape(p)[1]):
    a0 = p[:,ii]
    n1 = W1.dot(a0)[:,np.newaxis] + b1
    a1 = 1/(1+np.exp(-n1))
    n2 = W2.dot(a1) + b2
    salida[ii] = n2
    
    
plt.figure()
plt.plot(p,'o')
# plt.figure()
# plt.plot(salida)
# plt.grid()

plt.figure()
plt.plot(np.arange(0,Epoca*np.shape(p)[1]),aprendizaje)

 


