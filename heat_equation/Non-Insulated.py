from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

fig = plt.figure()
ax=fig.gca(projection="3d")
ax.set_title("Non-Insulated Wire")
ax.set_xlabel("Distance along wire")
ax.set_ylabel("Time")
ax.set_zlabel("Temperature")

L = 10
a = 5
T = 10
pi = np.pi
dx = 0.1
dt = 0.1
tmax = 10
sum_val = 100



Cn = np.zeros(sum_val)
for i in range(sum_val):
    n=i+1
    Cn[i] = (4*T/(n*pi)) * np.sin(n*pi/2) * np.sin(n*pi*a/(2*L))

def u(x,t):
    ans = a*T/L
    for n in range(1,sum_val+1,1):
        ans += (Cn[n-1] * np.sin(n*pi*x/L) * np.exp(-n*n*pi*pi*t/(L*L)))
    
    return ans

x = np.linspace(0,L,int(L/dx)+1)
t = np.linspace(0,L,int(tmax/dt)+1)

x,t = np.meshgrid(x,t)
z = u(x,t)

surf = ax.plot_surface(x,t,z,cmap = cm.coolwarm, linewidth=0, antialiased=False, )

plt.show()
