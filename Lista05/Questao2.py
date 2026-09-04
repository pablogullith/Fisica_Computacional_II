#Autor: Pablo Gullith
#Bibliotecas
from pylab import *

N = 10000000
z = random(N)
x = z**2

def funcao(x):
	
	return 1/(1+exp(x))

Integral = sum(funcao(x))/N*2

print('Integral:',Integral)