import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-whitegrid")

# l = 500e-9
l = 630e-9  # wavelength
a = 1 #amplitude
v = 3e8 #wave speed
number_of_slits = 100
slit_separation = 1e-5
slit_width = 0.0001
sources_per_slit = 10
pi = np.pi


def f(x):
    """returns value of wave"""
    return a * np.sin(2 * pi * x / l)


def generateSources(n, slit_separation, slit_width, sources_per_slit):
    """Generates n slits of width slit_width, with centres separated by a distance slit_separation, with sources_per_slit sources per slit"""

    # generate position
    sources = np.zeros((n, sources_per_slit))

    for i in range(n):
        slit_centre = (-(n - 1) * slit_separation / 2) + i * slit_separation

        for j in range(sources_per_slit):
            if sources_per_slit == 1:
                # special case of one source per slit
                sources[i] = slit_centre

            elif sources_per_slit % 2:
                # odd
                sources[i][j] = (slit_centre - slit_width / 2) + j * (
                    slit_width / (sources_per_slit - 1)
                )

            else:
                # even
                sources[i][j] = (slit_centre - slit_width / 2) + (j + 0.5) * (
                    slit_width / (sources_per_slit)
                )

    # convert into 1D array
    sources = sources.reshape(n * sources_per_slit)
    actual_sources = np.zeros((n * sources_per_slit, 2))
    for k in range(n * sources_per_slit):
        actual_sources[k] = [sources[k], 0]

    return actual_sources


def generateIntensity(
    screen_distance,
    screen_width,
    dx,
    number_of_slits=number_of_slits,
    slit_separation=slit_separation,
    slit_width=slit_width,
    sources_per_slit=sources_per_slit,
):
    """Generates intensiy values"""
    sources = generateSources(
        number_of_slits, slit_separation, slit_width, sources_per_slit
    )  # source locations

    # generate array holding all test points
    x_points = np.linspace(
        -screen_width / 2, screen_width / 2, num=int(screen_width / dx)
    )
    points = np.zeros((len(x_points), 2))
    for i in range(len(x_points)):
        points[i][0] = x_points[i]
        points[i][1] = screen_distance

    # calculate intensities
    intensities = np.zeros(int(screen_width / dx))
    for i in range(int(screen_width / dx)):  # for each point to measure intensity at
        for j in range(number_of_slits * sources_per_slit):  # for each source
            intensities[+i] += f(np.linalg.norm(points[i] - sources[j]))
            intensities[i] = abs(intensities[i])

    plt.scatter(x_points, intensities, marker=".")
    plt.show()


# generateIntensity(2.25,25, 0.001)
# generateIntensity(3.352,10,0.0001, 2, 1e-3, 1e-5, 100) #double slit
generateIntensity(3.5, 0.1, 0.0001, 1, 1e-3, 1e-3, 1000)
