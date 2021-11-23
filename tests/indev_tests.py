import numpy as np
import os

file_path = os.getcwd()
file_path = file_path.replace("tests", "data_files/TwoBodyTest.npy")

DataIn = np.load(file_path, allow_pickle=True)


print("Testing reading the file TwoBodyTest.npy  that you have loaded")

print("Printing Kinetic Energy of First Entry Earth and Satellite")
print("Earth KE: {:.5e}".format(DataIn[0][1].kineticEnergy()))
print("Satellite KE: {:.5e}".format(DataIn[0][2].kineticEnergy()))

print("Printing Kinetic Energy of Last Entry")
print("Earth KE: {:.5e}".format(DataIn[-1][1].kineticEnergy()))
print("Satellite KE: {:.5e}".format(DataIn[-1][2].kineticEnergy()))