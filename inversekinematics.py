import numpy as np
import matplotlib.pyplot as plt

# Arm segment lengths
L1, L2, L3 = 2, 2, 1.5

def inverse_kinematics(x_target, y_target):
    # Calculate the distance from the origin to the target point
    r = np.sqrt(x_target**2 + y_target**2)
    
    # Ensure the target is reachable
    if r > L1 + L2 + L3:
        print("Target is out of reach!")
        return 0, 0, 0
    
    # Law of cosines to find theta3
    cos_theta3 = (r**2 - L1**2 - L2**2) / (2 * L1 * L2)
    cos_theta3 = np.clip(cos_theta3, -1.0, 1.0)  # Clamping to prevent errors
    theta3 = np.arccos(cos_theta3)

    # Law of sines to find theta2
    k1 = L1 + L2 * cos_theta3
    k2 = L2 * np.sqrt(1 - cos_theta3**2)
    theta2 = np.arctan2(y_target, x_target) - np.arctan2(k2, k1)

    # Theta1
    theta1 = np.arctan2(y_target, x_target)

    # Convert to degrees
    theta1, theta2, theta3 = np.degrees([theta1, theta2, theta3])

    return theta1, theta2, theta3

def forward_kinematics(theta1, theta2, theta3):
    # Convert to radians
    theta1, theta2, theta3 = np.radians([theta1, theta2, theta3])

    # Joint positions
    x1 = L1 * np.cos(theta1)
    y1 = L1 * np.sin(theta1)

    x2 = x1 + L2 * np.cos(theta1 + theta2)
    y2 = y1 + L2 * np.sin(theta1 + theta2)

    x3 = x2 + L3 * np.cos(theta1 + theta2 + theta3)
    y3 = y2 + L3 * np.sin(theta1 + theta2 + theta3)

    return (0, x1, x2, x3), (0, y1, y2, y3)

def update_arm(x_target, y_target):
    # Compute inverse kinematics to find angles
    theta1, theta2, theta3 = inverse_kinematics(x_target, y_target)

    # Compute forward kinematics for plotting
    x, y = forward_kinematics(theta1, theta2, theta3)

    # Update plot
    arm.set_data(x, y)
    end_effector.set_data(x[-1], y[-1])
    ax.set_xlim(-max_reach, max_reach)
    ax.set_ylim(-max_reach, max_reach)
    plt.draw()

def on_press(event):
    if event.inaxes != ax:
        return
    
    # Distance from click to end effector
    x_target, y_target = event.xdata, event.ydata
    dist = np.sqrt((x_target - x[3])**2 + (y_target - y[3])**2)
    
    if dist < 0.1:  # If click is close to end effector
        dragging[0] = True

def on_release(event):
    dragging[0] = False

def on_motion(event):
    if dragging[0] and event.inaxes == ax:
        x_target, y_target = event.xdata, event.ydata
        update_arm(x_target, y_target)

# Calculate maximum reach
max_reach = L1 + L2 + L3

# Initial setup
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
dragging = [False]

# Initial target position
x_target_init, y_target_init = 3, 3

# Compute initial angles
theta1_init, theta2_init, theta3_init = inverse_kinematics(x_target_init, y_target_init)
x, y = forward_kinematics(theta1_init, theta2_init, theta3_init)

# Plot the arm and end effector
arm, = ax.plot(x, y, '-o', markersize=8, color='blue')
end_effector, = ax.plot(x[-1], y[-1], 'ro', markersize=10)  # End effector as a red dot
ax.set_xlim(-max_reach, max_reach)
ax.set_ylim(-max_reach, max_reach)
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Connect the event handlers
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

plt.show()
