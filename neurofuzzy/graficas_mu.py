# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:46:27 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

#Ejercicio 3

x = np.arange(0,10,0.1)

mu_a = x/(x+2)
mu_b = 2**(-x)
mu_c = 1/(1+10*(x-2)**2)

plt.figure()
plt.plot(x,mu_a/max(mu_a))
plt.plot(x,mu_b)
plt.plot(x,mu_c)
plt.title('Funciones originales')

#Complementos
plt.figure()
plt.plot(x,1-(mu_a/max(mu_a)))
plt.plot(x,1-mu_b)
plt.plot(x,1-mu_c)
plt.title('Complementos')

#Uniones
#AuB
a_new = mu_a/max(mu_a)
aub = []
for i in range(len(mu_a)):
    aub.append(max(a_new[i],mu_b[i]))
    
plt.figure()
plt.plot(x,aub)
plt.ylim([0,1])
plt.title(r'A$\cup$B')

#AuC
auc = []
for i in range(len(mu_a)):
    auc.append(max(a_new[i],mu_c[i]))
    
plt.figure()
plt.plot(x,auc)
plt.ylim([0,1])
plt.title(r'A$\cup$C')

#BuC
buc = []
for i in range(len(mu_b)):
    buc.append(max(mu_b[i],mu_c[i]))
    
plt.figure()
plt.plot(x,buc)
plt.ylim([0,1])
plt.title(r'B$\cup$C')

#Intersección
#AnB
anb = []
for i in range(len(mu_a)):
    anb.append(min(a_new[i],mu_b[i]))
    
plt.figure()
plt.plot(x,anb)
plt.ylim([0,1])
plt.title(r'A$\cap$B')

#AnC
anc = []
for i in range(len(mu_a)):
    anc.append(min(a_new[i],mu_c[i]))
    
plt.figure()
plt.plot(x,anc)
plt.ylim([0,1])
plt.title(r'A$\cap$C')

#BnC
bnc = []
for i in range(len(mu_b)):
    bnc.append(min(mu_b[i],mu_c[i]))
    
plt.figure()
plt.plot(x,bnc)
plt.ylim([0,1])
plt.title(r'B$\cap$C')

#Complementos 
#(AnC')'
anc_c = []
for i in range(len(mu_a)):
    anc_c.append(min(a_new[i],1-mu_c[i]))   
    
plt.figure()
plt.plot(x,1-np.array(anc_c))
plt.ylim([0,1])
plt.title(r'$\overline{A\cap\overline{B}}$')

#(B'nC)'
bnc_c = []
for i in range(len(mu_a)):
    bnc_c.append(min(1-mu_b[i],mu_c[i]))   
    
plt.figure()
plt.plot(x,1-np.array(bnc_c))
plt.ylim([0,1])
plt.title(r'$\overline{\overline{B}\cap C}$')

#(AnC)'
plt.figure()
plt.plot(x,1-np.array(auc))
plt.ylim([0,1])
plt.title(r'$\overline{A\cap C}$')


#Arreglo de imagenes
fig,ax = plt.subplots(2)
ax[0].plot(x,mu_a/max(mu_a))
ax[0].plot(x,mu_b)
ax[0].plot(x,mu_c)
ax[0].set_title('Funciones originales')

ax[1].plot(x,1-(mu_a/max(mu_a)))
ax[1].plot(x,1-mu_b)
ax[1].plot(x,1-mu_c)
ax[1].set_title('Complementos')

fig,ax = plt.subplots(1,3)
fig.suptitle('Uniones')
ax[0].plot(x,aub)
ax[0].set_ylim([0,1])
ax[0].set_title(r'A$\cup$B')

ax[1].plot(x,auc)
ax[1].set_ylim([0,1])
ax[1].set_title(r'A$\cup$C')

ax[2].plot(x,buc)
ax[2].set_ylim([0,1])
ax[2].set_title(r'B$\cup$C')

fig,ax = plt.subplots(1,3)
fig.suptitle('Intersecciones')
ax[0].plot(x,anb)
ax[0].set_ylim([0,1])
ax[0].set_title(r'A$\cap$B')

ax[1].plot(x,anc)
ax[1].set_ylim([0,1])
ax[1].set_title(r'A$\cap$C')

ax[2].plot(x,bnc)
ax[2].set_ylim([0,1])
ax[2].set_title(r'B$\cap$C')


fig,ax = plt.subplots(1,3)
fig.suptitle('Complementos')
ax[0].plot(x,1-np.array(anc_c))
ax[0].set_ylim([0,1])
ax[0].set_title(r'$\overline{A\cap\overline{B}}$')

ax[1].plot(x,1-np.array(bnc_c))
ax[1].set_ylim([0,1])
ax[1].set_title(r'$\overline{\overline{B}\cap C}$')

ax[2].plot(x,1-np.array(auc))
ax[2].set_ylim([0,1])
ax[2].set_title(r'$\overline{A\cap C}$')

#Ejericio 2

T = np.array([0,0.3,0.7,0.8,0.9,1])
R = np.array([0,0.2,0.4,0.6,0.8,1])

union = np.maximum(T,R)
interseccion = np.minimum(T,R)
complemento_t = 1 - T
complemento_r = 1 - R
complemento_tr = 1 - union

plt.figure()
plt.plot(T,label = 'T')
plt.plot(R,label = 'R')
plt.plot(union,label = 'Unión')
plt.plot(interseccion,label = 'Intersección')
plt.plot(complemento_t,label = 'Complemento T')
plt.plot(complemento_r,label = 'Complemento R')
plt.plot(complemento_tr,label = 'Complemento TR')

plt.legend()