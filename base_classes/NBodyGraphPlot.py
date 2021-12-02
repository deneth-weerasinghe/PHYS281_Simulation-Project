import matplotlib.pyplot as plt
import numpy as np


class NBodyGraphPlot():
    """
    Class for creating graphs containing the paths traced by multiple bodies
    """
    def __init__(self, data):
        self.data = np.copy(data).astype(float)
        self.times = NBodyGraphPlot.setTimes(self.data)
        self.positions = []

    @staticmethod
    def setTimes(data):
        new_times = []
        for i in data:
            new_times.append(i[0])
        return new_times
