import matplotlib.pyplot as plt
import numpy as np


class GraphPlotting:
    """
    Class for creating graphs of the path of a single body

    __________
    Constructor
    :param positions: list of floats; list of positions at every saved time
    :param: times: list of integers; list of times
    """

    def __init__(self, positions, times=None):
        if times is None:
            times = []
        extracted_x = GraphPlotting.getOneBodyVectorElements(positions, 0)
        extracted_y = GraphPlotting.getOneBodyVectorElements(positions, 1)
        extracted_z = GraphPlotting.getOneBodyVectorElements(positions, 2)

        self.times = np.array(times, dtype=float)
        self.x = np.array(extracted_x, dtype=float)
        self.y = np.array(extracted_y, dtype=float)
        self.z = np.array(extracted_z, dtype=float)

    def drawTimeXGraph(self):
        """
        Draws the particle's x-position as a function of time
        """
        plt.plot(self.times, self.x, "-r", label='X-component')
        plt.xlabel('time (s)')
        plt.ylabel('position')

    def draw2DPositionGraph(self, label="Trajectory in x-y plane", color=None):
        """
        Draws the particle's y-positions against its x-positions i.e. the x-y plane
        :param: label: string label to input into the plot function
        """
        plt.plot(self.x, self.y, label=label, color=color)

    def draw3DPositionGraph(self, axes, label="Trajectory in 3D space"):
        """
        Draws the particle's path in 3D space
        :param axes: plt.axes object
        :param label: string label to input into the plot function
        :return: plt.axes object for use to label the axis, which is done just after this method is called
        """
        axes.plot(self.x, self.y, self.z, label=label)

    @staticmethod
    def getOneBodyVectorElements(array, j):
        """
        Extracts all the jth component from all vectors in an array
        e.g. j = 0 extracts the first component from all vectors in the array (i.e. x-components)
        :param array: source array
        :param j: integer, which component should be extracted from all the vectors
        :return: new array containing all the extracted jth-components
        """
        new_array = []

        for i in array:
            new_array.append(i[j])

        return new_array

    @staticmethod
    def retrieveData(data):
        """
        Retrieves data from a specified file in a specified subdirectory
        :param data: raw data read from the storage file; list of Particle objects and times
        :return: list of position vectors (list of floats) of each object, names of the objects (list of strings)
        """
        # raw_data = np.load(path + file, allow_pickle=True)
        pos = []
        e_k = []
        u = []
        lin_p = []
        ang_p = []
        labels = []
        times = []
        for i in data:
            temp_pos = []
            temp_e_k = []
            for j in range(1, len(i)):  # starts at 1 to ignore time
                if len(labels) < len(i) - 1:  # generates separate list for the names of the objects
                    labels.append(i[j].name)
                temp_pos.append(i[j].position)
                temp_e_k.append(i[j].getKineticEnergy())
            pos.append(temp_pos)
            e_k.append(temp_e_k)
            times.append(i[0])
        return labels
