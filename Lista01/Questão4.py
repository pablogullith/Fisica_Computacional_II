#Autor: Pablo Gullith
#Bibliotecas:
from pathlib import Path
from numpy import loadtxt, zeros, copy, floor
from scipy.fftpack import rfft, irfft
from pylab import plot, show, xlabel, ylabel, savefig

dow = loadtxt(Path(__file__).with_name("dow.txt"), float)
plot(dow)
xlabel('k')
ylabel('Amplitude')
savefig("dow.png")
show()

dow_fourier = rfft(dow)
N = len(dow_fourier)
Primeiros_10_porcento = zeros(N, float)
Primeiros_10_porcento[0 : int(N / 10)] = copy(dow_fourier[0 : int(N / 10)])
dow_Primeiros_10_porcento = irfft(Primeiros_10_porcento)
Primeiros_2_porcento = zeros(N, float)
Primeiros_2_porcento[0 : int(N / 50)] = copy(dow_fourier[0 : int(N / 50)])
dow_Primeiros_2_porcento =irfft(Primeiros_2_porcento)

plot(dow, 'k')
plot(dow_Primeiros_10_porcento, 'b')
xlabel('k')
ylabel('Amplitude')
savefig("dow_Primeiros_10_porcento.png")
show()
plot(dow, 'k')
plot(dow_Primeiros_2_porcento, 'r')
xlabel('k')
ylabel('Amplitude')
savefig("dow_Primeiros_2_porcento.png")
show()