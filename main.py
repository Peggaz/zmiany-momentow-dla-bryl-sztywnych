import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class RigidBody:
    def __init__(self, mass, initial_velocity, initial_angular_velocity):
        self.mass = mass
        self.velocity = initial_velocity
        self.angular_velocity = initial_angular_velocity
    
    def change_in_momentum(self, time_interval):
        return self.mass * self.velocity * time_interval
    
    def change_in_angular_momentum(self, time_interval):
        return self.mass * self.angular_velocity * time_interval
    
def visualize_3d(material_name, data):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    time = np.linspace(0, 10, len(data))
    ax.plot(time, data, range(len(data)))
    
    ax.set_xlabel('Time')
    ax.set_ylabel('Change in Momentum')
    ax.set_zlabel('Step')
    ax.set_title(f'Change in Momentum for {material_name}')
    
    plt.show()

# Define rigid bodies for steel and aluminum
steel = RigidBody(mass=10, initial_velocity=5, initial_angular_velocity=2)
aluminium = RigidBody(mass=8, initial_velocity=7, initial_angular_velocity=3)

# Calculate change in momentum over time
time_interval = 0.1
num_time_steps = 100
steel_momentum_changes = [steel.change_in_momentum(time_interval) for _ in range(num_time_steps)]
aluminium_momentum_changes = [aluminium.change_in_momentum(time_interval) for _ in range(num_time_steps)]

# Visualize the change in momentum in 3D for steel and aluminum
visualize_3d("Steel", steel_momentum_changes)
visualize_3d("Aluminium", aluminium_momentum_changes)
