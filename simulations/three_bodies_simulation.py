import numpy as np
import copy
import os
from base_classes.Particle import Particle

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def satellite_system_objects():
    """
    Creates a simple preset of a three-body gravitational system, consisting of Earth and two satellites
    :return: list of Particle objects
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

    sat_1_position = earth_radius + (35786 * 1e3)
    sat_1_velocity = np.sqrt(earth.G * earth.mass / sat_1_position)  # from centrifugal force = gravitational force

    sat_2_position = earth_radius + (35786 * 1e3) * 2
    sat_2_velocity = np.sqrt(earth.G * earth.mass / sat_2_position)  # from centrifugal force = gravitational force

    satellite_1 = Particle(
        position=np.array([sat_1_position, 0, 0]),
        velocity=np.array([0, sat_1_velocity, 0]),
        acceleration=np.array([0, 0, 0]),
        name="Satellite 1",
        mass=100.
    )
    satellite_2 = Particle(
        position=np.array([sat_2_position, 0, 0]),
        velocity=np.array([0, sat_2_velocity, 0]),
        acceleration=np.array([0, 0, 0]),
        name="Satellite 2",
        mass=100.
    )

    return [earth, satellite_1, satellite_2]


def three_body_simulation(delta_t, iterations, objects, file, t=0):
    """
    Simulation loop for a 3 body system.

    :param delta_t: smallest unit of time in the simulation
    :param iterations: how many times should the particles update
    :param objects: list of Particle objects
    :param file: name of file in which data from this simulation will be stored
    :param t: starting time, equal to zero by default
    """
    data = []

    for i in range(1, iterations + 1):

        t += delta_t
        for j in objects:
            j.setAcceleration(j.NBodyAcceleration(objects))
            j.updateEuler(delta_t)
        # print(objects[1].acceleration)
        if (i - 1) % 100 == 0:
            data.append([t] + [copy.deepcopy(k) for k in objects])
    np.save(new_path + file, data, allow_pickle=True)


object_list = satellite_system_objects()
three_body_simulation(1, 3600 * 24 * 4, object_list, "/three_body_test")
