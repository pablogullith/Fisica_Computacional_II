#Autor: Pablo Gullith
#Bibliotecas
import random as rd

s = 0
N = 1000000

for i in range(1, N):
    x1 = 2*rd.random()-1
    x2 = 2*rd.random()-1
    x3 = 2*rd.random()-1
    x4 = 2*rd.random()-1
    x5 = 2*rd.random()-1
    x6 = 2*rd.random()-1
    x7 = 2*rd.random()-1
    x8 = 2*rd.random()-1
    x9 = 2*rd.random()-1
    x10 = 2*rd.random()-1
    if x1**2 + x2**2 + x3**2 + x4**2 + x5**2+ x6**2 +x7**2 + x8**2+ x9**2 + x10**2 < 1:
        s += 1
I = 2**(10)/N*s
print("A integral é {}".format(I))