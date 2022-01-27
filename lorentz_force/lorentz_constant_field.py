import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

E = np.array([0, 1, 2])
B = np.array([0.5, 0, 1])
q = 1
c = 1
m = 1

dt = 0.001
tmax = 10
times = np.linspace(0, 100, int(tmax / dt))

accs = np.zeros((len(times), 3))
vels = np.zeros((len(times), 3))
poss = np.zeros((len(times), 3))


def F(v: np.ndarray):
    return q * (E + (1 / c) * np.cross(v, B))


vels[0] = np.array([0, 0, 0])
poss[0] = np.array([0, 0, 0])
accs[0] = F(vels[0])

for i in range(0, len(times) - 1):
    accs[i + 1] = F(vels[i]) / m
    vels[i + 1] = vels[i] + accs[i + 1] * dt
    poss[i + 1] = poss[i] + vels[i + 1] * dt


print(vels)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot(*poss.transpose())

ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
