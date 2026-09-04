#Autor: Pablo Gullith
#Bibliotecas
from cmath import exp
from numpy import array, linspace, pi, cos, sin
from dcst import dst, idst
import matplotlib.pyplot as plt

def psi0(x):
    
    return exp(-(x-x0)**2/(2*sigma**2))*exp(1j*k*x)

def c(t):
    c = array([alpha[k]*cos(R*k**2*t) - eta[k]*sin(R*k**2*t) for k in range(N)],float)

    return c

L  = 1e-8
M  = 9.109e-31
x0 = L/2
h  = 1.0545718e-34
k  = 5e10
R  = (pi**2*h)/(2*M*L**2)
N  = 1000
sigma   = 1e-10
alpha   = []
eta     = []
xpoints = linspace(0, L, N)

A = array([psi0(xpoints[i]).real for i in range(N)],float)
B = array([psi0(xpoints[i]).imag for i in range(N)],float)

alpha = dst(A)
eta   = dst(B)
b_k   = alpha + eta*1j



t = [1e-16]

for i in t:
	plt.plot(idst(c(i)), label = "t = {}".format(i))

plt.legend()
plt.xlabel("x")
plt.ylabel("psi")
plt.title("Evolução temporal da função de onda")
plt.savefig("psi.png")
plt.show()


t = [2e-16,4e-16,6e-16,8e-16,1e-15]

for i in t:
	plt.plot(idst(c(i)), label = "t = {}".format(i))

plt.legend()
plt.xlabel("x")
plt.ylabel("psi")
plt.title("Evolução temporal da função de onda")
plt.savefig("psi1.png")
plt.show()

'''
C)
Com o aumento do t percebemos que o pico em y ocorre mais proximo do x = 0
logo a frequência diminui com o passar do tempo.
'''
