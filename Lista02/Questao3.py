#Autor: Pablo Gullith
#Bibliotecas
from numpy import zeros
from pylab import imshow, colorbar, show, savefig

#Constantes
V = 1.0 
a = 0.1  
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
phi[20:81, 20] = V 
phi[20:81, 80] = -V

while max_diff > delta:
     
    max_diff = 0.0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if(j != 20 and j != 80):
                delta = (phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1])/4 - phi[i,j]
                phi[i,j]=phi[i,j]+(1+omega)*delta
            elif(j==20 or j==80):
                if(i<=20 or i>=80):
                   delta = (phi[i+1,j]+phi[i-1,j]+phi[i,j+1]+phi[i,j-1])/4 - phi[i,j]
                   phi[i,j]=phi[i,j]+(1+omega)*delta

        if (abs(delta) > max_diff):
            max_diff = abs(delta)

    if(max_diff < delta):
        break

imshow(phi)
colorbar()
savefig("phi3.png")
show()
