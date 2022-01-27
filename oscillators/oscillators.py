import numpy as np


def van_der_pol(t, z, gamma=1):
    """Van der Pol equation. z is a 2x1 array of the form [x, dx/dt]
    returns [dx/dt, d2x/dt2]"""
    x, y = z  # y=dx/dt

    xdot = y
    ydot = -x + y * gamma * (1 - x ** 2)

    return [xdot, ydot]


def anosov(t, z, gamma=1):
    """Anosov's equation. z is a 2x1 array of the form [x, dx/dt]
    returns [dx/dt, d2x/dt2]"""
    x, y = z  # y=dx/dt

    xdot = y
    ydot = -x + y * gamma * (1 - x ** 2 - y ** 2)

    return [xdot, ydot]


def lotka_volterra(t, z, a, b, c, d):
    """Lotka-Volterra equation. z is a 2x1 array of the form [x, y]
    returns [dx/dt, dy/dt]"""

    x, y = z
    xdot = a * x - b * x * y
    ydot = d * x * y - c * y

    return [xdot, ydot]

def cartwright_littlewood(t, z, k, b, l, a):
    """Equation studeid by Cartwright and Littlewood in their 1945 paper
    z is a 2x1 array of the form [x, dx/dt]"""

    x, y=z

    xdot = y
    ydot = b*l*k*np.cos(l*t+a)-x+k*y*(1-y**2)

    return [xdot, ydot]



if __name__ == '__main__':
    print("Run other files")
