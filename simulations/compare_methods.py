import os
import copy
import numpy as np
from base_classes.Particle import Particle
import astropy.constants

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")

methods = ["Euler", "Euler_Cromer", "Euler_Richardson", "Verler"]


def generate_satellites():
    """
    Creates a simple preset of a n-body gravitational system, consisting of Earth and n satellites
    :return: list of Particle objects
    """
    earth_mass = 5.97237e24  # https://en.wikipedia.org/wiki/Earth
    earth_radius = 63710 * 1e3  # https://en.wikipedia.org/wiki/Earth

    sat_position = earth_radius + (35786 * 1e3)
    sat_velocity = np.sqrt(astropy.constants.G.value * earth_mass / sat_position)

    satellites = []
    for label in methods:
        satellites.append(
            Particle(
                position=np.array([sat_position, 0, 0]),
                velocity=np.array([0, sat_velocity, 0]),
                acceleration=np.array([0, 0, 0]),
                name=label,
                mass=100.
            )
        )
    return satellites


def sim_loop(delta_t, iterations, method, sat, t=0):
    earth = Particle(
        position=np.array([0, 0, 0]),
        velocity=np.array([0, 0, 0]),
        acceleration=np.array([0, 0, 0]),
        name="Earth",
        mass=5.97237e24
    )
    data = []  # list to store contents that will be written to "TwoBodyTest.npy"

    for k in range(1, iterations + 1):

        t += delta_t

        sat.setAcceleration(sat.NBodyAcceleration([earth]))
        if method == 0:
            sat.updateEuler(delta_t)
        elif method == 1:
            sat.updateEulerCromer(delta_t)
        elif method == 2:
            sat.updateEulerRichardson(delta_t, [earth])
        elif method == 3:
            sat.updateVerler(delta_t, [earth])

        if (k - 1) % 100 == 0:  # which values of i should be considered when storing data
            data.append(copy.deepcopy(sat))
    return data


object_list = generate_satellites()

data_1 = sim_loop(1, 3600 * 24 * 4, 0, object_list[0])
data_2 = sim_loop(1, 3600 * 24 * 4, 1, object_list[1])
data_3 = sim_loop(1, 3600 * 24 * 4, 2, object_list[2])
data_4 = sim_loop(1, 3600 * 24 * 4, 3, object_list[3])

final_data = []

for i in range(0, len(data_1)):
    final_data.append([
        data_1[i],
        data_2[i],
        data_3[i],
        data_4[i]
    ])

np.save(new_path + "/method_test_data", final_data, allow_pickle=True)
