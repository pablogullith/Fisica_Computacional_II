# Autor: Pablo Gullith
# Bibliotecas
from pathlib import Path
from numpy import loadtxt, exp, zeros, pi
from pylab import plot, show, xlabel, ylabel, savefig

sunspot_data = loadtxt(Path(__file__).with_name("sunspots.txt"), float)
tempo = sunspot_data[:, 0]
Manchas_Solares = sunspot_data[:, 1]

# Plotando as manchas solares
plot(tempo, Manchas_Solares, "c")
xlabel("Número de meses desde Janeiro de 1749")
ylabel("Número de manchas solares")
savefig("sunspots.png")
show()


def Transformada_Discreta_Fourier(y):
    N = len(y)
    c = zeros(N // 2 + 1, complex)
    for k in range(N // 2 + 1):
        for n in range(N):
            c[k] += y[n] * exp(-2j * pi * k * n / N)
    return c


# Transformada de fourier com os dados de manchas solares
fourier_data = Transformada_Discreta_Fourier(Manchas_Solares)


def Magnitude_ao_Quadrado(a):
    return abs(a) ** 2


plot(list(map(Magnitude_ao_Quadrado, fourier_data)))
xlabel("Frequency")
ylabel("Magnitude")
savefig("fourier_transform.png")
show()

# Olhando o gráfico e dando zoom no maior pico, observamos que o valor de k tido pela amplitude mais proeminente é 24.
# Temos o periodo dado em meses: 130.91666
