# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 21:27:18 2022

@author: alber
"""
def Dist(a,b):
    #print(str(a)+" - "+str(b))
    return abs(a-b)

import numpy as np
senalA=np.array([-1,-0.5,0,0.5,1,2,1,2])
senalB=np.array([3,1,1,0,0.5,-0.5,-1,-2,-3])
N=len(senalA)
M=len(senalB)
#D=np.zeros([N+1,M+1])
D2=np.inf*np.ones([N+1,M+1])
D2[N,0]=0

ruta=[]
for i in range(N-1,-1,-1):
    for j in range(1,M+1):
        #D[i,j]=Dist(senalA[N-1-i],senalB[j-1])+min(D[i+1,j-1],D[i+1,j],D[i,j-1])4
        aux=np.array([D2[i+1,j-1],D2[i+1,j],D2[i,j-1]])
        minimo=min(aux)
        ruta.append(np.argmin(aux))
        D2[i,j]=Dist(senalA[N-1-i],senalB[j-1])+minimo
        #print(str(D[i-1,j-1])+","+str(D[i-1,j])+","+str(D[i,j-1]))
        #print(str(i)+","+str(j))
      
##WARPING VOLTEADO

#Dv=np.zeros([N+1,M+1])
Dv2=np.inf*np.ones([N+1,M+1])
Dv2[0,0]=0

rutav=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        #Dv[i,j]=Dist(senalA[i-1],senalB[j-1])+min(Dv[i-1,j-1],Dv[i-1,j],Dv[i,j-1])
        aux=np.array([Dv2[i-1,j-1],Dv2[i-1,j],Dv2[i,j-1]])
        minimo=min(aux)
        rutav.append(np.argmin(aux))
        Dv2[i,j]=Dist(senalA[i-1],senalB[j-1])+minimo
        