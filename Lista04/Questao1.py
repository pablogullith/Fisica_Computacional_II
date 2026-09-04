#Autor: Pablo Gullith
#Bibliotecas
from random import randint

a = randint(1,6)
b = randint(1,6)

print('{}\t{}'.format(a,b))

count = 0
for i in range(1000000):
	a = randint(1,6)
	b = randint(1,6)
	if a==6 and b==6:
		count+=1

Fracao = count/1e6
print('Fracao de vezes que você recebe o duplo 6 é:',Fracao)