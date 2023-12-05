# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 08:58:36 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

plt.close('all')

x = np.arange(0,101,1)
y = x
z = y
x_e = 60
y_e = 35

A1 = lambda x: 1/(1 + np.exp(0.3*(x - 50)))
A2 = lambda x: 1/(1 + np.exp(-0.3*(x - 50)))
B1 = lambda y: np.exp(-0.5*((y - 25)/20)**2)
B2 = lambda y: np.exp(-0.5*((y - 75)/20)**2)
C1 = lambda z: 1/(1 + np.exp(0.3*(z - 50)))
C2 = lambda z: np.exp(-0.5*((z - 75)/20)**2)

plt.figure()
plt.plot(A1(x), label = 'A1')
plt.plot(A2(x), label = 'A2')
plt.legend()

plt.figure()
plt.plot(B1(y), label = 'B1')
plt.plot(B2(y), label = 'B2')
plt.legend()

plt.figure()
plt.plot(C1(z), label = 'C1')
plt.plot(C2(z), label = 'C2')
plt.legend()
zat = np.zeros((len(x),len(y)))


# A1_B1 = min(A1(x_e),B1(y_e))
# A1_B2 = min(A1(x_e),B2(y_e))
# A2_B1 = min(A2(x_e),B1(y_e))
# A2_B2 = min(A2(x_e),B2(y_e))

# C1_ag = max(A1_B1,A1_B2)
# C2_ag = max(A2_B1,A2_B2)

# C1_sal = []
# C2_sal = []
# for i in range(len(C1(z))):
#     C1_sal.append(C1_ag if C1(z)[i] > C1_ag else C1(z)[i])
#     C2_sal.append(C2_ag if C2(z)[i] > C2_ag else C2(z)[i])

# plt.figure()
# plt.plot(C1_sal, label = 'C1 salida')
# plt.plot(C2_sal, label = 'C2 salida')
# plt.legend()

# CT = np.maximum(C1_sal,C2_sal)


# for i in range (len(CT)):
#     Sumz += CT[i]*i

# za = Sumz/sum(CT)
    

#Todo el barrido
for i in range(len(x)):
    for j in range(len(y)):
            
        A1_B1 = min(A1(x[i]),B1(y[j]))
        A1_B2 = min(A1(x[i]),B2(y[i]))
        A2_B1 = min(A2(x[i]),B1(y[i]))
        A2_B2 = min(A2(x[i]),B2(y[i]))
        
        C1_ag = max(A1_B1,A1_B2)
        C2_ag = max(A2_B1,A2_B2)
        
        C1_sal = []
        C2_sal = []
        for k in range(len(C1(z))):
            C1_sal.append(C1_ag if C1(z)[k] > C1_ag else C1(z)[k])
            C2_sal.append(C2_ag if C2(z)[k] > C2_ag else C2(z)[k])

        CT = np.maximum(C1_sal,C2_sal)
        
        Sumzt = 0
        Sumt = 0
        
        
        for m in range (len(CT)):
            Sumzt += CT[m]*m
            Sumt += CT[m]
        
        zat[i,j] = Sumzt/Sumt
      

plt.figure()
ax=plt.axes(projection= '3d')
Xm,YM=np.meshgrid(x,y)
ax.plot_surface(Xm,YM,zat,cmap='cool')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Superficie de control Mamdani')

# plt.figure()
# ax3 = plt.axes(projection = '3d')
# ax3.contour3D(Xm,Ym,ZZ,100,cmap="inferno")

# ax3.plot_surface(Xm, Ym, ZZ, cmap='Set1')
        
        
