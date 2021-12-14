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
        plt.legend()

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

    def totalKineticEnergyPlot(self):
        """
        Draws the total kinetic energy of the system against time
        """

        raw_e_k = []

        for i in self.data:
            temp = 0
            for j in range(1, len(i)):  # starts at 1 to ignore time
                temp += i[j].getKineticEnergy()
            raw_e_k.append(temp)

        plt.plot(self.times, raw_e_k)
        plt.xlabel("Time (s)")
        plt.ylabel("Total kinetic energy (J)")
        plt.title("Kinetic energy evolution")
        plt.show()

    # def plot_kinetic_energy_diff(self):
    #     """
    #     Draws the total kinetic energy of the system against time
    #     :param time_data: list of int; list of times
    #     :param raw_e_k_data: 2D list of kinetic energies of all objects at all times
    #     """
    #     tot_e_k_list = []
    #     e_k_0 = 0
    #     for i, sublist in enumerate(raw_e_k_data):
    #         tot_e_k = 0
    #         for e_k_i in sublist:
    #             tot_e_k += e_k_i
    #         if i == 0:
    #             e_k_0 = tot_e_k  # total system energy at t=0
    #         tot_e_k_list.append(tot_e_k)
    #     print(e_k_0)
    #     plt.plot(time_data, (np.array(tot_e_k_list) - e_k_0) / e_k_0)
    #
    #     plt.xlabel("Time (s)")
    #     plt.ylabel("Normalised total kinetic energy (J)")
    #     plt.title("Kinetic energy fluctuations")
