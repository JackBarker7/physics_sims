import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp
import oscillators

# define the oscillator to be used
args = (5, 2, 3, 4)
oscillator = lambda t, z: oscillators.cartwright_littlewood(t, z, *args)
initial = [10, 10]


tmax = 500
dt = 0.01


# solve ode
solver = solve_ivp(oscillator, [0, tmax], initial, dense_output=True)
times = np.arange(0, tmax, dt)
out_arr = solver.sol(times)


# configure matplotlib
fig = plt.figure()
ax = fig.add_subplot(
    xlim=(1.1 * min(out_arr[0]), 1.1 * max(out_arr[0])),
    ylim=(1.1 * min(out_arr[1]), 1.1 * max(out_arr[1])),
)
ax.grid()

(point,) = ax.plot([], [], "o-", linewidth=2)
(trace,) = ax.plot([], [], linewidth=2, markersize=2)


def animate(i):
    x, y = out_arr.T[i]
    point.set_data(x, y)

    if i:
        trace.set_data(*out_arr.T[: i + 1].T)
    else:
        trace.set_data(*out_arr.T[:1])

    return point, trace


ani = FuncAnimation(fig, animate, len(times), interval=dt * 100, blit=True)
plt.xlabel("position")
plt.ylabel("velocity")
plt.title("Phase portrait")
plt.show()
