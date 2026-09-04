# Autor: Pablo Gullith
# Bibliotecas
from pathlib import Path
from numpy import loadtxt, exp, empty, real
from scipy.fftpack import fft2, ifft2
from pylab import imshow, plot, show, gray, savefig
from numpy.fft import rfft2, irfft2

# Constantes
sigma = 25
Foto_borrada = loadtxt(Path(__file__).with_name("blur.txt"), float)


gray()
imshow(Foto_borrada)
savefig("Foto_borrada.png")
show()

y_dim, x_dim = Foto_borrada.shape


def Ponto_de_Propagacao(x, y):
    return exp(-(x**2 + y**2) / (2 * sigma**2))


# Calcular a função de propagação de pontos para cada ponto
Ponto_de_Propagacao_array = empty([y_dim, x_dim], float)
for i in range(y_dim):
    for j in range(x_dim):
        Ponto_de_Propagacao_array[i, j] = Ponto_de_Propagacao(
            (j + y_dim / 2) % y_dim - y_dim / 2, (i + x_dim / 2) % x_dim - x_dim / 2
        )

Foto_borrada_fourier = rfft2(Foto_borrada)
Ponto_de_Propagacao_fourier = rfft2(Ponto_de_Propagacao_array)


Nao_borrada_fourier = empty([y_dim, x_dim // 2 + 1], complex)
epsilon = 10**-4
for i in range(x_dim // 2 + 1):
    for j in range(y_dim):
        if abs(Ponto_de_Propagacao_fourier[j, i]) < epsilon:
            Nao_borrada_fourier[j, i] = Foto_borrada_fourier[j, i]
        else:

            Nao_borrada_fourier[j, i] = Foto_borrada_fourier[j, i] / (
                Ponto_de_Propagacao_fourier[j, i]
            )

imshow(irfft2(Ponto_de_Propagacao_fourier))
gray()
savefig("Ponto_de_Propagacao.png")
show()


imshow(irfft2(Nao_borrada_fourier))
gray()
savefig("Nao_borrada.png")
show()
