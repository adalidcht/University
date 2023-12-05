# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 16:51:47 2022

@author: Saul
"""

import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm

plt.close('all')

x1 = np.arange(0,20,0.1)
x2= np.arange(0,20,0.1)
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
def trapezoidal(x,a,b,c,d):
    #A,bb,c,d Puntos del vertice en orden del trapecio
    tra = []
    for i in range(len(x)):
        if x[i] <= a:
            tra.append(0)
        if a < x[i] <= b:
            tra.append((x[i] - a)/(b - a))
        if b < x[i] <= c:
            tra.append(1)
        if c < x[i] <= d:
            tra.append((d - x[i])/(d - c))
        if d < x[i]:
            tra.append(0)
    return tra
triang=triangular(x1,3,6,9)
plt.figure()
plt.plot(x1,triang)
plt.grid()
y1=x2

trap=trapezoidal(x2,10,12,16,18)
plt.figure()
plt.plot(x2,trap)
plt.grid()
y2=x1



fig = plt.figure()
ax = plt.axes(projection='3d')
x1, y1 = np.meshgrid(x1, y1)
z1=triang +y1*0
x2, y2 = np.meshgrid(x2, y2)
z2=trap +y2*0
z2=z2.T
ax.plot_surface(x1, y1, z1, cmap=cm.hot,linewidth=0)
ax.plot_surface(x1,y1, z2, cmap=cm.cool,linewidth=0)

prodcart=np.minimum(z1,z2)

# prodcart=x1@y1
# for i in range(len(x1)):
#     for j in range(len(y1)):
#         prodcart[i,j]=np.minimum(z1[i,j],z2[i,j])
                
fig = plt.figure()

ax = plt.axes(projection='3d')

ax.plot_surface(x1, y1, prodcart, cmap=cm.hot,linewidth=0)

