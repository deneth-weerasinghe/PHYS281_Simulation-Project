import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlot import GraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


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
    # print(raw_data[0][3])
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
    :param labels:
    """
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
            subset.append(i[p])
        graph = GraphPlot(subset)
        graph.draw2DPositionGraph(label=labels[p])  # plots the path of a particle
    plt.xlabel("x (m)")
    plt.ylabel("y (m)")
    plt.legend()
    plt.show()


dataset, names = retrieve_data("/method_test_data.npy")
plot_paths(dataset, names)


