# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 08:46:41 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt

#Establecimiento de arquitectura
P = np.array([[0,0],[0,1],[1,0],[1,1]])
T = np.array([0,1,1,1])
wt = np.random.rand(2)
b = np.random.rand(1)
Epoca = 10000

for j in range(Epoca): #Entrenamiento
    for i in range(len(P)):
        n = np.dot(wt,P[i]) + b
        if n < 0:
            a = 0
        else:
            a = 1
        e = T[i]-a #Error
        wt = wt + np.dot(e,(P[i]))
        b = b + e
        
print(wt)
print(b)

intx = -b/wt[0]
inty = -b/wt[1]

m = (inty - 0)/(0 - intx)
x = np.arange(-0.5,1,0.01)
y = m*x + inty
w = plt.axes()

#Gráficas
plt.figure(1)
for i in range(len(P)):
    if i < 1:
        plt.plot(np.int0(P[i][0]),np.int0(P[i][1]),marker = "o",color = "blue")
    else:
        plt.plot(np.int0(P[i][0]),np.int0(P[i][1]),marker = "o",color = "orange")
        
w.arrow(0,0,0.1,0.1,head_width = 0.1, head_length = 0.1, color = "red")
plt.plot(x,y)
# plt.xlim(-2,2)
# plt.ylim(-2,2)
plt.title('Entrenamiento perceptron compuerta OR')
plt.legend(bbox_to_anchor = (0.9,1),loc = 'upper left', borderaxespad = 0)
plt.grid(True)