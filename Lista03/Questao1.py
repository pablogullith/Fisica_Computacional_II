#Autor: Pablo Gullith
#Bibliotecas
from pylab import plot, show, xlabel, ylabel, savefig, title
from numpy import empty, copy, exp

#Constantes
L = 1.0       
C = 1.0       
d = 0.1
N = 100       
sigma = 0.3   
a = L/N       
v = 100.0     
h = 1e-6
epsilon = h/1000
    
def Psi_Inicial(x):
    return (C*x*(L-x)/(L**2))*exp((-(x-d)**2)/(2*sigma**2))

phibeg = 0.0                
phimiddle = 0.0            
phiend = 0.0               
psibeg = 0.0               
psiend = 0.0                

t2 = 2e-3     #Corda em 2ms 
t50 = 50e-3   #Corda em 50ms
t100 = 100e-3 #Corda em 100ms
tend = t100 + epsilon


phi = empty(N+1,float)
phi[0] = phibeg
phi[N] = phiend
phi[1:N] = phimiddle
phip = empty(N+1,float)
phip[0] = phibeg
phip[N] = phiend

psi = empty(N+1,float)
psi[0] = psibeg
psi[N] = psiend
for i in range(1,N):
    psi[i] = Psi_Inicial(i*a)
psip = empty(N+1,float)
psip[0] = psibeg
psip[N] = psiend


t = 0.0
D = h*v**2 / (a*a)
while t<tend:

    
    
    for i in range(1,N):
        phip[i] = phi[i] + h*psi[i]
        psip[i] = psi[i] + D*(phi[i+1]+phi[i-1]-2*phi[i])
     
    phip[1:N] = phi[1:N] + h*psi[1:N]
    psip[1:N] = psi[1:N] + D*(phi[0:N-1] + phi[2:N+1] -2*phi[1:N])
    phi= copy(phip)
    psi= copy(psip)
    phi,phip = phip,phi
    psi,psip = psip,psi
    t += h

    
    if abs(t-t2)<epsilon:
        t2array = copy(phi)
        title('Vibraçao da corda usando FTCS em 2ms')
        xlabel("x")
        ylabel("phi")
        plot(phi, label = "2 ms")
        savefig("phi2ms.png")
        show()
    if abs(t-t50)<epsilon:
        t50array = copy(phi)
        title('Vibraçao da corda usando FTCS em 50ms')
        xlabel("x")
        ylabel("phi")
        plot(phi, label = "50 ms")
        savefig("phi50ms.png")
        show()
    if abs(t-t100)<epsilon:
        t100array = copy(phi)
        title('Vibraçao da corda usando FTCS em 100ms')
        xlabel("x")
        ylabel("phi")
        plot(phi, label = "100 ms")
        savefig("phi100ms.png")
        show()