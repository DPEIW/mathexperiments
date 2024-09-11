import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Slider

# Constants for the arm length
L1, L2, L3 = 2, 2, 1.5  # Lengths of the arm segments

# Function to compute forward kinematics
def forward_kinematics(theta1, theta2, theta3):
    # Convert angles to radians
    theta1, theta2, theta3 = np.radians([theta1, theta2, theta3])
    
    # Position of the first joint
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)
    z1 = 0  # Fixed base in the XY plane
    
    # Position of the second joint
    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)
    z2 = 0  # Fixed base in the XY plane
    
    # Position of the end effector
    x3 = x2 + L3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3 * np.sin(theta1 + theta2 + theta3)
    z3 = 0  # Fixed base in the XY plane
    
    return (0, x1, x2, x3), (0, y1, y2, y3), (0, z1, z2, z3)

# Function to update the plot
def update(val):
    theta1 = s_theta1.val
    theta2 = s_theta2.val
    theta3 = s_theta3.val
    
    # Compute forward kinematics
    x, y, z = forward_kinematics(theta1, theta2, theta3)
    
    # Update the plot
    arm.set_data(x, y)
    arm.set_3d_properties(z)
    plt.draw()

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.25)

# Initial angles
theta1_init = 30
theta2_init = 45
theta3_init = 60

# Compute initial positions
x, y, z = forward_kinematics(theta1_init, theta2_init, theta3_init)

# Plot initial arm position
arm, = ax.plot(x, y, z, '-o', markersize=8, color='blue')

# Axes limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Sliders for joint angles
axcolor = 'lightgoldenrodyellow'
ax_theta1 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_theta2 = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_theta3 = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)

s_theta1 = Slider(ax_theta1, 'Theta1', -180, 180, valinit=theta1_init)
s_theta2 = Slider(ax_theta2, 'Theta2', -180, 180, valinit=theta2_init)
s_theta3 = Slider(ax_theta3, 'Theta3', -180, 180, valinit=theta3_init)

# Update plot on slider change
s_theta1.on_changed(update)
s_theta2.on_changed(update)
s_theta3.on_changed(update)

plt.show()

