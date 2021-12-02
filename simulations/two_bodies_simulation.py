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


def two_bodies_euler_loop(delta_t, iterations, object_1, object_2, file, t=0):
    data = []  # list to store contents that will be written to "TwoBodyTest.npy"#

    for i in range(1, iterations + 1):

        t += delta_t

        object_1_g = object_1.twoBodiesAcceleration(object_2)
        object_2_g = object_2.twoBodiesAcceleration(object_1)

        object_1.setAcceleration(object_1_g)
        object_2.setAcceleration(object_2_g)

        object_1.updateEuler(delta_t)
        object_2.updateEuler(delta_t)

        if (i - 1) % 100 == 0:  # which values of i should be considered when storing data
            data.append([t, copy.deepcopy(object_1), copy.deepcopy(object_2)])

    np.save(new_path + file, data, allow_pickle=True)


def two_bodies_euler_cromer_loop(delta_t, iterations, object_1, object_2, file, t=0):
    data = []  # list to store contents that will be written to "TwoBodyTest.npy"

    for i in range(1, iterations + 1):

        t += delta_t

        object_1_g = object_1.twoBodiesAcceleration(object_2)
        object_2_g = object_2.twoBodiesAcceleration(object_1)

        object_1.setAcceleration(object_1_g)
        object_2.setAcceleration(object_2_g)

        object_1.updateEulerCromer(delta_t)
        object_2.updateEulerCromer(delta_t)

        if (i - 1) % 100 == 0:  # which values of i should be considered when storing data
            data.append([t, copy.deepcopy(object_1), copy.deepcopy(object_2)])

    np.save(new_path + file, data, allow_pickle=True)


def retrieve_data(file, s):
    data = np.load(file, allow_pickle=True)
    times = []
    positions = []
    for i in data:
        times.append(i[0])
        positions.append(i[s].position)
    return times, positions


Earth, satellite_1 = satellite_system_objects()
two_bodies_euler_loop(1, 3600 * 24 * 4, Earth, satellite_1, "/TwoBodyTest")

Earth_2, satellite_2 = satellite_system_objects()
two_bodies_euler_cromer_loop(1, 3600 * 24 * 4, Earth_2, satellite_2, "/CromerTest")


sat_1_times, sat_1_pos = retrieve_data(new_path + "/TwoBodyTest.npy", 2)
sat_2_times, sat_2_pos = retrieve_data(new_path + "/CromerTest.npy", 2)

satellite_x_y = SimpleGraphPlot(sat_1_times, sat_1_pos)
satellite_x_y_2 = SimpleGraphPlot(sat_2_times, sat_2_pos)
satellite_x_y.draw2DPositionGraph(color="r", label="Euler")
satellite_x_y_2.draw2DPositionGraph(color="b", label="Euler Cromer")
plt.legend()
plt.show()