#Autor: Pablo Gullith
#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Ising(object):
    J = 1 #Constante de interação
    h = 0
    L = 15
    k_B = 1
    T = 2.0 #Temperatura 
    iterate = 100000 #Número de interações
    ic = 0 
    lattice = np.random.choice([1,-1],size=[L,L])
    
    def magnetizacao(self,lattice):
        
        return np.sum(lattice)/self.L

    def metropolis(self,change_E,y,x,lattice,T):
        
        r = np.random.random()
        if r < np.exp(change_E/(self.k_B*T)):
            lattice[y,x] = -lattice[y,x]
        
        return lattice

    def deltaEnergia(self,y,x):
        
        per = np.empty([self.L+2,self.L+2],dtype=int) 
        per[1:self.L+1,1:self.L+1] = self.lattice
        per[0,1:self.L+1] = self.lattice[self.L-1]
        per[self.L+1,1:self.L+1] = self.lattice[0]
        per[1:self.L+1,0] = self.lattice[:,self.L-1]
        per[1:self.L+1,self.L+1] = self.lattice[:,0]
        
        X = x+1
        Y = y+1
        S_j = per[Y-1,X]+per[Y+1,X]+per[Y,X+1]+per[Y,X-1]
        h_i = self.J*S_j + self.h
        return -2*self.lattice[y,x]*h_i

    
            
    def loop_continuo(self):
        
        while self.ic < self.iterate:
            self.ic += 1
            yield self.ic 

    def atualizar(self,loop_continuo):
               
        y,x = np.random.randint(self.L),np.random.randint(self.L) 
        change_E = self.deltaEnergia(y,x)
        self.lattice = self.metropolis(change_E,y,x,self.lattice,self.T)
        self.im.set_array(self.lattice)

    def animacao(self):
                
        fig = plt.figure()        
        self.im = plt.imshow(self.lattice,interpolation="nearest",animated=1,cmap = plt.cm.Spectral)
        plt.axis('off')
        anim = FuncAnimation(fig,self.atualizar,self.loop_continuo,interval=10,repeat=0)
        plt.tight_layout()     
        plt.show(block=1)

if __name__ == "__main__":
    sim = Ising()  
    sim.animacao()  
	
	
#O que acontece aqui é que quando a temperatura excede a temperatura critíca, o alinhamento global desaparece,
#mas o alinhamento local (ou seja, aglomeração) permanece. Os  aglomerados  são eliminados apenas por flutuações 
#térmicas quando a temperatura é significativamente maior que a temperatura crítica. 	