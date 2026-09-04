#Autor: Pablo Gullith
#Bibliotecas
from pathlib import Path
from numpy import floor, linspace, array, zeros, copy, loadtxt
from scipy.fftpack import rfft, irfft, dct, idct
from pylab import plot, show, xlabel, ylabel, savefig

dow2 = loadtxt(Path(__file__).with_name("dow2.txt"), float)
plot(dow2)
xlabel('k')
ylabel('Amplitude')
savefig("dow2.png")
show()


dow2_fourier = rfft(dow2)
N = len(dow2_fourier)
Primeiros_2_porcento = zeros(N, float)
Primeiros_2_porcento[0 : int(N / 50)] = copy(dow2_fourier[0 : int(N / 50)])
Suavizada_dow2 = irfft(Primeiros_2_porcento)


dow2_cos = dct(dow2)
n = len(dow2_cos)
Primeiros_cos_2_porcento = zeros(n, float)
Primeiros_cos_2_porcento[0 : int(n / 50)] = copy(dow2_cos[0 : int(n / 50)])
Suavizada_cos_dow2 = idct(Primeiros_cos_2_porcento) / (2*n) 

plot(dow2, 'k')
plot(Suavizada_dow2, 'g')
xlabel('k')
ylabel('Amplitude')
savefig("dow2_Suavizada_dow2.png")
show()
plot(dow2, 'k')
plot(Suavizada_cos_dow2, 'r')
xlabel('k')
ylabel('Amplitude')
savefig("dow2_Suavizada_cos_dow2.png")
show()