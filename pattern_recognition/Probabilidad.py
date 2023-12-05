# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:01:37 2022

@author: adalc
"""

e = espacio_muestral  = [1,2,3,4,5,6]
n = len(espacio_muestral)

#Sucesos simples mutuamente excluyentes
probabilidad = 1.0/n

#Sucesos compuestos por sucesos simples mutuamente excluyentes
#Unión o suma
numeros_pares = [i for i in espacio_muestral if i%2 == 0]
h = len(numeros_pares)
probilidad_comp = float(h)/n

#Funciones#
# Probabilidad de sucesos simples mutuamente excluyentes
pssme = lambda e: 1.0/len(e) #Función Lambda (Anónima)

# Probabilidad de sucesos compuestos mutuamente excluyentes
def pscme(e, sc): #e espacio muestral | sc sucesos compuestos
    n = len(e)
    return len(sc)/float(n)

###Probabilidad condicional###
#Dependientes
a = [i for i in espacio_muestral if i % 2 != 0]
b = [i for i in espacio_muestral if i < 4]
intersec = [i for i in a if i in b]
intersec = [i for i in a if i in b] # intersección de A y B
n = len(e) # total de la muestra
ha = len(a) # total de sucesos simples en A
hintersec = len(intersec) # total de sucesos simples en la intersección
# probabilidad de la intersección
probabilidad_intersec = float(hintersec)/n
# probabilidad de 'a'
probabilidad_a = float(ha)/n
# probabilidad condicional
probabilidad_b_dado_a = probabilidad_intersec/probabilidad_a

#Independientes
# probabilidad de A
a = [i for i in e if i%2 != 0] #impares
pa = len(a)/float(n)
# probabilidad de B
b = [i for i in e if i%2 == 0] #pares
pb = len(b)/float(n)
# probabilidad de la intersección de sucesos
pi = pa*pb

#Funciones#
# Probabilidad condicional: sucesos dependientes
def pscd(e, a, b):
    i = list(set(a).intersection(b))
    pi = pscme(e, i)
    pa = pscme(e, a)
    return pi / pa
# Probabilidad condicional: sucesos independientes
def psci(e, a, b):
    pa = pscme(e, a)
    pb = pscme(e, b)
    return pa * pb


