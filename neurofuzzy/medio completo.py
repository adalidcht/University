# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 10:18:26 2022

@author: Saul
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
p = np.array(([3,1,-1],[-2,-2,2],[-3,-1,1]))

t = np.array(([1],[-1],[-1]))

w = np.random.rand(3)
origen=np.zeros(3)
b = np.random.rand(1)

epoca = 10

for i in range(epoca):
    for j in range(len(p)):
        n = np.dot(np.transpose(w),p[j])+b
        if n<0:
            a=-1
        else:
            a=1
        e = t[j] - a
        w = w + p[j]*e
        b = b + e
        
print(w)
print(b)

intx = (-b)/w[0]
inty = (-b)/w[1]
intz = (-b)/w[2]

x = np.linspace(0,6,1)
y = np.linspace(0,6,1)
z = np.linspace(0,6,1)

u = x*intx+y*inty+z*intz-b


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.set_xlim3d(-4, 4)
ax.set_ylim3d(-4, 4)
ax.set_zlim3d(-4, 4)
ax.scatter(3,1,-1, color="red")
ax.scatter(-2,-2,2,color="yellow")
ax.scatter(-3,-1,1, color="yellow")


xx,yy=np.meshgrid(range(-4, 4),range(-4, 4))
# z1=(b-xx*intx-yy*inty)/intz
z1=(1-xx/intx-yy/inty)*intz

#z1=(1-xx/w[0]-yy/w[1])*w[2]

ax.plot([0,w[0]],[0,w[1]],[0,w[2]], color="blue")

ax.plot_surface(xx,yy,z1, alpha=0.5, color="red")

plt.show()
