# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:22:46 2023

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
#=================================================================#
def hardLim(n):
    if (n > 0):
        a = 1
    else:
        a = 0
    return a
def purelin(n):
    a = 1 * n
    return a
def poslin(n):
    a = np.where(n <= 0, 0, n)
    return a
def compet(n):
    a = np.where(np.max(n) == n, 1, 0)
    return a
#=================================================================#
alpha = 0.5
P1 = np.array([-1, -1])
P2 = np.array([ 1,  1])
P3 = np.array([ 1, -1])
P4 = np.array([-1,  1])
t1 = np.array([1, 0])
t2 = np.array([1, 0])
t3 = np.array([1, 0])
t4 = np.array([1, 0])

Patrones = np.array([P1, P2, P3, P4])
Target   = np.array([t1, t2, t3, t4])
Pesos1 = np.array([[-0.543, -0.969, 0.997, 0.456],[0.840, -0.249, 0.094, 0.954]])
Pesos2 = np.array([[1, 1, 0, 0], [0, 0, 1, 1]])
plt.close('all')
plt.plot(0,0,'ok')
plt.axis('equal')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.grid(b = True, which = 'major')
plt.ion()
ax = plt.axes()

for i in range (Patrones.shape[0]):
    ax.arrow(0,0,Patrones[i,0],Patrones[i,1],head_width=0.05,head_length=0.1,color = 'b')
for i in range (Pesos1.shape[1]):
    ax.arrow(0,0,Pesos1[0,i],Pesos1[1,i],head_width=0.05,head_length=0.1,color = 'r')
a1 = np.zeros(Patrones.shape[0])
for epocas in range(10):
    for i in range (Patrones.shape[0]):
        vectorP = Patrones[i, :]
        d = 0
        
        #Aprendizaje
        for n in range(2):
            d = d + (vectorP[n]-Pesos1[n, :])**2
        dista = np.sqrt(d)
        ind = np.argmin(dista)
        
        a1 = np.where(np.min(dista) == dista, 1, 0)
        print(a1)
        
        vectorW = Pesos1[:, ind] + alpha*(vectorP - Pesos1[:, ind])
        Pesos1[:,ind] = vectorW
        
        a2 = Pesos2@a1
        print(a2)
        
        plt.cla()
        plt.plot(0,0,'ok')
        plt.axis('equal')
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        plt.grid(b = True, which = 'major')
        for i in range (Patrones.shape[0]):
            ax.arrow(0,0,Patrones[i,0],Patrones[i,1],head_width=0.05,head_length=0.1,color = 'b')
        for i in range (Pesos1.shape[1]):
            ax.arrow(0,0,Pesos1[0,i],Pesos1[1,i],head_width=0.05,head_length=0.1,color = 'r')
        
        plt.pause(0.5)
        
        
        
        
        
        
        
        