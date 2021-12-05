import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")


z = np.linspace(0, 1, 100)
x = z * np.sin(20 * z)
y = z * np.cos(20 * z)

plt.plot(x, y, z, label="test plot")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("$\Delta$")
ax.set_title("TEST PLOT")
plt.legend()
plt.show()