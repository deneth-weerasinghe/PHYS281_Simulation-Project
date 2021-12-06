import matplotlib.pyplot as plt
import numpy as np


class GraphPlot:
    """
    Class for creating graphs of the path of a single body
    """

    def __init__(self, positions, times=None):
        if times is None:
            times = []
        extracted_x = GraphPlot.getOneBodyVectorElements(positions, 0)
        extracted_y = GraphPlot.getOneBodyVectorElements(positions, 1)
        extracted_z = GraphPlot.getOneBodyVectorElements(positions, 2)

        self.times = np.array(times, dtype=float)
        self.x = extracted_x
        self.y = extracted_y
        self.z = extracted_z

    def drawTimeXGraph(self):
        """
        Draws the particle's x-position as a function of time
        """
        plt.plot(self.times, self.x, "-r", label='X-component')
        plt.xlabel('time (s)')
        plt.ylabel('position')

    def draw2DPositionGraph(self, label="Trajectory in x-y plane"):
        """
        Draws the particle's y-positions against its x-positions i.e. the x-y plane
        """
        plt.plot(self.x, self.y, label=label)

    def draw3DPositionGraph(self, label="Trajectory in 3D space"):
        """
        Draws the particle's path in 3D cartesian space"
        """
        ax = plt.axes(projection="3d")
        ax.plot(self.x, self.y, self.z, label=label)

        return ax

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

    @staticmethod
    def retrieveData(path, file):
        """
        Retrieves data from a specified file in a specified subdirectory
        :param path: the directory the data file is located in, in string
        :param file: the filename of the data file, in string
        :return: list of position vectors of each object, names of the objects
        """
        raw_data = np.load(path + file, allow_pickle=True)
        processed_data = []
        names = []
        for i in raw_data:
            print(i[4].acceleration)
            temp = []
            for j in range(1, len(i)):
                if len(names) < len(i) - 1:  # generates separate list for the names of the objects
                    names.append(i[j].name)
                temp.append(i[j].position)
            processed_data.append(temp)
        return processed_data, names
