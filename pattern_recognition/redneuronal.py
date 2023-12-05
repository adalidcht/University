# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:30:41 2022

@author: adalc
"""

import matplotlib.pyplot as plt
import numpy as np



Patron = np.array([[0,0,1,1],[0,1,0,1]])
Target = np.array([0,1,1,0])[:,np.newaxis]


#Construcción de la arquitextura neuronal
N1 = 2 #Número de neuronas en la primera capa
W1 = np.random.rand(N1,Patron.shape[0])*2-1 #Valores aleatorios [-1,1]
B1 = np.random.rand(N1,1)*2-1

N2 = 1 #Número de neuronas en la segunda capa
W2 = np.random.rand(N2,N1)*2-1 #Valores aleatorios [-1,1] #N1 porque es la salida de la capa anterior
B2 = np.random.rand(N2,1)*2-1

#Si se requiere...
# N3 = 1 #Número de neuronas en la tercera capa
# W3 = np.random.rand(N3,N2)*2-1 #Valores aleatorios [-1,1] #N2 porque es la salida de la capa anterior
# B3 = np.random.rand(N3,1)*2-1

alpha = 0.01
et = [] #error total
for epocas in range(500):
    suma = 0
    for i in range(Patron.shape[1]):
        #Forward propagation
        P = Patron[:,i]
        P = P[:,np.newaxis]
        n1 = (W1 @ P) + B1
        a1 = 1/(1+np.exp(-n1)) #Función logsig
        n2 = (W2 @ a1) + B2
        a2 = 1*n2[0,0] #Función pureline
        
        #Back propagation
        t = Target[i]
        #t = t[:,np.newaxis]
        error = t - a2
        dF2 = 1 #derivada de pureline
        S2 = (-2)*dF2*error

        dF1 = np.diagonal((1 - a1)*a1) #Jacobiano
        S1 = dF1*W2.T*S2
        suma = (error**2) + suma #error cuadrático
        
        #Si se requiere...
        # dF3 = 1 #derivada de pureline
        # S3 = (-2)*dF3*error
        # dF2 = np.diagflat((1 - a2)*a2) #Jacobiano
        # S2 = dF2*W3.T*S3
        # dF1 = 1
        # S1 = dF1*W2.T*S2
        
        #Actualización
        W2 = W2 - (alpha*S2*a1.T)
        B2 = B2 - (alpha*S2)
        W1 = B1 - (alpha*S1*P.T)
        B1 = B1 - (alpha*S1)
    et.append(suma/Patron.shape[1]) #error cuadrático medio

plt.figure()
plt.plot(et)


for i in range(Patron.shape[1]):
    #Forward propagation
    P = Patron[:,i]
    P = P[:,np.newaxis]
    n1 = (W1 @ P) + B1
    a1 = 1/(1+np.exp(-n1)) #Función logsig
    n2 = (W2 @ a1) + B2
    a2 = 1*n2 #Función pureline
    print(a2)
    
    