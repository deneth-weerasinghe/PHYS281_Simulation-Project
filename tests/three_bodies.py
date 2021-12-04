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
        temp = []
        for j in range(1, len(i)):
            if len(names) < len(i) - 1:  # creates a separate list for the names of the objects
                names.append(i[j].name)
            temp.append(i[j].position)
        processed_data.append(temp)
    return processed_data, names


def plot_paths(data, labels, colours):
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
            subset.append(i[p])
        graph = SimpleGraphPlot(subset)
        graph.draw2DPositionGraph(color=colours[p], label=labels[p])  # plots the path of a particle
    plt.legend()
    plt.show()


dataset, names = retrieve_data()
my_colours = ["g", "r", "orange"]
print(names)
plot_paths(dataset, names, my_colours)
