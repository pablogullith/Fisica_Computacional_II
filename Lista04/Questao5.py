#Autor: Pablo Gullith
#Bibliotecas
from pylab import sqrt, sin
from numpy.random import random

#Definição
def f(x):
	return sin(1/x/(2-x))**2

#Dados	
a = 0
b = 2
A = (b-a)*1
N = 10000

x = random(N)*2
y = random(N)
fx = f(x)
count = sum(fx>y)

#Monte carlo 
Integral1 = A*count/N
Erro1 = sqrt(Integral1*(A-Integral1)/N)
print('Resultado da integral por monte carlo:',Integral1)
print('Erro por monte carlo:',Erro1)

print()

#Valor médio
Integral2 = (b-a)/N*sum(fx)
var2 = sum(fx**2)/N - (sum(fx)/N)**2
Erro2 = (b-a)*sqrt(var2/N)
print('Resultado da integral por valor medio:',Integral2)
print('Erro por valor medio:',Erro2)