import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlot import GraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def three_d_plot_paths(data, labels):
    ax = plt.axes(projection="3d")
    pos = []

    for i in data:
        temp_pos = []
        for j in range(1, len(i)):  # starts at 1 to ignore time
            temp_pos.append(i[j].position)
        pos.append(temp_pos)

    for p in range(len(pos[0])):  # iterates through each particle
        subset = []
        for i in pos:  # looking at ith time saved
            subset.append(i[p])
        graph = GraphPlot(subset)
        graph.draw3DPositionGraph(ax, label=labels[p])
    ax.set_xlabel("x-axis (m)")
    ax.set_ylabel("y-axis (m)")
    ax.set_zlabel("z-axis (m)")
    ax.set_title("Solar System Simulation 1")
    plt.legend()
    plt.show()


def two_d_plot_paths(data, labels):
    pos = []

    for i in data:
        temp_pos = []
        for j in range(1, len(i)):  # starts at 1 to ignore time
            temp_pos.append(i[j].position)
        pos.append(temp_pos)

    for p in range(len(pos[0])):  # iterates through each particle
        subset = []
        for i in pos:  # looking at ith time saved
            subset.append(i[p])
        graph = GraphPlot(subset)
        graph.draw2DPositionGraph(label=labels[p])
    plt.xlabel("x-axis (m)")
    plt.ylabel("y-axis (m)")
    plt.title("2D view of solar system simulation")
    plt.legend()
    plt.show()


def plot_total_kinetic_energy(data):
    """
    Draws the total kinetic energy of the system against time
    """

    raw_e_k = []
    times = []

    for i in data:
        temp = 0
        for j in range(1, len(i)):  # starts at 1 to ignore time
            temp += i[j].getKineticEnergy()
            print(i[j].getKineticEnergy())
        raw_e_k.append(temp)
        times.append(i[0])

    plt.plot(times, raw_e_k)
    plt.xlabel("Time (s)")
    plt.ylabel("Total kinetic energy (J)")
    plt.title("Kinetic energy evolution")
    # plt.legend()
    plt.show()


def plot_kinetic_energy_diff(time_data, raw_e_k_data):
    """
    Draws the total kinetic energy of the system against time
    :param time_data: list of int; list of times
    :param raw_e_k_data: 2D list of kinetic energies of all objects at all times
    """
    tot_e_k_list = []
    e_k_0 = 0
    for i, sublist in enumerate(raw_e_k_data):
        tot_e_k = 0
        for e_k_i in sublist:
            tot_e_k += e_k_i
        if i == 0:
            e_k_0 = tot_e_k  # total system energy at t=0
        tot_e_k_list.append(tot_e_k)
    print(e_k_0)
    plt.plot(time_data, (np.array(tot_e_k_list) - e_k_0) / e_k_0)

    plt.xlabel("Time (s)")
    plt.ylabel("Normalised total kinetic energy (J)")
    plt.title("Kinetic energy fluctuations")


my_data = np.load(new_path + "/solar_test_data_1.npy", allow_pickle=True)
my_data_2 = np.load(new_path + "/solar_energy_test_1.npy", allow_pickle=True)

# names = GraphPlot.retrieveData(my_data)

# two_d_plot_paths(my_data, names)
# three_d_plot_paths(my_data, names)
# plt.figure()
# plt.subplot(211)
plot_total_kinetic_energy(my_data_2)
# plt.subplot(212)
# plot_kinetic_energy_diff(times, energy_data)
# plt.tight_layout()
# plt.show()

# three_d_plot_paths(pos_data, names)

# two_d_plot_paths(pos_data, names)
