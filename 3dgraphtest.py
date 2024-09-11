from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the grid for plotting
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Define the equations of the planes
b1, b2, b3 = 10, -5, 15  # Example values for b1, b2, b3

# Calculate the corresponding Z values for each plane
Z1 = (b1 - X - 2*Y) / 4
Z2 = (b2 - 2*X + Y) / 4
Z3 = (b3 - 2*X - Y) / 5

# Plot the planes
ax.plot_surface(X, Y, Z1, color='red', alpha=0.5, label='x + 2y + 4z = b1')
ax.plot_surface(X, Y, Z2, color='green', alpha=0.5, label='2x - y - 4z = b2')
ax.plot_surface(X, Y, Z3, color='blue', alpha=0.5, label='2x + y + 5z = b3')

# Set the title and labels
ax.set_title('3D Planes Plot')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
