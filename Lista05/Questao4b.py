#Autor: Pablo gullith
#Bibliotecas

import math as mt
from pylab import *
import random as rd


def ff(x):
    return mt.cos(x) + mt.cos(x*2**(1/2)) + mt.cos(x*3**(1/2))


def Temp(t, tmax):
    tau = 1e4
    return tmax*mt.exp(-t/tau)


x = 0
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
    if rd.random() > mt.exp((-ff(x) + ff(xOld))/(kb*Tp)) or x >= 50 or x <= 0:
        x -= delta
print(x)
plot(xp, ".")
xlabel("Tempo")
ylabel("X")
title("X ao longo do tempo - letra b")
savefig("x1.png")
show()

# Os dados de Tau, Tmin e Tmax eu coloquei iguais os que o senhor fez na questão em sala "salesmanb".