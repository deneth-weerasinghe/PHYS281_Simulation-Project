import numpy as np
import matplotlib.pyplot as plt


class NBodyGraphPlotting:

    def __init__(self, data):
        self.data = data
        self.labels = self.getLabels()
        self.times = [i[0] for i in data]

    def getLabels(self):
        labels = []
        for i in self.data:
            for j in range(1, len(i)):  # starts at 1 to ignore time
                if len(labels) < len(i) - 1:  # generates separate list for the names of the objects
                    labels.append(i[j].name)
        return labels

    def twoDimPositionPlot(self, title="2D Plot"):
        """
        Draws the path of all objects in the x-y plane
        """

        for i in range(1, len(self.data[0])):  # iterates through each object; starts at 1 because index 0 is time
            x_list = []
            y_list = []
            for j in self.data:
                x_list.append(j[i].position[0])
                y_list.append(j[i].position[1])
            plt.plot(x_list, y_list, label=self.labels[i - 1])

        plt.xlabel("x-axis (m)")
        plt.ylabel("y-axis (m)")
        plt.title(title)
        plt.legend(loc=5)

    def threeDimPositionPlot(self, title="3D Plot"):
        """
        Draws the path of all objects in x-y-z space
        """
        ax = plt.axes(projection="3d")  # required to make 3D plots

        for i in range(1, len(self.data[0])):  # iterates through each object; starts at 1 because index 0 is time
            x_list = []
            y_list = []
            z_list = []
            for j in self.data:
                x_list.append(j[i].position[0])
                y_list.append(j[i].position[1])
                z_list.append(j[i].position[2])
            plt.plot(x_list, y_list, z_list, label=self.labels[i - 1])

        ax.set_xlabel("x-axis (m)")
        ax.set_ylabel("y-axis (m)")
        ax.set_zlabel("z-axis (m)")
        ax.set_title(title)
        plt.legend()
        plt.show()

    def totalKineticEnergyPlot(self):
        """
        Draws the total kinetic energy of the system against time
        """

        e_k_list = []

        for i in self.data:
            temp = 0
            for j in range(1, len(i)):  # starts at 1 to ignore time
                temp += i[j].getKineticEnergy()
            e_k_list.append(temp)

        plt.plot(self.times, np.array(e_k_list, dtype=float))
        plt.xlabel("Time (s)")
        plt.ylabel("Total kinetic energy (J)")
        plt.title("Kinetic energy evolution")

    def diffKineticEnergyPlot(self):
        """
        Draws the change in kinetic energy of the system against time
        """

        e_k_list = []

        for i in self.data:
            temp = 0
            for j in range(1, len(i)):  # starts at 1 to ignore time
                temp += i[j].getKineticEnergy()
            e_k_list.append(temp)

        e_k_init = e_k_list[0]

        plt.plot(self.times, abs(np.array(e_k_list, dtype=float) - e_k_init)/e_k_init)
        plt.xlabel("Time (s)")
        plt.ylabel("Change in kinetic energy from $t_0$ (J)")
        plt.title("Change in kinetic energy")
