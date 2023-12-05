#------------------------------Ejercicio 5 ------------------------------------
#----------------------------Base de Datos Iris--------------------------------
#________________________________ADALINE_______________________________________
import numpy as np 
from matplotlib import pyplot as plt 
from numpy.random import uniform , random
from mpl_toolkits.mplot3d import Axes3D
from sympy import *
from math import log
from scipy.fft import fft, ifft
import pyaudio
import wave
import winsound


def hardlimitS(value):
    
    if value < 0:
        value=-1
        
    else:
        value = 1
    return value 

def plano3d(intx,inty, intz):
    puntos= [  [ float(intx), 0 , 0 ],
               [ 0 ,  float(inty), 0], 
               [ 0 , 0 , float(intz)]    ]
    punto0, punto1, punto2= puntos 
    
    Ax,Ay,Az=punto0
    Bx,By,Bz=punto1
    Cx,Cy,Cz=punto2
    
    ABx,ABy,ABz= [Bx-Ax,By-Ay,Bz-Az]
    ACx,ACy,ACz= [Cx-Ax,Cy-Ay,Cz-Az]
    ABcruzAC= [ABy * ACz - ABz * ACy, ABz * ACx - ABx * ACz, ABx * ACy - ABy * ACx]
    
    punto= np.array(punto0)
    vectorNormal= np.array(ABcruzAC) 
    d= -punto.dot(vectorNormal)
    
    xx,yy=np.meshgrid(range(0,4),range(0,15))
    z= (-vectorNormal[0]*xx-vectorNormal[1]*yy-d)* 1. /vectorNormal[2]
    return xx,yy,z

def EntropiaShannon(Audios):
    H = 0
    for i in range(len(Audios[:546])):
        H -= Audios[i]*log(Audios[i])
        
    H1 = 0
    for i in range(546,len(Audios[:1340])):
        H1 -= Audios[i]*log(Audios[i])
        
    H2 = 0
    for i in range(1340,len(Audios)):
        H2 -= Audios[i]*log(Audios[i])
    return(H,H1,H2)


def Data(Fourier):
    Entropy=[]
    MaxData=[]
    for j in range(len(Fourier)):
        suma=0
        for i in range(len(Fourier[j])):
            suma=suma+(1/Fourier[j][i])*(log(Fourier[j][i],2))
        Max=Fourier[j][1250]
        
        Entropy.append(suma)
        MaxData.append(Max)
    P=np.zeros([len(Entropy),2])
    P[:,0]=np.array(Entropy)
    P[:,1]=np.array(MaxData)
    return(P)

def Norm(P, EntropyMax, MaximoMax):
    P[:,0]=P[:,0]/EntropyMax
    P[:,1]=P[:,1]/MaximoMax
    return(P)
plt.close('all')

paquete=512
sample=pyaudio.paInt16
canales=1
fs=8000
segundos=2

words=[]

Fourier=[]
T = 1.0 / 6
x = np.linspace(0.0, fs*T,fs)
y = np.sin(60.0*np.pi*x)

y_f = fft(y)

x_f = np.linspace(0.0, 1.0/(2.0*T), fs//2)
# plt.figure(1)
# plt.title('Seno FFT')




# plt.plot(x_f, 2.0/fs* np.abs(y_f[:fs//2]))

# plt.figure(2)
# plt.title('Seno sin FFT')
# plt.plot(x,y)

# for j in range(30):
#     archive=str(j)+'patron.wav'
#     obj_audio=pyaudio.PyAudio()
    
#     input('Presiona na tecla \n')
    
#     streaming = obj_audio.open(format=sample, channels=canales,  rate=fs,
#                                 frames_per_buffer=paquete, input=True)
#     tramas=[]
#     sonido=[]
    
#     for i in range(0,int(fs/paquete*segundos)):
#         datos=streaming.read(paquete)
#         tramas.append(datos)
#         sonido.append(np.frombuffer(datos, dtype=np.int16))
        
        
#     streaming.stop_stream()
#     streaming.close()
    
#     obj_audio.terminate()
    
    
#     wf=wave.open(archive, 'wb')
#     wf.setnchannels(canales)
#     wf.setsampwidth(obj_audio.get_sample_size(sample))
#     wf.setframerate(fs)
#     wf.writeframes(b''.join(tramas))
#     wf.close()
#     winsound.PlaySound(archive, winsound.SND_FILENAME | winsound.SND_ASYNC)
    
    
#     Palabra=np.hstack(sonido)
#     Frec=fft(Palabra)
#     Tamaño=len(Frec)
#     Fourier.append(abs(Frec[0:int(Tamaño/2)]))
#     print('Palabra número ',j+1,' grabada')
    
#     np.savetxt('sonido.txt', sonido, fmt='%.18g', delimiter=' ')

#     np.savetxt('Fourier.txt', Fourier, fmt='%.18g', delimiter=' ')

# print('Sali del for')
    
Fourier= np.loadtxt('Fourier.txt')

s=np.zeros((30,3))

s[0] = EntropiaShannon(Fourier[0])
s[1] = EntropiaShannon(Fourier[1])
s[2]=EntropiaShannon(Fourier[2])
s[3]=EntropiaShannon(Fourier[3])
s[4]=EntropiaShannon(Fourier[4])
s[5]=EntropiaShannon(Fourier[5])
s[6]=EntropiaShannon(Fourier[6])
s[7]=EntropiaShannon(Fourier[7])
s[8]=EntropiaShannon(Fourier[8])
s[9]=EntropiaShannon(Fourier[9])
s[10] = EntropiaShannon(Fourier[10])
s[11]=EntropiaShannon(Fourier[11])
s[12]=EntropiaShannon(Fourier[12])
s[13]=EntropiaShannon(Fourier[13])
s[14]=EntropiaShannon(Fourier[14])
s[15]=EntropiaShannon(Fourier[15])
s[16]=EntropiaShannon(Fourier[16])
s[17]=EntropiaShannon(Fourier[17])
s[18] = EntropiaShannon(Fourier[18])
s[19] = EntropiaShannon(Fourier[19])
s[20]=EntropiaShannon(Fourier[20])
s[21]=EntropiaShannon(Fourier[21])
s[22]=EntropiaShannon(Fourier[22])
s[23]=EntropiaShannon(Fourier[23])
s[24]=EntropiaShannon(Fourier[24])
s[25]=EntropiaShannon(Fourier[25])
s[26]=EntropiaShannon(Fourier[26])
s[27] = EntropiaShannon(Fourier[27])
s[28] = EntropiaShannon(Fourier[28])
s[29]=EntropiaShannon(Fourier[29])

datos=-s/250000000
w= uniform(0,1,size=(2,3))

b= uniform(0,1,size=(1,2))
print(b)

tarjets=[]
for i in range(0,8,1):
    tarjets.append(np.array([-1,-1]))
for i in range(10,18,1):
    tarjets.append(np.array([1,-1]))
for i in range(20,28,1):
    tarjets.append(np.array([1,1]))
    
erroneos=0
epocas=10000
P=datos
R=0
for i in range(0,24,1):
    R=R+np.outer(P[i],np.transpose(P[i]))

eigenvalor,vector=np.linalg.eig(R)
landamax=max(eigenvalor)
alpha=5e-5


for i in range (epocas):
    for j in range (0,24,1):
        a= np.dot(w,np.transpose(datos[j])) + b
        error= np.float64( tarjets[j]-a)
        w= w +alpha*( np.outer(error,datos[j]))
        b= b+alpha*error
        
        
cont=0      

print('Los valores de peso son:' ,w)
print('Los valores de polarización son:', b)

for j in range (0,24,1):
    a= np.dot(w,np.transpose(datos[j]))+ b
    a[0][0]=hardlimitS(a[0][0])
    a[0][1]=hardlimitS(a[0][1])
    error= np.float64(tarjets[j]-a)
    w= w + alpha*( np.outer(error,datos[j]))
    b= b+alpha*error
        
    if (error[0][0]!=0 or error[0][1]!=0):
        erroneos=erroneos+1
 
eficiencia= (24 - erroneos)* 100 / len(datos)
print('La eficiencia es de \n', eficiencia,'%')
print('acertando en: ', 24-erroneos)



p11=np.float64(-b[0][0]/w[0][0])
p12=np.float64(-b[0][0]/w[0][1])
p13=np.float64(-b[0][0]/w[0][2])


p21=np.float64(-b[0][1]/w[1][0])
p22=np.float64(-b[0][1]/w[1][1])
p23=np.float64(-b[0][1]/w[1][2])

xx,yy,z= plano3d(p11,p12,p13)
xx1,yy1,z1= plano3d(p21,p22,p23)


plt.figure(1)
plt3d = plt.axes(projection='3d')
plt3d.plot_surface(xx,yy,z, alpha = 0.8, color = 'yellow')
plt3d.plot_surface(xx1,yy1,z1, alpha = 0.8, color = 'green')


for i in range(0,8):
    plt3d.scatter(datos[i][0], datos[i][1],datos[i][2],marker='o', c='red')
for i in range(8,16):
    plt3d.scatter(datos[i][0], datos[i][1],datos[i][2],marker='o', c='blue')    
for i in range(16,24):
    plt3d.scatter(datos[i][0], datos[i][1],datos[i][2],marker='o', c='green')
plt3d.plot([0,w[0][0]],[0,w[0][1]],[0,w[0][2]], color="yellow")
plt3d.plot([0,w[1][0]],[0,w[1][1]],[0,w[1][2]], color="green")

plt.figure(2)

for j in range (24,30,1):
    a= np.dot(w,np.transpose(datos[j]))+ b
    a[0][0]=hardlimitS(a[0][0])
    a[0][1]=hardlimitS(a[0][1])
    


for i in range(24,26):
    plt3d.scatter(datos[i][0], datos[i][1],datos[i][2],marker='o', c='red')
for i in range(26,28):
    plt3d.scatter(datos[i][0], datos[i][1],datos[i][2],marker='o', c='blue')    
for i in range(28,30):
    plt3d.scatter(datos[i][0], datos[i][1],datos[i][2],marker='o', c='green')
plt3d.plot([0,w[0][0]],[0,w[0][1]],[0,w[0][2]], color="yellow")
plt3d.plot([0,w[1][0]],[0,w[1][1]],[0,w[1][2]], color="green")







