import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.SimpleGraphPlot import SimpleGraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def retrieve_data():
    raw_data = np.load(new_path + "/three_body_test.npy", allow_pickle=True)
    processed_data = []
    names = []
    for i in raw_data:
        processed_data.append([i[1].position, i[2].position, i[3].position])
    for j in range(1, len(raw_data[0])):
        names.append(raw_data[0][j].name)
    return processed_data, names


def plot_paths(data, names, colours):
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
            subset.append(i[p])
        graph = SimpleGraphPlot(subset)
        graph.draw2DPositionGraph(color=colours[p], label=names[p])  # plots the path of a particle
    plt.legend()
    plt.show()


dataset, names = retrieve_data()
colours = ["g", "r", "orange"]
plot_paths(dataset, names, colours)
