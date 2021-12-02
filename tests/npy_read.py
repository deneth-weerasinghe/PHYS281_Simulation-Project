import numpy as np
import os

file_path = os.getcwd()
file_path = file_path.replace("tests", "data_files/TwoBodyTest.npy")

data = np.load(file_path, allow_pickle=True)
print(data[5][1].getPosition())
