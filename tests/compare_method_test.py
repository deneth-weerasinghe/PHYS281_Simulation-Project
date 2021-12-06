import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlot import GraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def retrieve_data(file):
    raw_data = np.load(new_path + file, allow_pickle=True)
    processed_data = []
    names = []
    for i in raw_data:
        temp = []
        for j in range(0, len(i)):
            if len(names) < len(i):  # generates separate lists for the names and colours of the objects
                names.append(i[j].name)
            temp.append(i[j].position)
        processed_data.append(temp)
    return processed_data, names


def plot_paths(data, labels):
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
print(dataset[1])
# plot_paths(dataset, names)

