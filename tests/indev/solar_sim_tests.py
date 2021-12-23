import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.NBodyGraphPlotting import NBodyGraphPlotting

new_path = os.path.dirname(os.path.dirname(os.getcwd()))


def position_tests(graph_object, years_str):
    fig = plt.figure(figsize=[5, 5])
    param = {"font.size": 15}
    plt.rcParams.update(param)

    graph_object.threeDimPositionPlot("System Evolution over {} years, 3D".format(years_str))


def energy_tests(graph_object, filename):
    # fig = plt.figure(constrained_layout=True)
    # param = {"font.size": 15}
    # plt.rcParams.update(param)
    # plt.subplot(211)
    # graph_object.percentageLinearMomentum()
    # plt.subplot(212)
    graph_object.kineticAndPotentialEnergyPlot()
    # plt.legend()
    # plt.show()
    # fig.savefig(new_path + "/plots" + filename.replace("npy", "png"))


# final plotting:
filenames = ["/248y_euler.npy",
             "/248y_euler_high.npy",
             "/248y_euler_cromer.npy",
             "/248y_euler_cromer_high.npy",
             "/248y_euler_richardson.npy",
             "/248y_euler_richardson_high.npy",
             "/248y_verlet.npy",
             "/248y_verlet_high.npy"]

raw_datasets = [np.load(new_path + "/data_files" + i, allow_pickle=True) for i in filenames]  # list of raw datasets
graph_objects = [NBodyGraphPlotting(i) for i in raw_datasets]

for i, n in enumerate(filenames):
    energy_tests(graph_objects[i], n)
