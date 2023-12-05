# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 09:07:55 2022

@author: adalc
"""

import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.proj3d import proj_transform
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.patches import FancyArrowPatch

#Funciones
def hardlimitS(value):
    if value < 0:
        value = -1
    else:
        value = 1
    return value 

#FUNCION GRAFICA PLANO 3D
def plano3d(intx,inty, intz):
    puntos = [[ float(intx), 0 , 0 ],
              [ 0 ,  float(inty), 0], 
              [ 0 , 0 , float(intz)]]
    punto0,punto1,punto2 = puntos 
    
    Ax,Ay,Az = punto0
    Bx,By,Bz = punto1
    Cx,Cy,Cz = punto2
    
    ABx,ABy,ABz = [Bx-Ax,By-Ay,Bz-Az]
    ACx,ACy,ACz = [Cx-Ax,Cy-Ay,Cz-Az]
    ABcruzAC = [ABy*ACz - ABz*ACy,ABz*ACx - ABx*ACz,ABx*ACy - ABy*ACx]
    
    punto = np.array(punto0)
    vectorNormal = np.array(ABcruzAC) 
    d = -punto.dot(vectorNormal)
    
    xx,yy = np.meshgrid(range(3,10),range(1,10))
    z = (-vectorNormal[0]*xx - vectorNormal[1]*yy-d)*1./vectorNormal[2]
    return xx,yy,z

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

plt.close("all")

P = np.loadtxt('IrisDataBase.txt',usecols = (0,1,2)) # Definiendo variables 
#print(P)
# Creamos la figura
fig = plt.figure()
# Creamos el plano 3D
ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(P[0:49,0], P[0:49,1],P[0:49,2], c = 'b', marker = 'o')
ax1.scatter(P[50:99,0], P[50:99,1],P[50:99,2], c = 'g', marker = 'o')
ax1.scatter(P[100:149,0], P[100:149,1],P[100:149,2], c = 'k', marker = 'o')
plt.show()

#Target
T = []
for i in range(0,50,1):
    T.append(np.array([0,0]))
for i in range(50,100,1):
    T.append(np.array([1,0]))
for i in range(100,150,1):
    T.append(np.array([0,1]))
    
#variiables adaptativas
W = np.random.rand(2,3)
b = np.random.rand(1,2)

Epoca = 5000
a = np.array([0,0])

#Entrenamiento
for i in range(Epoca):
    for j in range(len(P)):
        n = np.dot(W,np.transpose(P[j])) + b
        for k in [0,1]:
                if n[:,k] < 0:
                    a = 0
                else:
                    a = 1
        e = T[j]-a #Error
        W = W + np.outer(e,(P[j]))
        b = b + e
        
intx1 = (-b[0,0])/W[0,0]
inty1 = (-b[0,0])/W[0,1]
intz1 = (-b[0,0])/W[0,2]

intx2 = (-b[0,1])/W[1,0]
inty2 = (-b[0,1])/W[1,1]
intz2 = (-b[0,1])/W[1,2]


#Gráficas

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
ax1.scatter(P[0:49,0], P[0:49,1],P[0:49,2], c = 'b', marker = 'o')
ax1.scatter(P[50:99,0], P[50:99,1],P[50:99,2], c = 'g', marker = 'o')
ax1.scatter(P[100:149,0], P[100:149,1],P[100:149,2], c = 'k', marker = 'o')

xx,yy = np.meshgrid(range(3,10),range(1,6))

z1 = (1 - xx/intx1 - yy/inty1)*intz1
z2 = (1 - xx/intx2 - yy/inty2)*intz2
# ax.plot([0,W[0,0]],[0,W[0,1]],[0,W[0,2]], color = 'red')
ax1.plot_surface(xx,yy,z1,alpha = 0.5,color = 'skyblue')
ax1.plot_surface(xx,yy,z2,alpha = 0.5,color = 'mediumorchid')

ax1.arrow3D(7,5,4,
            W[0,0],W[0,1],W[0,2],
            mutation_scale = 20,
            fc = 'skyblue')

ax1.arrow3D(7,5,4,
            W[1,0],W[1,1],W[1,2],
            mutation_scale = 20,
            fc='mediumorchid')

ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

plt.title('Práctica 1.3')
# plt.grid(True)