import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.SimpleGraphPlot import SimpleGraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def retrieve_data(file, s):
    """
    :param file: .npy file to extract data from
    :param s: which type of data to extract. 0 is time and 1-n is a Particle instance
    :return: the times and positions extracted
    """
    data = np.load(file, allow_pickle=True)
    times = []
    positions = []
    for i in data:
        times.append(i[0])
        positions.append(i[s].position)
    return times, positions


sat_1_times, sat_1_pos = retrieve_data(new_path + "/two_body_test.npy", 2)
sat_2_times, sat_2_pos = retrieve_data(new_path + "/cromer_test.npy", 2)

euler_x_y = SimpleGraphPlot(sat_1_times, sat_1_pos)  # Plot for the Euler method
euler_cromer_x_y = SimpleGraphPlot(sat_2_times, sat_2_pos)  # Plot for the Euler-Cromer method

euler_x_y.draw2DPositionGraph(color="r", label="Euler")
euler_cromer_x_y.draw2DPositionGraph(color="b", label="Euler-Cromer")

plt.legend()
plt.show()