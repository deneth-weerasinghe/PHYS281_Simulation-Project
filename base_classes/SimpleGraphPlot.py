import matplotlib.pyplot as plt
import numpy as np


class SimpleGraphPlot:

    def __init__(self, times, positions):
        extracted_x = SimpleGraphPlot.getOneBodyVectorElements(positions, 0)
        extracted_y = SimpleGraphPlot.getOneBodyVectorElements(positions, 1)
        extracted_z = SimpleGraphPlot.getOneBodyVectorElements(positions, 2)

        self.times = np.array(times, dtype=float)
        self.x = extracted_x
        self.y = extracted_y
        self.z = extracted_z

    def drawTimeXGraph(self):
        """
        Draws the particle's x-position as a function of time
        """
        plt.plot(self.times, self.x, "-r", label='x-component')
        plt.xlabel('time (s)')
        plt.ylabel('position')
        plt.legend()

    def draw2DPositionGraph(self, color="r", label="trajectory in x-y plane"):
        """
        Draws the particle's y-positions against its x-positions i.e. the x-y plane
        """
        plt.plot(self.x, self.y, color=color, label=label)
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")

    @staticmethod
    def getOneBodyVectorElements(array, j):
        """
        Extracts all the jth component from all vectors in an array
        e.g. j = 0 extracts the first component from all vectors in the array (i.e. x-components)
        :param array: source array
        :param j: which component should be extracted from all the vectors
        :return: new array containing all the extracted jth-components
        """
        new_array = []

        for i in array:
            new_array.append(i[j])

        return new_array
