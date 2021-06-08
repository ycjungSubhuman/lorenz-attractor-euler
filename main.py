# Code reference: https://en.wikipedia.org/wiki/Lorenz_system#Python_simulation

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def f(t, _y):
    x, y, z = _y  # Unpack the state vector
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]  # Derivatives

def solve_euler(f, ts, state0):
    result = np.zeros([len(state0), len(ts)])
    y = state0.copy()
    t0 = 0
    for i, t in enumerate(ts):
        result[:, i] = y
        delta = np.array(f(t, y))
        y += (t-t0)*delta
        t0 = t

    return result

state0 = [1.0, 1.0, 1.0]
ts = np.arange(0, 40, 0.01)

res = solve_ivp(f, (0, 40), state0, method='RK45', t_eval=ts)
y_rk = res.y
y_euler = solve_euler(f, ts, state0)

errors = np.linalg.norm(y_euler - y_rk, axis=0)

plt.figure(figsize=(20, 60))
plt.subplot(3, 1, 1, projection='3d')
plt.title('Runge-Kutta')
plt.plot(y_rk[0,:], y_rk[1,:], y_rk[2,:])

plt.subplot(3, 1, 2, projection='3d')
plt.title('Euler')
plt.plot(y_euler[0,:], y_euler[1,:], y_euler[2,:])

plt.subplot(3, 1, 3)
plt.title('Error (L2 distance of each time point)')
plt.plot(ts, errors)

plt.draw()
plt.show()
