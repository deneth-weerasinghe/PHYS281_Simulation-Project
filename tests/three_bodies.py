import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.SimpleGraphPlot import SimpleGraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def retrieve_data():
    raw_data = np.load(new_path + "/three_body_test.npy", allow_pickle=True)
    processed_data = []
    for i in raw_data:
        processed_data.append([i[1].position, i[2].position, i[3].position])
    return processed_data

# def plot_paths(data):
#