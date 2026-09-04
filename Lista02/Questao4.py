#Autor: Pablo Gullith
#Bibliotecas
from pylab import plot, show, xlabel, ylabel, savefig
from numpy import sin, pi, zeros

A = 10
B = 12
tau = 365
D = 0.1

def T0(t):
	return A + B*sin(2*pi*t/tau)

L = 20  
D = 0.1
N = 100
a = L/N
h = 0.01
epsilon = h/1000
T = zeros(N+1,float)
T[1:N]=10


def iteracao(T,t_minimo,t_maximo):
	
	t = t_minimo
	c = h*D/a**2

	while t<t_maximo:		   
		T[0] = T0(t)
		T[N] = 11
		T[1:N] = T[1:N] + c*(T[2:N+1]+T[0:N-1]-2*T[1:N])
		t += h
	return T


T9 = iteracao(T,0,365*9)

T9_i = T9
t_minimo = 365*9
for t_maximo in [365*9 + i*(365//4) for i in range(4)]:
	T9_i = iteracao(T9_i,t_minimo,t_maximo)
	plot(T9_i,label=t_maximo%365/(365//4))
	t_minimo = t_maximo

xlabel("x")
ylabel("T")
savefig("phi4.png")
show()
