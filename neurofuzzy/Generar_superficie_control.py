# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 15:43:28 2022

@author: cinth
"""
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
plt.close('all')

x_=np.linspace(0,100)
y_=np.linspace(0,100)
z_=np.linspace(0,100)

def A1(x):
    a1=1/(1+np.exp(0.3*(x-50)))
    return a1

def A2(x):
    a2=1/(1+np.exp(-0.3*(x-50)))
    return a2

def B1(y):
    b1=np.exp((-1/2)*((y-25)/20)**2)
    return b1

def B2(y):
    b2=np.exp((-1/2)*((y-75)/20)**2)
    return b2

def C1(z):
    c1=1/(1+np.exp(0.3*(z-50)))
    return c1
def C2(z):
    c2=np.exp((-1/2)*((z-75)/20)**2)
    return c2
    
plt.figure()
plt.plot(x_,A1(x_))
plt.plot(x_,A2(x_))
plt.legend(['A1','A2'])
plt.figure()
plt.plot(y_,B1(y_))
plt.plot(y_,B2(y_))
plt.legend(['B1','B2'])
plt.figure()
plt.plot(z_,C1(z_))
plt.plot(z_,C2(z_))
plt.legend(['C1','C2'])

# xx_=60
# yy_=35
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

ejex=[]
ejey=[]
ejez=[]
for xx_ in range(0,100,1):  
    for yy_ in range(0,100,1):
        
        muA1=A1(xx_)
        muA2=A2(xx_)
        muB1=B1(yy_)
        muB2=B2(yy_)
        
        agC1=np.maximum(np.minimum(muA1,muB1),np.minimum(muA1,muB2))
        agC2=np.maximum(np.minimum(muA2,muB1),np.minimum(muA2,muB2))
        
        C1rec=np.minimum(C1(z_),agC1)   #minimum para recortar
        C2rec=np.minimum(C2(z_),agC2)
        
        CT=np.maximum(C1rec,C2rec) #union es maximum, interseccion minimum
        SalZ=sum(CT*z_)/sum(CT) #Ecuacion 1
        ejex.append(xx_)
        ejey.append(yy_)
        ejez.append(SalZ)
ax.scatter(ejex,ejey,ejez,cmap='viridis')
plt.title('Superficie de Control Resultante')
plt.xlabel('X')
plt.ylabel('Y')

plt.figure()
plt.plot(z_,C1rec) 
plt.plot(z_,C2rec)
plt.legend(['agregacion C1','agregacion C2'])
plt.xlabel('Z')
plt.ylabel('Membresía')

plt.figure()
plt.plot(z_,CT)
plt.xlabel('Z')
plt.ylabel('Membresía')
plt.legend([' CT '])