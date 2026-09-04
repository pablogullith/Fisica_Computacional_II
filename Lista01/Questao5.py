#Autor: Pablo Gullith
#Bibliotecas
from numpy import floor, linspace, array, zeros, copy
from scipy.fftpack import rfft, irfft
from pylab import plot, show, xlabel, ylabel, savefig

def f(t):	

	if floor(2*t) % 2==0:
		return 1
	else:
		return -1
		
n = linspace(0,1,1000,endpoint=False)
f = array(list(map(f,n)), float)
c = rfft(f)
c[10:]=0
yt = irfft(c)
plot(f)
xlabel('t')
ylabel('f(t)')
savefig("f.png")
show()
plot(f,'k')
plot(yt,'r')
xlabel('t')
ylabel('f(t)')
savefig("f_filtered.png")
show()
show()
