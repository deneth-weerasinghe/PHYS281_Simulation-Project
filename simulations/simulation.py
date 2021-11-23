import numpy as np
import copy
import os
from base_classes.Particle import Particle

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")

earthMass = 5.97237e24  # https://en.wikipedia.org/wiki/Earth
earthRadius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
Earth = Particle(
    position=np.array([0, 0, 0]),
    velocity=np.array([0, 0, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Earth",
    mass=earthMass
)
satPosition = earthRadius + (35786 * 1e3)
satVelocity = np.sqrt(Earth.G * Earth.mass / satPosition)  # from centrifugal force = gravitational force
Satellite = Particle(
    position=np.array([satPosition, 0, 0]),
    velocity=np.array([0, satVelocity, 0]),
    acceleration=np.array([0, 0, 0]),
    name="Satellite",
    mass=100.
)

t = 0
delta_T = 6

Data = []  # list to store contents that will be written to "TwoBodyTest.npy"#

times = []  # list storing values for the time (x axis) of the plot
positions = []  # list storing values for the position (y axis) of the satellite

for i in range(1, 2001):

    times.append(t)
    positions.append(Satellite.position)

    t += delta_T

    Earth.updateGravitationalAcceleration(Satellite)
    Satellite.updateGravitationalAcceleration(Earth)

    Earth.update(delta_T)
    Satellite.update(delta_T)

    if (i - 1) % 100 == 0:  # which values of i should be considered when storing data
        Data.append([t, copy.deepcopy(Earth), copy.deepcopy(Satellite)])

np.save(new_path + "/TwoBodyTest", Data, allow_pickle=True)

for n, i in enumerate(positions):
    f = open(new_path + "/test_data.txt", "w+")
    f.write("# t x y\n")
    to_save = [times[n], i[0], i[1]]
    # print(to_save)
    np.savetxt(f, to_save)
# simple_graph_plot.draw2DPositionGraph(positions)
