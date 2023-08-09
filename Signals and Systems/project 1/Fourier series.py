import numpy as np
import matplotlib.pyplot as plt


tau = 2
T0 = 5
f0 = 1 / T0
w0 = 2 * np.pi * f0

N = 100

a = lambda k: (tau / T0) * np.sinc(k * f0 * tau)

def x(t, N):
    sum = 0
    for k in range(-N, N):
        sum += a(k) * np.exp(1j * k * w0 * t)

    return sum

t_domain = np.linspace(-5, 5, 1000)

x_t = list()

for t in t_domain:
    x_t.append(x(t, N))


plt.plot(t_domain, x_t)
plt.show()