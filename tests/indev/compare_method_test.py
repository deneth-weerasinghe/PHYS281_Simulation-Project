import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlotting import GraphPlotting

new_path = os.path.dirname(os.path.dirname(os.getcwd()))
fig = plt.figure()


def retrieve_data(file):
    """
    Reads data from the selected data file, obtaining data useful for plotting
    :param file: string; filename
    :return: 3D list containing the 3-vector positions of each object as floats at each time and a list containing the
    string names of each object
    """
    raw_data = np.load(new_path + file, allow_pickle=True)
    processed_data = []
    labels = []
    for i in raw_data:
        temp = []
        for j in range(0, len(i)):
            if len(labels) < len(i):  # generates separate lists for the names and colours of the objects
                labels.append(i[j].name)
            temp.append(i[j].position)
        processed_data.append(temp)
    return processed_data, labels


def plot_paths(data, labels):
    """
    Plots and displays the data as a series of overlaid 2D graphs of y-position against x-position
    :param data: 3D list of floats; the input data
    :param labels: list of labels for each object to use in the plot's legend
    """
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
            subset.append(i[p])
        graph = GraphPlotting(subset)
        graph.draw2DPositionGraph(label=labels[p])  # plots the path of a particle
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.legend()
    plt.show()


dataset, names = retrieve_data("/data_files/method_test_data.npy")
plot_paths(dataset, names)
fig.savefig(new_path + "/plots/different_methods.png")
