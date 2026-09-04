#Autor: Pablo Gullith
#Biblotecas
from numpy import sqrt, pi, log, cos, sin
from numpy.random import random
from pylab import hist, ylabel, xlabel, title, show, savefig

def gauss():
    r = sqrt(-2*log(1-random()))
    theta = 2*pi*random()
    x = r*cos(theta)
    y = r*sin(theta)
    return x, y

z = random(10000)

#A
print("a)")
nums = -log(1 - z)


ylabel("Numeros sorteados neste intervalo")
xlabel("x")
title("Histograma")
hist(nums,bins=20)
savefig("histograma.png")
show()

#B
print("b)")
apoints = []
for i in range(10000):
    a, b = gauss()
    apoints.append(a)
    apoints.append(b)
    

ylabel("Numeros sorteados neste intervalo")
xlabel("x")
title("Histograma")
hist(apoints,bins=20)
savefig("histograma_gauss.png")
show()
