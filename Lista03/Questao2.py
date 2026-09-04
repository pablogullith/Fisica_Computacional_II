#Autor: Pablo Gullith
#Bibliotecas
from pylab import plot,xlabel,ylabel,show,zeros,linspace,savefig

N = 100
L = 100
h = L/N
g = 9.81

x = zeros(N+1,float)

x[0]=0
x[N]=0

delta = 1


while delta>10**-6:
	xp = h**2/g/2 + 1/2*(x[2:N+1] + x[0:N-1])
	delta = max(abs(xp-x[1:N]))
	x[1:N] = xp
	

plot(linspace(0,10,N+1),x)
xlabel('t')
ylabel('x')
savefig("x.png")
show()
