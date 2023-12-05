# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 08:40:59 2023

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
alpha = 0.1

 

P1 = np.array([-0.1961, -0.7806]) #([-0.1961, 0.9806])
P2 = np.array([-0.1961, 0.9806])
P3 = np.array([ 0.9806, 0.1961])
P4 = np.array([ 0.9806,-0.1961])
P5 = np.array([-0.5812,-0.8137])
P6 = np.array([-0.8137,-0.5812])
Patrones = np.array([P1, P2, P3, P4, P5, P6])
 

W1 = np.array([0.17071,-0.17071])
W2 = np.array([0.17071, 0.17071])
W3 = np.array([-0.17071, 0.07071])
Pesos1 = np.array([W1, W2, W3])
Pesos2 = np.array([[1, -0.2, -0.2], [-0.2, 1, -0.2], [-0.2, -0.2, 1]]) #1/(s-1) s = neuronas
# Bias = np.array([[2], [2],[2]])
Bias = np.zeros((3, 1))

 

plt.close('all')
plt.ion()
ax = plt.axes()
for i in range (Patrones.shape[0]):
    ax.arrow(0,0,Patrones[i,0],Patrones[i,1],head_width=0.05,head_length=0.1,color = 'b')
for i in range (Pesos1.shape[0]):
    ax.arrow(0,0,Pesos1[i,0],Pesos1[i,1],head_width=0.05,head_length=0.1,color = 'r')


plt.plot(0,0,'ok')
plt.axis('equal')
plt.xlim([-2, 2])
plt.ylim([-2, 2])
#plt.grid(b = True, which = 'major')


for epocas in range(30):
    for i in range (Patrones.shape[0]):
        a1 = Pesos1.dot(Patrones[i,:].T)
        # a21 = a1.T #Recursividad
        # a22 = poslin(Pesos2.dot(a21)) 
        # a23 = poslin(Pesos2.dot(a22))
        # a24 = poslin(Pesos2.dot(a23))
        # a25 = poslin(Pesos2.dot(a24))
        # a26 = poslin(Pesos2.dot(a25))
        # Pesos1[0,:] = Pesos1[0,:] + alpha*(a26[0])*(Patrones[i,:]-Pesos1[0,:])
        # Pesos1[1,:] = Pesos1[1,:] + alpha*(a26[1])*(Patrones[i,:]-Pesos1[1,:])
        # Pesos1[2,:] = Pesos1[2,:] + alpha*(a26[2])*(Patrones[i,:]-Pesos1[2,:])
        #Compet
        a26 = compet(a1)
        g1 = np.argmax(a26) #peso ganador
        Pesos1[g1,:] = Pesos1[g1,:] + alpha*(Patrones[i,:]-Pesos1[g1,:]) #se actualiza la w asociada a g1
        
        
        plt.cla()
        plt.plot(0,0,'ok')
        plt.axis('equal')
        plt.xlim([-2, 2])
        plt.ylim([-2, 2])
        #plt.grid(b = True, which = 'major')
        for i in range (Patrones.shape[0]):
            ax.arrow(0,0,Patrones[i,0],Patrones[i,1],head_width=0.05,head_length=0.1,color = 'b')
        for i in range (Pesos1.shape[0]):
            ax.arrow(0,0,Pesos1[i,0],Pesos1[i,1],head_width=0.05,head_length=0.1,color = 'r')
        plt.pause(0.15)

plt.show()





