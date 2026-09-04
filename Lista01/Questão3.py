#Autor:Pablo Gullith
#Bibliotecas
from pathlib import Path
from scipy.fftpack import fft
from numpy import loadtxt
from pylab import plot, show, xlabel, ylabel, savefig

piano_data = loadtxt(Path(__file__).with_name("piano.txt"), float)
trumpet_data = loadtxt(Path(__file__).with_name("trumpet.txt"), float)
plot(piano_data)
xlabel('k')
ylabel('Amplitude')
savefig('piano.png')
show()
plot(trumpet_data)
xlabel('k')
ylabel('Amplitude')
savefig('trumpet.png')
show()

piano_fourier = fft(piano_data)
plot(abs(piano_fourier[0:9999]))
xlabel('k')
ylabel('|c_k|')
savefig('piano_fourier.png')
show()

trumpet_fourier = fft(trumpet_data)
plot(abs(trumpet_fourier[0:9999]))
xlabel('k')
ylabel('|c_k|')
savefig('trumpet_fourier.png')
show()
