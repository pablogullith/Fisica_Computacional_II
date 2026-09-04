# Autor: JOAB MORAIS VARELA '-'
# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randrange

passo = 0.005
tempototal = 100
quantidade = int(tempototal / passo)

fig = plt.figure()
ax = fig.add_subplot(111)
(ponto,) = ax.plot([], [], "ko")
ax.set_ylim(0, 101)
ax.set_xlim(0, 101)
ax.grid()
xdata, ydata = [], []


def f(passo, quantidade):
    y = 51
    x = 51

    for i in range(quantidade):
        if x == 101 and y != 101:
            y = randrange(y - 1, y + 2)
            x = randrange(x - 1, x + 1)
            yield y, x
        elif x == 0 and y != 0:
            y = randrange(y - 1, y + 2)
            x = randrange(x, x + 2)
            yield y, x
        elif y == 101 and x != 101:
            y = randrange(y - 1, y + 1)
            x = randrange(x - 1, x + 2)
            yield y, x
        elif y == 0 and x != 0:
            y = randrange(y, y + 2)
            x = randrange(x - 1, x + 2)
            yield y, x
        elif y == 0 and x == 0:
            y = randrange(y, y + 2)
            x = randrange(x, x + 2)
            yield y, x
        elif y == 101 and x == 101:
            y = randrange(y - 1, y + 1)
            x = randrange(x - 1, x + 1)
            yield y, x
        elif y == 101 and x == 0:
            y = randrange(y - 1, y + 1)
            x = randrange(x, x + 2)
            yield y, x
        elif y == 0 and x == 101:
            y = randrange(y, y + 2)
            x = randrange(x - 1, x + 1)
            yield y, x
        else:
            y = randrange(y - 1, y + 2)
            x = randrange(x - 1, x + 2)
            yield y, x


def passagem(data):
    X, Y = data
    xdata.append(X)
    ydata.append(Y)
    xmin, xmax = ax.get_xlim()
    ponto.set_data([X], [Y])
    return (ponto,)


ani = animation.FuncAnimation(
    fig,
    passagem,
    f(passo, quantidade),
    blit=True,
    interval=30,
    repeat=False,
    cache_frame_data=False,
)
plt.title("Caminhada Aleatória")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("caminhada_aleatoria.png")
plt.show()

# Se quiser aumentar a velocidade, mude o valor de interval: ex interval = 10
