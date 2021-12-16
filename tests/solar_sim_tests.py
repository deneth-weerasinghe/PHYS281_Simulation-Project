import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.NBodyGraphPlotting import NBodyGraphPlotting


new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def energy_tests(graph_object, years_str):

    # graph_object.threeDimPositionPlot("System Evolution, 3D")

    plt.figure(constrained_layout=True)
    plt.subplot(311)
    graph_object.twoDimPositionPlot("System evolution over " + years_str + " years, 2D")
    plt.subplot(312)
    graph_object.totalKineticEnergyPlot()
    plt.subplot(313)
    graph_object.kineticAndPotentialEnergyPlot()
    plt.legend()
    plt.show()


euler_data = np.load(new_path + "/284y_euler.npy", allow_pickle=True)
verlet_data = np.load(new_path + "/284y_verlet.npy", allow_pickle=True)

years = "10"
# test_set_euler_284y = NBodyGraphPlotting(euler_data)
test_set_verlet = NBodyGraphPlotting(verlet_data)

# print(test_set_verlet.labels)
# energy_tests(test_set_verlet, years)
