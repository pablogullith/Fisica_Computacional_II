#Autor: Pablo Gullith
#Bibliotecas
from pylab import plot, show, xlabel, ylabel, legend, savefig, arange
from random import random

random()

#Dados
h = 1 
Bi209 = 0
Pb209 = 0
Ti209 = 0
Bi213 = 10000
pPb = 1 - 2**(-h/3.3/60)
pTi = 1 - 2**(-h/2.2/60)
pBi = 1 - 2**(-h/46/60)

#Listas
Bi209_list = []
Pb209_list = []
Ti209_lsit = []
Bi213_list = []

t = arange(0,2e4,h)

#Laços
for ti in t:
	Bi209_list.append(Bi209)
	Pb209_list.append(Pb209)
	Ti209_lsit.append(Ti209)
	Bi213_list.append(Bi213)
	
	for i in range(Pb209):
		if random()<pPb:
			Pb209-=1
			Bi209+=1
	
	for i in range(Ti209):
		if random()<pTi:
			Ti209-=1
			Pb209+=1
	
	for i in range(Bi213):
		if random()<pBi:
			Bi213 -=1
			if random()<0.9791:
				Pb209+=1
			else:
				Ti209+=1
                
#Plots
plot(t,Ti209_lsit,label='Ti209 - Talio')
plot(t,Pb209_list,label='Pb209 - Chumbo')	
plot(t,Bi213_list,label='Bi213 - Bismute')			
plot(t,Bi209_list,label='Bi209 - Bismute')
legend()
xlabel('Tempo em segundos')
ylabel('Numero de atomos')
savefig('decaimento.png')
show()