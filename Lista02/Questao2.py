#Autor: Pablo Gullith
#Bibliotecas
from numpy import zeros
from pylab import imshow, colorbar, show, savefig

#Constantes
V = 1.0
a = 0.01
N = 101
delta = 10 ** -6
omega = 0.9

def larger(a, b):
    if a >= b:
        return a
    else:
        return b


max_diff = 2 * delta

phi = zeros([N + 1, N + 1], float)
phi[0,:] = V
while max_diff > delta:
    
    max_diff = 0.0
    for i in range(N + 1):
        for j in range(N + 1):
            if not i == 0 and not j == 0 and not i == N and not j == N:
                old_phi = phi[i,j]
                new_phi = (1 + omega) * (phi[i + 1, j] + phi[i - 1, j] + phi[i, j + 1] + phi[i, j - 1]) / 4 \
                          - omega * old_phi
                phi[i, j] = new_phi

                
                max_diff = larger(max_diff, abs(new_phi - old_phi))
    


imshow(phi)
colorbar()
savefig("phi1.png")
show()
