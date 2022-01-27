import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#all distances measured in moon-radii, all masses measured in moon-masses

Omega = 2.6615e-6 #moon angular frequency
R0 = 222 #distance of moon
Me = 83.3 #earth mass
G = 9.63e-7
pi = np.pi

final_time = 2000000
dt = 100
t = np.linspace(0, final_time, int(final_time / dt))


def a(Rr: np.ndarray, Rm: np.ndarray):
    '''Calculates acceleration of rocket'''

    return -G * (
        (Me * Rr / (np.linalg.norm(Rr) ** 3))
        + ((Rr - Rm) / (np.linalg.norm(Rr - Rm) ** 3))
    )


def moon_pos_2(t):
    '''Orbiting moon position'''
    return R0 * np.array([np.cos(Omega * t), np.sin(Omega * t)])


def moon_pos_1(t):
    '''stationary moon position'''
    return np.array([0, R0])


def simulate_rocket(init_pos, init_vel, moon_pos, times):
    '''simulates rocket position using Improved Euler Method'''

    Rr = init_pos #rocket position vector
    Vr = init_vel #rocket velocity vector
    dt = times[1] - times[0]

    tout = times
    pos = np.zeros((len(times), 2))

    for i, t in enumerate(times):
        Rm = moon_pos(t)

        Rr_prime = Rr + dt * Vr

        Vr_prime = Vr + dt / 2 * (a(Rr, Rm) + a(Rr_prime, Rm))

        Rr = Rr + dt / 2 * (Vr + Vr_prime)

        Vr = Vr_prime

        pos[i] = Rr

        if np.linalg.norm(Rr - Rm) < 1:
            #if rocket has reached the moon, end the simulation
            tout = times[1:i]
            pos = pos[1:i]
            break

    return (tout, pos)


#52.2 degrees leads to a collision
theta = 52.2 * pi / 180 

init_pos = np.array([0, 3.7])
init_vel = 0.0066 * np.array([np.cos(theta), np.sin(theta)])


tout, pos = simulate_rocket(init_pos, init_vel, moon_pos_2, t)



# configure matplotlib
fig = plt.figure()
ax = fig.add_subplot(
    xlim=(-20, 260),
    ylim=(-20, 260),
)
ax.grid()

(moon,) = ax.plot([], [], "o-", linewidth=2)
(rocket,) = ax.plot([], [], "o-", linewidth=2)
(rocket_trace,) = ax.plot([], [], linewidth=2, markersize=2)


def animate(i):
    x, y = pos[i]
    moonx, moony = moon_pos_2(t[i])

    moon.set_data(moonx, moony)
    rocket.set_data(x, y)

    if i:
        rocket_trace.set_data(*pos.T[:, : i + 1])
    else:
        rocket_trace.set_data(*pos[:1])

    return rocket, moon, rocket_trace


ani = FuncAnimation(fig, animate, len(tout), interval=0.01, blit=True)
plt.show()
