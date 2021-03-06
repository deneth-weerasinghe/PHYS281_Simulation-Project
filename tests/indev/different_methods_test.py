import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlotting import GraphPlotting

new_path = os.path.dirname(os.path.dirname(os.getcwd()))
fig = plt.figure()


def retrieve_data(file, s):
    """
    :param file: .npy file to extract data from
    :param s: which type of data to extract. 0 is time and 1-n is a Particle object
    :return: the times and positions extracted
    """
    data = np.load(file, allow_pickle=True)
    times = []
    positions = []
    for i in data:
        times.append(i[0])
        positions.append(i[s].position)
    return times, positions


sat_1_times, sat_1_pos = retrieve_data(new_path + "/data_files/two_body_test.npy",
                                       2)  # 2 for the second object i.e. the satellite
sat_2_times, sat_2_pos = retrieve_data(new_path + "/data_files/cromer_test.npy", 2)

euler_x_y = GraphPlotting(sat_1_pos, sat_1_times)  # Plot for the Euler method
euler_cromer_x_y = GraphPlotting(sat_2_pos, sat_2_times)  # Plot for the Euler-Cromer method

param = {"font.size": 20}
plt.rcParams.update(param)
euler_x_y.draw2DPositionGraph(label="Euler")
euler_cromer_x_y.draw2DPositionGraph(label="Euler-Cromer")

plt.legend()
plt.show()
fig.savefig(new_path + "/plots/different_methods.png")
