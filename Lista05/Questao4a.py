#Autor: Pablo Gullith
#Bibliotecas

import math as mt
from pylab import *
import random as rd


def f(x):
    return x**2 -mt.cos(mt.pi*4*x)


def Temp(t, tmax):
    tau = 1e4
    return tmax*mt.exp(-t/tau)


x = 2
xp = []
Tmin = 1e-3
Tmax = 10.0
t = 0
kb = 1
xOld = 0
Tp = Tmax
while Tp > Tmin:
    t += 1
    Tp = Temp(t, Tmax)
    xp.append(x)
    r = mt.sqrt(-2*mt.log(1 - rd.random()))
    theta = rd.random()*2*mt.pi
    delta = r*mt.cos(theta)
    xOld = x
    x += delta
    if rd.random() > mt.exp((-f(x) + f(xOld))/(kb*Tp)):
        x = xOld
print(x)
plot(xp, ".")
xlabel("Tempo")
ylabel("X")
title("X ao longo do tempo - letra a")
savefig("x.png")
show()

# Os dados de Tau, Tmin e Tmax eu coloquei iguais os que o senhor fez na questão em sala "salesmanb".