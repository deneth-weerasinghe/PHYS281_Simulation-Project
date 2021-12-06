import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.GraphPlot import GraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def plot_paths(data, labels):
    for p in range(len(data[0])):  # iterates through each particle
        subset = []
        for i in data:  # looking at ith time saved
            subset.append(i[p])
        graph = GraphPlot(subset)
        graph.draw2DPositionGraph(label=labels[p])
    plt.legend()
    plt.show()


dataset, names = GraphPlot.retrieveData(new_path, "/solar_test_data_1.npy")

plot_paths(dataset, names)
# for i in dataset:
#     print(i[3].acceleration)
