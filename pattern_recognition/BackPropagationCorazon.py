import os
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

plt.close("all")
#=========== Se Cargan los Datos del complejo PQRST =========================#
mat1 = scipy.io.loadmat('complejo.mat')
corazon  = mat1["ECG"]
maximo   = np.max(np.abs(corazon[170:211]))
complejo = corazon[170:211]/maximo
plt.figure()
plt.plot(complejo)

#========== Entrenamiento de Tipo Back-Propagation ==========================#
# w1 = np.array([[0.552066, 0.630556, -0.160708, -0.105904, -0.156121, 0.274024, 0.783117, 0.416339, 0.229726, 0.313834]]).T
# b1 = np.array([[0.291525, 0.1795, -0.0994794, -0.217357, -0.0502783, -0.252782, 0.634564, 0.231901, -0.0900022, 0.642082]]).T
# w2 = np.array([[0.133688, -0.464947, 0.073163, 0.470569, 0.0139398, 0.0531539, 0.411573, -0.440494, 0.341193, -0.26571]])
# b2 = np.array([[-0.0707505]])

w1 = np.random.rand(10, 1)
b1 = np.random.rand(10, 1)
w2 = np.random.rand(1, 10)
b2 = np.random.rand(1,  1)

# patron = np.linspace(0, 1, 41)
# patron = patron[:, np.newaxis]
patron = complejo
target = complejo

alpha = 0.01
for j in range (1500):
    for i in range (patron.shape[0]):
        a0 = patron[i]
        a0 = a0[:, np.newaxis]
        n1 = w1@(a0) + b1
        a1 = 1 / (1 + np.exp(-n1))
        n2 = w2@(a1) + b2
        a2 = n2
        t  = target[i]
        t  = t[:, np.newaxis]
        e  = t - a2
        dF2 = 1
        s2 = (-2)*dF2*e
        dF1 = np.diagflat((1-a1)*a1)
        s1 = ((dF1).dot(w2.T)).dot(s2)
        w2 = w2 - (alpha*s2*a1.T)
        b2 = b2 - (alpha*s2)
        w1 = w1 - (alpha*s1*a0.T)
        b1 = b1 - (alpha*s1)

#========= Prueba al Sistemas ===============================================#
salida = np.zeros(patron.shape[0])
for ii in range (patron.shape[0]):
    a0 = patron[ii]
    a0 = a0[:, np.newaxis]
    n1 = w1@(a0) + b1
    aa1 = 1 / (1 + np.exp(-n1))
    n2 = w2@(aa1) + b2
    salida[ii] = n2

plt.figure()
plt.plot(salida,'ob')
plt.plot(target,'+-')
#============================================================================#
mat2 = scipy.io.loadmat('rec_1m.mat')
prueba   = mat2["val"].T
maxi   = np.max(np.abs(prueba))
prueba = prueba/maxi

plt.figure()
plt.plot(prueba,'+-')

sal = np.zeros(prueba.shape[0])
for i in range (prueba.shape[0]):
    a0 = prueba[i]
    a0 = a0[:, np.newaxis]
    n1 = w1@(a0) + b1
    a1 = 1 / (1 + np.exp(-n1))
    n2 = w2@(a1) + b2
    a2 = 1 / (1 + np.exp(-n2))
    sal[i] = n2

plt.plot(sal,'or')





