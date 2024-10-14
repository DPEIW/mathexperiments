import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the Lorenz attractor
sigma = 10
rho = 28
beta = 8 / 3

# Lorenz system differential equations
def lorenz(x, y, z, sigma=sigma, rho=rho, beta=beta):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# Time parameters
dt = 0.01
num_steps = 10000  # Number of iterations

# Arrays to hold the points
xs = np.zeros(num_steps)
ys = np.zeros(num_steps)
zs = np.zeros(num_steps)

# Initial conditions
xs[0], ys[0], zs[0] = 1.0, 1.0, 1.0

# Integrating the Lorenz equations
for i in range(1, num_steps):
    dx_dt, dy_dt, dz_dt = lorenz(xs[i - 1], ys[i - 1], zs[i - 1])
    xs[i] = xs[i - 1] + dx_dt * dt
    ys[i] = ys[i - 1] + dy_dt * dt
    zs[i] = zs[i - 1] + dz_dt * dt

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Lorenz attractor
ax.plot(xs, ys, zs, lw=0.5)

# Labels and title
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")

plt.show()
