import numpy as np
import matplotlib.pyplot as plt


class NBodyGraphPlotting:
    """
    Class used to generate every plot for each complete system dataset, rather than for individual solar objects
    unlike GraphPlotting.py.

    -------------------
        Includes plots for:
            * 2D position
            * 3D position
            * total kinetic energy over time
            * percentage errors in kinetic, potential and total energy
            * linear momentum
    -------------------
    Constructor:
        :param data: a dataset consisting of deep copies of all objects at all times, pulled from a numpy
        binary file file in ./data_files/
    """

    def __init__(self, data):
        self.data = data
        self.labels = [i.name for i in self.data[0][1:]]  # labels are used often, so the list of labels is stored as a class attribute
        self.times = [i[0] for i in data]  # likewise with the list of times

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
        Draws the path of all objects in the x-y-z space
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
            e_k = 0
            for j in i[1:]:  # starts at 1 to ignore time
                e_k += j.getKineticEnergy()
            e_k_list.append(e_k)

        plt.plot(self.times, np.array(e_k_list, dtype=float))
        plt.xlabel("Time (s)")
        plt.ylabel("Total kinetic energy (J)")
        plt.title("Kinetic energy evolution")

    def kineticAndPotentialEnergyPlot(self):
        """
        Draws the percentage change in kinetic energy of the system compared to energy at t=0, against time
        """

        e_k_list = []
        u_e_list = []

        for i in self.data:
            e_k = 0
            u_e = 0
            for j in i[1:]:  # starts at 1 to ignore time
                e_k += j.getKineticEnergy()
                u_e += j.getPotentialEnergy(i[1:])
            e_k_list.append(e_k)
            u_e_list.append(u_e)
        e_k_list = np.array(e_k_list)
        u_e_list = np.array(u_e_list)
        tot_energy = e_k_list + u_e_list

        y1_values = [(e_k_list[0] - i) * 100 / e_k_list[0] for i in e_k_list]
        y2_values = [(u_e_list[0] - i) * 100 / u_e_list[0] for i in u_e_list]
        y3_values = [(tot_energy[0] - i) * 100 / tot_energy[0] for i in tot_energy]

        plt.plot(self.times, y1_values, "--", label="Kinetic energy")
        plt.plot(self.times, y2_values, "--", label="Potential energy")
        plt.plot(self.times, y3_values, label="Total energy", color="r")

        print(sum(y1_values) / len(y1_values))
        plt.xlabel("Time (s)")
        plt.ylabel("Percentage error")
        plt.title("Percentage error in energy")
