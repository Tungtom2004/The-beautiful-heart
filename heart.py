import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import*

# Set up the figure, axis, and plot element
fig, ax = plt.subplots()
x = np.linspace(-sqrt(pi), sqrt(pi), 1000)
ax.set_xlim(-2, 2)
ax.set_ylim(-1.5, 3)
points, = ax.plot([], [], 'r-')

def init():
    points.set_data([], [])
    return points,

# Update function
def update(frame):
    y = np.power(x ** 2, 1 / 3) + e / 3 * (pi - x ** 2) ** 0.5 * np.sin(frame * pi * x / 10)
    points.set_data(x, y)
    return points,


# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 301), init_func=init, blit=True, interval=50,
                              repeat=False)

plt.show()