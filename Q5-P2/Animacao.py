#Autor: Pablo Gullith de melo dantas
#Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
from vpython import *

#Dados
L = 50 #Tamanho
scene2 = canvas(width = 650, height = 650, center = vector(L/2,L/2,0) ,background=color.black) #Local onde a animação é rodada
R_E = 0.50 # O raio da esfera 

def E(Dimer):
    return -Dimer

def N(M):
    for k in range(L):
        for j in range(L):
            if M[k,j] != 0:
                M[k,j] =1
    return M

csphere = np.zeros((L,L),dtype=sphere)   

#Varie o tau caso queira outros gráficos

P = 1e4

for k in [P]:
    A = np.zeros((L,L),dtype=int)
    Q = 0
    Ti = 1e3
    T_Min = 1e-3
    tau = k
    t = 0
    T = 1
    w = 0
    Dimer = 0
    t_list,y_list=[],[]
    
    for f in range(L):
        for j in range(L):
            csphere[f,j] = sphere(pos=vector(f,j,0), radius=R_E,color=color.black)
            
    while(T>T_Min):
        t+=1
        T = Ti*np.exp(-t/tau)
        x,y = int(np.random.randint(0,L)),int(np.random.randint(0,L))
        o = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        xo,yo = o[np.random.randint(0,high=4)]
        if (xo<0 or xo>=L or yo<0 or yo>=L):
            Q+=1
            t-=1
        else: 
            if(A[x,y]==0 and A[xo,yo]==0):
                w += 1
                A[x,y] = w
                A[xo,yo] = w
                Dimer +=1
                if x==xo:    
                    csphere[x,y],csphere[xo,yo] = sphere(pos=vector(x,y,0), radius=R_E,color=color.cyan),sphere(pos=vector(xo,yo,0), radius=R_E,color=color.cyan)
                else:
                    csphere[x,y],csphere[xo,yo] = sphere(pos=vector(x,y,0), radius=R_E,color=color.red),sphere(pos=vector(xo,yo,0), radius=R_E,color=color.red)
            elif(A[x,y]==A[xo,yo]):
                if (np.random.uniform()<np.exp(-1/T)):
                    A[x,y] = 0
                    A[xo,yo] = 0
                    Dimer -=1
                    csphere[x,y],csphere[xo,yo] = sphere(pos=vector(x,y,0), radius=R_E,color=color.black),sphere(pos=vector(xo,yo,0), radius=R_E,color=color.black)
                 
            if t%100:
                rate(30)
            t_list.append(t)
            y_list.append(E(Dimer))
            
