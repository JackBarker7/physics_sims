import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp


tmax = 50
dt = 0.01


def van_der_pol(t, z, gamma=1):
    """van der Pol equation. z is a 2x1 array of the form [x, dx/dt]
    returns [dx/dt, d2x/dt2]"""
    x, y = z  # y=dx/dt

    xdot = y
    ydot = -x + y * gamma * (1 - x ** 2)

    return [xdot, ydot]


# solve ode
solver = solve_ivp(van_der_pol, [0, tmax], [0, 0.001], dense_output=True)
times = np.arange(0, tmax, dt)
out_arr = solver.sol(times)


# configure matplotlib
fig = plt.figure()
ax = fig.add_subplot(
    xlim=(0, tmax),
    ylim=(1.1 * min(out_arr[0]), 1.1 * max(out_arr[0])),
)
ax.grid()

(point,) = ax.plot([], [], "o-", linewidth=2)
(trace,) = ax.plot([], [], linewidth=2, markersize=2)


def animate(i):
    point.set_data(times[i], out_arr[0][i])

    if i:
        trace.set_data(times[:i], out_arr[0][:i])
    else:
        trace.set_data(times[i], out_arr[0][1])

    return point, trace


ani = FuncAnimation(fig, animate, len(times), interval=dt * 100, blit=True)
plt.xlabel("time")
plt.ylabel("displacement")
plt.title("Displacement of Van der Pol Oscillator")
plt.show()
