# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 08:58:36 2022

@author: adalc
"""

import numpy as np
import matplotlib.pyplot as plt

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

plt.close('all')
pi=np.pi
x = np.arange(0,360,1)
x2=np.arange(pi/16, 2*pi, ((2*pi-pi/16)/360))
x3=np.arange(0,2,2/360)


NEv = trapezoidal(x, 0, 0, 15, 60)
Ev=trapezoidal(x, 30, 75, 105, 150)
Sv=trapezoidal(x, 120, 165 , 195, 240)
Ov=trapezoidal(x, 210 , 255, 285, 330)
NOv=trapezoidal(x, 300, 345, 360, 360)

NEg = trapezoidal(x, 0, 0, 15, 60)
Eg=trapezoidal(x, 30, 75, 105, 150)
Sg=trapezoidal(x, 120, 165 , 195, 240)
Og=trapezoidal(x, 210 , 255, 285, 330)
NOg=trapezoidal(x, 300, 345, 360, 360)


# A2 = lambda x: 1/(1 + np.exp(-0.3*(x - 50)))
# B1 = lambda y: np.exp(-0.5*((y - 25)/20)**2)
# B2 = lambda y: np.exp(-0.5*((y - 75)/20)**2)
# C1 = lambda z: 1/(1 + np.exp(0.3*(z - 50)))
# C2 = lambda z: np.exp(-0.5*((z - 75)/20)**2)
B= trapezoidal(x2, pi/16, pi/16, 7*pi/21+pi/16, 12*pi/21+pi/16)
M= trapezoidal(x2, 9*pi/21, 14*pi/21, 28*pi/21+pi/16, 33*pi/21+pi/16)
A= trapezoidal(x2, 30*pi/21, 35*pi/21, 42*pi/21, 2*pi)

NM=trapezoidal(x, 0, 0, 0.2*180, 0.55*180)
H=trapezoidal(x, 0.45*180, 0.8*180, 1.2*180, 1.55*180)
AH=trapezoidal(x, 1.45*180, 1.8*180, 360, 360)

plt.figure()
plt.plot(NEv, label = 'NEv')
plt.plot(Ev, label = 'Ev')
plt.plot(Sv, label = 'Sv')
plt.plot(Ov, label = 'Ov')
plt.plot(NOv, label = 'NOv')
plt.legend()

plt.figure()
plt.plot(NEg, label = 'NEg')
plt.plot(Eg, label = 'Eg')
plt.plot(Sg, label = 'Sg')
plt.plot(Og, label = 'Og')
plt.plot(NOg, label = 'NOg')
plt.legend()

plt.figure()
plt.plot(B, label = 'Baja')
plt.plot(M, label = 'Media')
plt.plot(A, label = 'Alta')
plt.legend()


plt.figure()
plt.plot(NM, label = 'No movimiento')
plt.plot(H, label = 'Horario')
plt.plot(AH, label = 'Anti Horario')
plt.legend()



# plt.figure()
# plt.plot(B1(y), label = 'B1')
# plt.plot(B2(y), label = 'B2')
# plt.legend()

# plt.figure()
# plt.plot(C1(z), label = 'C1')
# plt.plot(C2(z), label = 'C2')
# plt.legend()

NEv_NEg=(min(NEv,NEg))
NEv_Eg=min(NEv,Eg)
NEv_Sg=min(NEv,Sg)
NEv_Og=min(NEv,Og)
NEv_NOg=min(NEv,NOg)

Ev_NEg=(min(Ev,NEg))
Ev_Eg=min(Ev,Eg)
Ev_Sg=min(Ev,Sg)
Ev_Og=min(Ev,Og)
Ev_NOg=min(Ev,NOg)

Sv_NEg=(min(Sv,NEg))
Sv_Eg=min(Sv,Eg)
Sv_Sg=min(Sv,Sg)
Sv_Og=min(Sv,Og)
Sv_NOg=min(Sv,NOg)

Ov_NEg=(min(Ov,NEg))
Ov_Eg=min(Ov,Eg)
Ov_Sg=min(Ov,Sg)
Ov_Og=min(Ov,Og)
Ov_NOg=min(Ov,NOg)


NOv_NEg=(min(NOv,NEg))
NOv_Eg=min(NOv,Eg)
NOv_Sg=min(NOv,Sg)
NOv_Og=min(NOv,Og)
NOv_NOg=min(NOv,NOg)




B_agg=max(NEv_NEg,NEv_NOg,NOv_NEg,NOv_NOg,Ev_Eg,Sv_Sg,Ov_Og)
M_agg=max(NEv_Eg,NEv_Og,Ev_NEg,Ev_Sg,Ev_NOg,Sv_Eg,Sv_Og,Ov_NEg,Ov_Sg,Ov_NOg,NOv_Eg,NOv_Og)
A_agg=max(NEv_Sg,Ev_Og, Sv_NEg,Sv_NOg,Ov_Eg, NOv_Sg)

NM_agg=max(NEv_NEg,Ev_Eg,Sv_Sg,Ov_Og,NOv_NOg,NEv_NOg,NOv_NEg)
H_agg=max(NEv_Og,Ev_NEg, Ev_Og,Ev_NOg,Sv_NEg,Sv_Eg,Ov_Sg,NOv_Sg,NOv_Og)
AH_agg=max(NEv_Eg,NEv_Sg,Ev_Eg,Sv_Og,Sv_NOg,Ov_NEg,Ov_Eg, Ov_NOg,NOv_Eg)

B_sal=[]
M_sal=[]
A_sal=[]

for i in range(len(B)):
    B_sal.append(B_agg if B[i] > B_agg else B[i])
    M_sal.append(M_agg if M[i] > M_agg else M[i])
    A_sal.append(A_agg if A[i] > A_agg else A[i])

NM_sal=[]
H_sal=[]
AH_sal=[]

for i in range(len(H)):
    NM_sal.append(NM_agg if NM[i] > NM_agg else NM[i])
    H_sal.append(H_agg if H[i] > H_agg else H[i])
    AH_sal.append(AH_agg if AH[i] > AH_agg else AH[i])

plt.figure()
plt.plot(B_sal, label = 'BAJA salida')
plt.plot(M_sal, label = 'MEDIA salida')
plt.plot(A_sal, label = 'ALTA salida')
plt.legend()


plt.figure()
plt.plot(NM_sal, label = 'NO MOVIMIENTO salida')
plt.plot(H_sal, label = 'HORARIO salida')
plt.plot(AH_sal, label = 'ANTIHORARIO salida')
plt.legend()

Velocidad = np.maximum(B_sal,M_sal,A_sal)

plt.figure()
plt.plot(Velocidad, label = 'Velocidad')
plt.legend()


Sentido = np.maximum(H_sal,NM_sal,AH_sal)

plt.figure()
plt.plot(Sentido, label = 'Sentido')
plt.legend()

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

# plt.figure()
# plt.plot(CT, label = 'CT')
# plt.legend()


# plt.figure()
# ax3 = plt.axes(projection = '3d')
# ax3.contour3D(Xm,Ym,ZZ,100,cmap="inferno")

# ax3.plot_surface(Xm, Ym, ZZ, cmap='Set1')


