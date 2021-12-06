import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlot import GraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def three_d_plot_paths(data, labels):
    ax = plt.axes(projection="3d")
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
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
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
            subset.append(i[p])
        graph = GraphPlot(subset)
        graph.draw2DPositionGraph(label=labels[p])
    plt.xlabel("x-axis (m)")
    plt.ylabel("y-axis (m)")
    plt.title("2D view of solar system simulation")
    plt.legend()
    plt.show()


dataset, names = GraphPlot.retrieveData(new_path, "/solar_test_data_1.npy")

three_d_plot_paths(dataset, names)
two_d_plot_paths(dataset, names)
