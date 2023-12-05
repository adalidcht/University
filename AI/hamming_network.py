# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 09:22:13 2023

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt

def poslin(n):
    a = np.where(n <= 0,0,n)
    return a

def hardlim(n):
    if (n > 0):
        a = 1
    else:
        a = 0
    return a



alpha = 0.1

p1 = np.array([-0.1961,0.9806])
p2 = np.array([0.1961,0.9806])
p3 = np.array([0.9806,0.1961])
p4 = np.array([0.9806,-0.1961])
p5 = np.array([-0.5812,-0.8137])
p6 = np.array([-0.8137,-0.5812])
patrones = np.array([p1,p2,p3,p4,p5,p6])

w1 = np.array([0.7071,-7071])
w2 = np.array([0.7071,0.7071])
w3 = np.array([-1,0])
pesos1 = np.array([w1,w2,w3])
pesos2 = np.array([[1,-0.2,-0.2],[-0.2,1,-0.2],[-0.2,-0.2,1]]) #-epsilon es la parte inhibitoria | 1/(s-1) s = neuronas

bias = np.zeros((3,1))

plt.close('all')
plt.ion() # Enable interactive mode.

ax = plt.axes()

for i in range(patrones.shape[0]):
    ax.arrow(0,0,patrones[i,0],patrones[i,1],head_width = 0.05,head_length = 0.1,color = 'b')
for i in range(pesos1.shape[0]):
    ax.arrow(0,0,pesos1[i,0],pesos1[i,1],head_width = 0.05,head_length = 0.1,color = 'r')


plt.plot(0,0,'ok')
plt.axis('equal')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.grid(visible = True)


for epocas in range(20):
    for i in range(patrones.shape[0]):
        a1 = pesos1.dot(patrones[i,:].T)
        a21 = a1 #a2,tiempo1 | entra por primera vez a recursividad, solo es la salida
        a22 = poslin(pesos2.dot(a21)) #Segunda recursividad
        a23 = poslin(pesos2.dot(a22)) #Tercera recursividad
        a24 = poslin(pesos2.dot(a23))
        
        pesos1[0,:] = pesos1[0,:] + alpha*(a24[0])*(patrones[i,:] - pesos1[0,:])
        pesos1[0,:] = pesos1[1,:] + alpha*(a24[1])*(patrones[i,:] - pesos1[1,:])
        pesos1[0,:] = pesos1[2,:] + alpha*(a24[2])*(patrones[i,:] - pesos1[2,:])


        plt.cla() #clear axes
        plt.plot(0,0,'ok')
        plt.axis('equal')
        plt.xlim([-2,2])
        plt.ylim([-2,2])
        plt.grid(visible = True)
        
                
        for i in range(patrones.shape[0]):
            ax.arrow(0,0,patrones[i,0],patrones[i,1],head_width = 0.05,head_length = 0.1,color = 'b')
        
        for i in range(pesos1.shape[0]):
            ax.arrow(0,0,pesos1[i,0],pesos1[i,1],head_width = 0.05,head_length = 0.1,color = 'r')
        plt.pause(0.15)
                

























