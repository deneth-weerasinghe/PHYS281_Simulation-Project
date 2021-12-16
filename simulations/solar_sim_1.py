import os
import copy
import numpy as np
from poliastro import constants
from base_classes.EphemeridesObjects import EphemeridesObjects

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")  # place the data file in a different subdirectory


def generate_data(delta_t, iterations, objects, file, method=0, t=0):
    """
    Simulation loop for a 3 body system.

    :param method: which Particle method to use for updating the position of the object
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
            if method == 0:
                j.updateEuler(delta_t)
            elif method == 1:
                j.updateEulerCromer(delta_t)
            elif method == 2:
                j.updateEulerRichardson(delta_t, objects)
            elif method == 3:
                j.updateVerlet(delta_t, objects)
        data.append([t] + [copy.deepcopy(k) for k in objects])
    np.save(new_path + file, data, allow_pickle=True)


# dictionary {label: mass * G} of objects to be simulated
celestial_objects = {"Sun": constants.GM_sun,
                     "Mercury": constants.GM_mercury,
                     "Venus": constants.GM_venus,
                     "Earth": constants.GM_earth,
                     "Mars": constants.GM_mars,
                     "Jupiter": constants.GM_jupiter,
                     "Saturn": constants.GM_saturn,
                     "Uranus": constants.GM_uranus,
                     "Neptune": constants.GM_neptune,
                     "Pluto": constants.GM_pluto}

t_0 = "2021-12-04 00:00:00.0"  # initial time from which to obtain the initial conditions
solar_system = EphemeridesObjects(t_0, celestial_objects)
solar_objects = solar_system.obtainObjects()

# seconds in a day of a Julian year i.e. 60 * 60 * 24 seconds = 86400 seconds hence the time step
time_step = 86400

"""
To simplify, I do not use a Julian year (364.25 days), instead using 365 days because the number of days is used as
the number of iterations, which needs to be an integer
"""


"""
method key argument specifies which method to use to update the position of the object
method: [0, 1, 2, 3] for Euler, Euler-Cromer, Euler-Richardson, Verlet, method = 0 by default
"""
# simulate for 365 days, Earth should complete one full orbit
# generate_data(time_step, 365 * 4, solar_objects, "/4y_euler")
# simulate for 10 years (close to Jupiter's orbital period
# generate_data(time_step, 365 * 10, solar_objects, "/10y_verlet", method=3)
# simulate for Pluto's orbital period
generate_data(time_step * 5, 365 * int(248 / 5), solar_objects, "/284y_verlet", method=3)
# generate_data(time_step * 5, 365 * int(284 / 5), solar_objects, "/284y_euler")
