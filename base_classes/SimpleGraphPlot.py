import matplotlib.pyplot as plt
import numpy as np


class SimpleGraphPlot:

    def __init__(self, times, positions):
        extracted_x = SimpleGraphPlot.getVectorElements(positions, 0)
        extracted_y = SimpleGraphPlot.getVectorElements(positions, 1)
        extracted_z = SimpleGraphPlot.getVectorElements(positions, 2)

        self.times = np.array(times, dtype=float)
        self.x = extracted_x
        self.y = extracted_y
        self.z = extracted_z

    def drawTimeXGraph(self):
        plt.plot(self.times, self.x, "-r", label='trajectory')
        plt.xlabel('time (s)')
        plt.ylabel('position')
        plt.legend()
        plt.show()

    def draw2DPositionGraph(self):
        scatter_colour = None
        division = int(len(self.x) / 4)

        # for i in range(0, len(self.x)):
        #     if 0 <= i < (division * 1):
        #         scatter_colour = "r"
        #     elif (division * 1) <= i < (division * 2):
        #         scatter_colour = "o"
        #     elif (division * 2) <= i < (division * 3):
        #         scatter_colour = "y"

        plt.scatter(self.x, self.y, marker="o", color="r")
        plt.xlabel("x (m)")
        plt.ylabel("y (m)")
        plt.show()

    @staticmethod
    def getVectorElements(array, j):
        """
        Extracts all the jth elements from an array of vectors
        e.g. j = 0 extracts the first element from all vectors in the array
        :param array: source array
        :param j: which element should be extracted from all the vectors
        :return: new array containing all the extracted elements
        """
        new_array = []

        for i in array:
            new_array.append(i[j])

        return new_array
