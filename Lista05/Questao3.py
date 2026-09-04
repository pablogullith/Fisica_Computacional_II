#Autor: Pablo Gullith
#Bibliotecas

import random as rd
import numpy as np
import math as mt
from pylab import *


def calcGrid():
    N = 20
    matriz = np.zeros([N, N], int)
    for h in range(N):
        for w in range(N):
            if rd.random() < 0.5:
                s = 1
            else:
                s = -1
            matriz[h, w] = s
    return matriz


def calcEne(grid, j):
    N = 20
    en = np.sum(grid[:, :N-1]*grid[:, 1:]) + np.sum(grid[:N-1, :]*grid[1:, :])
    return -en*j


j = 1
T = 1
kb = 1
beta = 1/(T*kb)
passos = 1000000
grid = calcGrid()
M = []
for i in range(passos):
    M.append(np.sum(grid))
    x = rd.randrange(20)
    y = rd.randrange(20)
    eVelha = calcEne(grid, j)
    grid[x, y] *= -1
    eNova = calcEne(grid, j)
    if rd.random() > mt.exp(-(eNova - eVelha)*beta):
        grid[x, y] *= -1

plot(M)
xlabel("Tempo")
ylabel("Magnetizacao total")
title("Magnetizacao total ao longo do tempo")
savefig("magnetizacao.png")
show()

# o valor de M converge alternando sempre entre 400 e -400 o que nos diz que todos os spins se alinham em 1 ou -1

