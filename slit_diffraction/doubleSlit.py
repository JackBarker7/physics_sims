import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")

pi = np.pi


l = [500e-9, 500e-9]  # wavelength
a = [1, 1]  # amplitude
v = [3e8, 3e8]  # wave speed
phi = [0, np.pi]  # phase shift
separation = 3e-6  # slit separation


def f(x, t, i):
    """Returns value of wave. x=distance from source, t=time, i=souce number (0 or 1)"""
    return a[i] * np.sin((2 * pi / l[i]) * (x - (v[i] * t)) - phi[i])


def normalDoubleSlit(separation, screen_width, screen_distance, dx):
    # define source points
    s1 = np.array([-separation / 2, 0])
    s2 = np.array([separation / 2, 0])
    # array to hold intensity values
    intensity_measurements = np.zeros(int(screen_width / dx))
    for i in range(int(screen_width / dx)):

        measure = [(-screen_width / 2) + i * dx, screen_distance]  # point to measure at
        # distance from sources to point
        s1_distance = np.linalg.norm(s1 - measure)
        s2_distance = np.linalg.norm(s2 - measure)

        intensity_measurements[i] = f(s1_distance, 0, 0) + f(s2_distance, 0, 1)

    points = np.linspace(-screen_width / 2, screen_width / 2, int(screen_width / dx))
    plt.scatter(points, intensity_measurements, marker=".")
    plt.show()


normalDoubleSlit(separation, 10, 3, 0.0001)
