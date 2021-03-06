import numpy as np
import os

parent_dir = os.path.dirname(os.getcwd())
file_path = os.path.join(parent_dir, "data_files/TwoBodyTest.npy")


def print_particle(particle):
    print("Particle: {}".format(particle.name))
    print("  Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("  {}: {}".format(attribute,
                                particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!


print("Testing reading the file TwoBodyTest.npy that you have loaded")

float_formatter = lambda x: "%.5e" % x
np.set_printoptions(formatter={'float_kind': float_formatter})
DataIn = np.load(file_path, allow_pickle=True)
print("Printing First Entry")
print("{}".format(int(DataIn[0][0])))  # time
print_particle(DataIn[0][1])  # Earth
print_particle(DataIn[0][2])  # Satellite

print("Printing Fifth Entry")
print("{}".format(int(DataIn[4][0])))  # time
print_particle(DataIn[4][1])  # Earth
print_particle(DataIn[4][2])  # Satellite

print("Printing Last Entry")
print("{}".format(int(DataIn[-1][0])))  # time
print_particle(DataIn[-1][1])  # Earth
print_particle(DataIn[-1][2])  # Satellite
