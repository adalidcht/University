# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:33:26 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.proj3d import proj_transform
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.patches import FancyArrowPatch

#---------------------------------
#Métodos para flecha 3D
class Arrow3D(FancyArrowPatch):

    def __init__(self, x, y, z, dx, dy, dz, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._xyz = (x, y, z)
        self._dxdydz = (dx, dy, dz)

    def draw(self, renderer):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        super().draw(renderer)
        
    def do_3d_projection(self, renderer=None):
        x1, y1, z1 = self._xyz
        dx, dy, dz = self._dxdydz
        x2, y2, z2 = (x1 + dx, y1 + dy, z1 + dz)

        xs, ys, zs = proj_transform((x1, x2), (y1, y2), (z1, z2), self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))

        return np.min(zs) 
    
def _arrow3D(ax, x, y, z, dx, dy, dz, *args, **kwargs):
    '''Add an 3d arrow to an `Axes3D` instance.'''

    arrow = Arrow3D(x, y, z, dx, dy, dz, *args, **kwargs)
    ax.add_artist(arrow)


setattr(Axes3D, 'arrow3D', _arrow3D)

#---------------------------------

#Establecimiento de arquitectura
P = np.array([[3,1,-1],[-2,-2,2],[-3,-1,1]])
T = np.array([[1],[-1],[-1]])
W = np.random.rand(3)
b = np.random.rand(1)
Epoca = 10000

#Entrenamiento
for j in range(Epoca): 
    for i in range(len(P)):
        n = np.dot(W,np.transpose(P[i])) + b
        if n < 0:
            a = -1
        else:
            a = 1
        e = T[i]-a #Error
        W = W + np.outer(e,(P[i]))
        b = b + e

intx = (-b)/W[0,0]
inty = (-b)/W[0,1]
intz = (-b)/W[0,2]

x = np.linspace(0,6,1)
y = np.linspace(0,6,1)
z = np.linspace(0,6,1)

#Gráficas
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.scatter(3,1,-1, color = 'mediumorchid')
ax.scatter(-2,-2,2,color = 'darkturquoise')
ax.scatter(-3,-1,1, color = 'darkturquoise')
    
xx,yy = np.meshgrid(range(-4, 4),range(-4, 4))
z1 = (1 - xx/intx - yy/inty)*intz
ax.plot_surface(xx,yy,z1,alpha = 0.5,color = 'skyblue')

ax.arrow3D(0,0,0,
           W[0,0],W[0,1],W[0,2],
           mutation_scale=20,
           fc='red')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.title('Práctica 1.3')
# plt.grid(True)