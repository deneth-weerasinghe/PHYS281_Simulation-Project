import numpy as np
import copy
import os
import matplotlib.pyplot as plt
from base_classes.Particle import Particle
from base_classes.SimpleGraphPlot import SimpleGraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def satellite_system_objects():
    """
    Creates a simple preset of a two-body gravitational system, consisting of Earth and a satellite
    :return:
    """
    earth_mass = 5.97237e24  # https://en.wikipedia.org/wiki/Earth
    earth_radius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth
    earth = Particle(
        position=np.array([0, 0, 0]),
        velocity=np.array([0, 0, 0]),
        acceleration=np.array([0, 0, 0]),
        name="Earth",
        mass=earth_mass
    )
    sat_position = earth_radius + (35786 * 1e3)
    sat_velocity = np.sqrt(earth.G * earth.mass / sat_position)  # from centrifugal force = gravitational force
    satellite = Particle(
        position=np.array([sat_position, 0, 0]),
        velocity=np.array([0, sat_velocity, 0]),
        acceleration=np.array([0, 0, 0]),
        name="Satellite",
        mass=100.
    )
    return earth, satellite


def two_bodies_simulation_loop(delta_t, iterations, object_1, object_2, t=0):
    data = []  # list to store contents that will be written to "TwoBodyTest.npy"#
    times = []  # list storing values for the time (x axis) of the plot
    positions = []  # list storing values for the position (y axis) of the satellite

    for i in range(1, (3600 * 24 * 4 + 1)):

        t += delta_t

        object_1.updateGravitationalAcceleration(object_2)
        object_2.updateGravitationalAcceleration(object_1)

        object_1.updateEuler(delta_t)
        object_2.updateEuler(delta_t)

        if (i - 1) % 100 == 0:  # which values of i should be considered when storing data
            data.append([t, copy.deepcopy(object_1), copy.deepcopy(object_2)])

            # times.append(t)
            # positions.append(Satellite.position.copy())


Earth, Satellite = satellite_system_objects()

plt.legend()
plt.show()
