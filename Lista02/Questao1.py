#Autor: Pablo Gullith
#Bibliotecas
from numpy import sqrt, zeros
from pylab import imshow, show, colorbar, savefig

#Constantes
epsilon_0 = 1.0
L = 100
N = 101  
a = L / N  
rho_0 = 1.0
delta = 10 ** -6

def rho(i, j):
    if 20 < i < 40 and 60 < j < 80:
        return rho_0
    elif 60 < i < 80 and 20 < j < 40:
        return -rho_0
    else:
        return 0

test = zeros([N+1,N+1], float)
for i in range(N):
     for j in range(N):
            test[i,j] = rho(i,j)
imshow(test)
colorbar()
savefig("rho.png")
show()

def larger(a, b):
    if a >= b:
        return a
    else:
        return b


max_diff = 2 * delta

phi = zeros([N + 1, N + 1], float)

while max_diff > delta:
    
    max_diff = 0.0
    for i in range(N + 1):
        for j in range(N + 1):
            if not i == 0 and not j == 0 and not i == N and not j == N:
                old_phi = phi[i,j]
                new_phi = (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1] \
                             + a ** 2 / 4 * rho(i, j)) / 4
                phi[i, j] = new_phi

                
                max_diff = larger(max_diff, abs(new_phi - old_phi))


imshow(phi)
colorbar()
savefig("phi.png")
show()
