# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 18:53:35 2022

@author: adalc
"""
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm

plt.close('all')

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

x = np.arange(-15,16,1)
x1 = np.arange(0,16,1)
A = 1/(1+((x + 5)/7.5)**4)
B = triangular(x1,4,8,11)

plt.figure()
plt.plot(x,A,label = 'A')
plt.plot(x1,B,label = 'B')
plt.title('Conjuntos')
plt.legend()


#Extensión cilíndrica BxA
ext = np.zeros((len(B),len(A)))
for k in range(len(A)):
    for i in range(len(B)):
        ext[i,k] = A[k]

xx, yy = np.meshgrid(x,x1)

plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(xx,yy,ext,cmap = cm.hot,linewidth = 0)
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('Z')
plt.title('Extensión cilíndrica BxA')

#Extensión cilíndrica AxB
ext1 = np.zeros((len(A),len(B)))
for k in range(len(B)):
    for i in range(len(A)):
        ext1[i,k] = B[k]

xx1, yy1 = np.meshgrid(x1,x)

plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(xx1,yy1,ext1,cmap = cm.cool,linewidth = 0)
ax.set_xlabel('B')
ax.set_ylabel('A')
ax.set_zlabel('Z')
plt.title('Extensión cilíndrica AxB')

prod_cart = np.minimum(ext,ext1.T)
plt.figure()
ax = plt.axes(projection = '3d')
ax.plot_surface(xx,yy,prod_cart,cmap = cm.hot,linewidth = 0)
ax.set_xlabel('A')
ax.set_ylabel('B')
ax.set_zlabel('Z')
plt.title('Producto cartesiano')
    



