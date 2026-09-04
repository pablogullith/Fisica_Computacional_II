#Autor: Pablo Gullith
#Bibliotecas
from numpy import exp, pi, zeros, empty, sin
from pylab import plot, show, savefig, title, xlabel, ylabel

# Constants
N = 1000  # number of sample points

def dft(y):
    N = len(y)
    c = zeros(N // 2 + 1, complex)
    for k in range(N // 2 + 1):
        for n in range(N):
            c[k] += y[n] * exp(-2j * pi * k * n / N)
    return c



square_wave = zeros(1000, complex)
for i in range(1, N // 2):
	square_wave[i] = 1.0
plot(list(map(abs,dft(square_wave))), '-')
savefig('square_wave.png')
title('Square Wave')
xlabel('Frequency')
ylabel('Magnitude')
show()

# Modulated sine wave
mod_sine = empty(N, float)
for n in range(N):
    mod_sine[n] = sin(pi * n / N) * sin(20 * pi * n / N)

plot(list(map(abs,dft(mod_sine))), '-')
savefig('modulated_sine_wave.png')
title('Modulated Sine Wave')
xlabel('Frequency')
ylabel('Magnitude')
show()