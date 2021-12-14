import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.NBodyGraphPlotting import NBodyGraphPlotting


new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def euler_test(data):

    euler_sim = NBodyGraphPlotting(data)
    euler_sim.threeDimPositionPlot("System Evolution, 3D")

    plt.figure(constrained_layout=True)
    plt.subplot(311)
    euler_sim.twoDimPositionPlot("System Evolution, 2D")
    plt.subplot(312)
    euler_sim.totalKineticEnergyPlot()
    plt.subplot(313)
    euler_sim.diffKineticEnergyPlot()

    # plt.tight_layout()
    plt.show()


my_data = np.load(new_path + "/solar_test_data_1.npy", allow_pickle=True)
euler_data = np.load(new_path + "/solar_energy_test_1.npy", allow_pickle=True)

euler_test(euler_data)

# three_d_plot_paths(my_data, names)
# plt.figure()
# plt.subplot(211)
# plot_total_kinetic_energy(my_data_2)
#
# plt.subplot(212)
# plot_kinetic_energy_diff(times, energy_data)
# plt.tight_layout()
# plt.show()

# three_d_plot_paths(pos_data, names)

# two_d_plot_paths(pos_data, names)
