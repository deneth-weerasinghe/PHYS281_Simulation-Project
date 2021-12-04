import os
import numpy as np
import matplotlib.pyplot as plt
from base_classes.SimpleGraphPlot import SimpleGraphPlot

new_path = os.path.join(os.path.dirname(os.getcwd()), "data_files")


def retrieve_data():
    raw_data = np.load(new_path + "/three_body_test.npy", allow_pickle=True)
    processed_data = []
    for i in range(100):
        processed_data.append([raw_data[i][1].position, raw_data[i][2].position, raw_data[i][3].position])
    return processed_data
