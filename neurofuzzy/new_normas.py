# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:58:20 2022

@author: adalc
"""

import matplotlib.pyplot as plt 
import numpy as np 

plt.close('all')

x = np.arange(-15,16,1)
A = 1/(1+((x + 5)/7.5)**4)
B = 1/(1+((x - 5)/5)**2)

#T-normas
#Hamacher
r = 8
H = A*B/(r + (1 - r)*(A + B - A*B))
#Schweizer & Sklar 1
p = 5
S = np.abs(np.maximum(0,A**p + B**p - 1))**(1/p)
#Yager
w = 2
Y = 1 - np.minimum(1,((1 - A)**w + (1 - B)**w)**(1/w))

plt.figure()
plt.plot(A,label = 'A')
plt.plot(B,label = 'B')
plt.plot(H,label = 'Hamacher')
plt.plot(S,label = 'Schwizer-Sklar')
plt.plot(Y,label = 'Yager')
plt.title('T-normas')
plt.legend()


#S-normas
#Hamacher
r = 1
H = (A + B + (r - 2)*A*B)/(r + (r - 1)*A*B)
#Schweizer & Sklar 1
p = 2
S = 1 - np.abs(np.maximum(0,(1 - A)**p + (1 - B)**p - 1))**(1/p)
#Yager
w = 2
Y = 1 - np.minimum(1,(A**w + B**w)**(1/w))

plt.figure()
plt.plot(A,label = 'A')
plt.plot(B,label = 'B')
plt.plot(H,label = 'Hamacher')
plt.plot(S,label = 'Schwizer-Sklar')
plt.plot(Y,label = 'Yager')
plt.title('S-normas')
plt.legend()
        