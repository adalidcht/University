# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:46:41 2022

@author: adalc
"""
#Adaline OR

import numpy as np
import matplotlib.pyplot as plt

#Establecimiento de arquitectura
P = np.array([[0,0],[0,1],[1,0],[1,1]])
T = np.array([-1,1,1,1])
wt = np.random.rand(1,2)
b = np.random.rand(1,1)
Epoca = 10000


R = 0 #Correlación
for i in range(len(P)):
    R = R + 0.25*np.outer(P[i],np.transpose(P[i]))
    print('Correlación\n',R)

eigenvalor,vector = np.linalg.eig(R)
landamax = max(eigenvalor)
alpha = 1/(4*landamax)*0.99
    
for j in range(Epoca): #Entrenamiento
    for i in range(len(P)):
        a = np.dot(wt,P[i]) + b
        e = np.float64(T[i]-a) #Error
        wt = wt + alpha*(np.dot(e,P[i]))
        b = b + alpha*e


print('Matriz de pesos\n',wt)
print('Matriz de polarización\n',b)

intx = np.float64(-b/wt[0][0])
inty = np.float64(-b/wt[0][1])

m = (-inty)/(intx)
x = np.arange(-2,2,0.01)
y = m*x + inty
w = plt.axes()

#Gráficas
plt.figure(1)
for i in range(len(P)):
    if i < 1:
        plt.plot(np.int0(P[i][0]),np.int0(P[i][1]),marker = "o",color = "blue")
    else:
        plt.plot(np.int0(P[i][0]),np.int0(P[i][1]),marker = "o",color = "orange")
        
plt.xlim(-2.5,2.5)
plt.ylim(-2.5,2.5)
w.arrow(0,0,wt[0][0],wt[0][1],head_width = 0.2, head_length = 0.2, color = "red")
plt.plot(x,y)
plt.title('Entrenamiento adaline compuerta OR')
plt.grid(True)