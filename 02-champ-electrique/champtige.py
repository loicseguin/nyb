import matplotlib.pyplot as plt

Q = -5e-9
k = 8.99e9
L = 10e-2
d = 6e-2

def E_x(n):
    dx = L / n
    xs = [(i - 1) * dx + dx / 2 for i in range(1, n + 1)]
    kdq = k * Q / n
    E_ix = [kdq / (L + d - xi)**2 for xi in xs]
    return sum(E_ix)

ns = list(range(1, 21))
Es = [E_x(n) for n in ns]

for n, E in zip(ns, Es):
    print("{:5d}{:15.1f}".format(n, E))

plt.plot(ns, Es)
plt.show()
