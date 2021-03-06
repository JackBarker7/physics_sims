import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def E(x, y, z, t):
    '''Electric field vector as a function of position and time'''
    return np.array([1 / x, 1 / y, 1 / z])


def B(x, y, z, t):
    '''Magnetic field vector as a function of position and time'''
    return np.array([y, z, x])


q = 1
c = 1
m = 1

dt = 0.001
tmax = 10
times = np.linspace(0, 100, int(tmax / dt))

accs = np.zeros((len(times), 3))
vels = np.zeros((len(times), 3))
poss = np.zeros((len(times), 3))


def F(pos, vel, t):
    return q * (E(*pos, t) + (1 / c) * np.cross(vel, B(*pos, t)))


vels[0] = np.array([0, 0, 0])
poss[0] = np.array([0.1, 0.5, 1])
accs[0] = F(poss[0], vels[0], 0)

for i in range(0, len(times) - 1):
    accs[i + 1] = F(poss[i], vels[i], times[i]) / m
    vels[i + 1] = vels[i] + accs[i + 1] * dt
    poss[i + 1] = poss[i] + vels[i + 1] * dt


fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot(*poss.transpose())

ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
