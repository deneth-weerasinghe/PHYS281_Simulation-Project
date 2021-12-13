import os
import copy
import numpy as np
from poliastro import constants
from base_classes.EphemeridesObjects import EphemeridesObjects

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")  # place the data file in a different subdirectory


def generate_data(delta_t, iterations, objects, file, t=0):
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
        print(str((i/(iterations + 1) * 100).__round__(1)) + "%")

        t += delta_t
        for j in objects:
            j.setAcceleration(j.NBodyAcceleration(objects))
            j.updateEuler(delta_t)
        # if (i - 1) % 100 == 0:
        data.append([t] + [copy.deepcopy(k) for k in objects])
    np.save(new_path + file, data, allow_pickle=True)


# list of objects to be simulated
labels = ["Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
raw_masses = [constants.GM_sun,
              constants.GM_mercury,
              constants.GM_venus,
              constants.GM_earth,
              constants.GM_moon,
              constants.GM_mars,
              constants.GM_jupiter,
              constants.GM_saturn,
              constants.GM_uranus,
              constants.GM_neptune,
              constants.GM_pluto,
              ]

t_0 = "2021-12-04 00:00:00.0"  # initial time from which to obtain the initial conditions

solar_system = EphemeridesObjects(t_0, labels, raw_masses)
solar_objects = solar_system.obtainObjects()

# seconds in a day in 1 Julian year = 60 * 60 * 24 seconds = 86400 seconds hence timestep
time_step = 86400

# to simplify, I do not use a Julian year (364.25 days), instead using 365 days because the number of days is used as
# the number of iterations, which needs to be an integer

# simulate for 365 days, Earth should complete one full orbit
# generate_data(time_step, 365 * 4 , solar_objects, "/solar_test_data_1")
# simulate for 10 years (close to Jupiter's orbital period
generate_data(time_step, 365 * 10, solar_objects, "/solar_test_data_1_10y")
# simulate for Pluto's orbital period
# generate_data(time_step * 31, 365 * int(248 / 31), solar_objects, "/solar_energy_test_1")
