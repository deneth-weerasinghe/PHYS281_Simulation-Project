import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlotting import GraphPlotting

new_path = os.path.dirname(os.path.dirname(os.getcwd()))
fig = plt.figure(figsize=[4, 4])


def retrieve_data(file):
    raw_data = np.load(new_path + file, allow_pickle=True)
    processed_data = []
    names = []
    for i in raw_data:
        temp = []
        for j in range(1, len(i)):
            if len(names) < len(i) - 1:  # generates separate lists for the names of the objects
                names.append(i[j].name)
            temp.append(i[j].position)
        processed_data.append(temp)
    return processed_data, names


def plot_paths(data, labels):
    param = {"font.size": 15}
    plt.rcParams.update(param)
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
            subset.append(i[p])
        graph = GraphPlotting(subset)
        graph.draw2DPositionGraph(label=labels[p])  # plots the path of a particle
    plt.xlabel("x-position (m)")
    plt.ylabel("y-position (m)")
    plt.title("Five body system")
    plt.legend()
    plt.show()


dataset, names = retrieve_data("/data_files/three_body_test.npy")  # incorrectly named, should be "five" not "three"
plot_paths(dataset, names)

fig.savefig(new_path + "/plots/five_bodies.png")
