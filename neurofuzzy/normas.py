# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 21:50:39 2022

@author: adalc
"""

import matplotlib.pyplot as plt 
import numpy as np 

plt.close('all')

T = np.array([0,0.3,0.7,0.8,0.9,1])
R = np.array([0,0.2,0.4,0.6,0.8,1])

x = np.arange(-15,16,1)
A = 1/(1+((x + 5)/7.5)**4)
B = 1/(1+((x - 5)/5)**2)

#T normas
t_minimo = np.minimum(T,R)
t_producto = T*R
t_frontera = np.maximum(0,T + R - 1)
t_drastico = 0
t_drastico = []
for i in range(len(T)):
    if R[i] == 1:
        t_drastico.append(T[i])
    elif T[i] == 1:
        t_drastico.append(R[i])
    else:
        t_drastico.append(0)
    
#S normas
s_maximo = np.maximum(T,R)
s_suma = T + R - (T*R)
s_frontera = np.minimum(1,T + R)
s_drastico = 0
s_drastica = []
for i in range(len(T)):
    if R[i] == 0:
        s_drastica.append(T[i])
    elif T[i] == 0:
        s_drastica.append(R[i])
    else:
        s_drastica.append(1)
        
plt.figure()
plt.plot(T,label='T')
plt.plot(R,label='R')
plt.plot(t_minimo,label='min')
plt.plot(t_producto,label='Producto algebraico')
plt.plot(t_frontera,label='Producto frontera')
plt.plot(t_drastico,label='Producto drástico')
plt.title('T-normas')

plt.figure()
plt.plot(T,label='T')
plt.plot(R,label='R')
plt.plot(s_maximo,label='max')
plt.plot(s_suma,label='Suma algebraica')
plt.plot(s_frontera,label='Suma frontera')
plt.plot(s_drastica,label='Suma drástica')
plt.title('S-normas')
plt.legend()


t_minimo = np.minimum(A,B)
t_producto = A*B
t_frontera = np.maximum(0,A + B - 1)
t_drastico = 0
t_drastico = []
for i in range(len(A)):
    if B[i] == 1:
        t_drastico.append(A[i])
    elif A[i] == 1:
        t_drastico.append(B[i])
    else:
        t_drastico.append(0)

#S normas
s_maximo = np.maximum(A,B)
s_suma = A + B - (A*B)
s_frontera = np.minimum(1,A + B)
s_drastico = 0
s_drastica = []
for i in range(len(A)):
    if B[i] == 0:
        s_drastica.append(A[i])
    elif A[i] == 0:
        s_drastica.append(B[i])
    else:
        s_drastica.append(1)


plt.figure()
plt.plot(A,label = 'A')
plt.plot(B,label = 'B')
plt.plot(t_minimo,label = 'min')
plt.plot(t_producto,label = 'Producto algebraico')
plt.plot(t_frontera,label = 'Producto frontera')
plt.plot(t_drastico,label = 'Producto drástico')
plt.title('T-normas')
plt.legend()
        
plt.figure()
plt.plot(A,label = 'A')
plt.plot(B,label = 'B')
plt.plot(s_maximo,label = 'max')
plt.plot(s_suma,label = 'Suma algebraica')
plt.plot(s_frontera,label = 'Suma frontera')
plt.plot(s_drastica,label = 'Suma drástica')
plt.title('S-normas')
plt.legend()