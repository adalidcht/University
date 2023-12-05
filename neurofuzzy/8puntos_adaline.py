# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:33:26 2022

@author: adalc
"""

#Adaline 8 puntos
import numpy as np
import matplotlib.pyplot as plt

#Establecimiento de arquitectura
P = np.array([[-2,0],[0,1],[0,-1],[3,2],[4,1],[4,3],[4,-2],[3,-3]])
T = np.array([[1,1],[1,1],[1,1],[-1,1],[-1,1],[-1,1],[-1,-1],[-1,-1]])
W = np.random.rand(2,2)
b = np.random.rand(2)
Epoca = 10000
a = ([0,0])

R = 0 #Correlación
for i in range(len(P)):
    R = R + 0.25*np.outer(P[i],np.transpose(P[i]))
    print('Correlación\n',R)

eigenvalor,vector = np.linalg.eig(R)
landamax = max(eigenvalor)
alpha = 1/(4*landamax)*0.99

for j in range(Epoca): #Entrenamiento
    for i in range(len(P)):
        a = np.dot(W,np.transpose(P[i])) + b
        e = T[i]-a #Error
        W = W + alpha*(np.outer(e,P[i]))
        b = b + alpha*e

intx = -b[0]/W[0,0]
inty = -b[0]/W[0,1]
intx1 = -b[1]/W[1,0]
inty1 = -b[1]/W[1,1]

m = (inty - 0)/(0 - intx)
x = np.arange(-6,6,0.01)
y = m*x + inty
m1 = (inty1 - 0)/(0 - intx1)
y1 = m1*x + inty1
w = plt.axes()

print(-inty/m)
print(-inty1/m1)

print('Matriz de pesos\n',W)
print('Matriz de polarización\n',b)

#Gráficas
plt.figure(1)
for i in range(len(P)):
    if i < 3:
        plt.plot(np.int0(P[i][0]),np.int0(P[i][1]),marker = "o",color = "blue")
    elif i > 5 :
        plt.plot(np.int0(P[i][0]),np.int0(P[i][1]),marker = "o",color = "green")
    else:
        plt.plot(np.int0(P[i][0]),np.int0(P[i][1]),marker = "o",color = "orange")
        
w.arrow(0,0,5*W[0,0],5*W[0,1],head_width = 0.2, head_length = 0.2, color = "mediumorchid")
w.arrow(0,0,5*W[1,0],5*W[1,1],head_width = 0.2, head_length = 0.2, color = "darkturquoise")

plt.plot(x,y, color = 'mediumorchid')
plt.plot(x,y1, color = 'darkturquoise')
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.title('Adaline, Práctica 1.2')
# plt.grid(True)