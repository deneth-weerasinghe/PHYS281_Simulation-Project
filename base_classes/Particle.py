import numpy as np
from astropy.constants import G


class Particle:

    def __init__(self,
                 position=np.array([0, 0, 0], dtype=float),
                 velocity=np.array([0, 0, 0], dtype=float),
                 acceleration=np.array([0, -10, 0], dtype=float),
                 name="Ball",
                 mass=1.0,
                 colour="r"
                 ):
        """
        Constructor

        :param position: position of particle at t=0; 3D vector as a numpy array
        :param velocity: velocity of particle at t=0; 3D vector as a numpy array
        :param acceleration: acceleration of particle at t=0; 3D vector as a numpy array
        :param name: identifier for particle
        :param mass: mass of particle; assume no relativistic effects on mass
        """

        # class variables
        self.colour = colour
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)  # Copies input array and converts all elements into floats
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def updateEuler(self, delta_t):
        """
        Euler method for updating the position of an object: position is updated before object velocity

        :param delta_t: time interval
        """
        self.position += self.velocity * delta_t
        self.velocity += self.acceleration * delta_t

    def updateEulerCromer(self, delta_t):
        """
        Euler-Cromer method for updating the position of an object: object velocity is updated before position

        :param delta_t: time interval
        """
        self.velocity += self.acceleration * delta_t
        self.position += self.velocity * delta_t

    def setAcceleration(self, g):
        self.acceleration = np.array(g, dtype=float)

    def twoBodiesAcceleration(self, body):
        """
        Updates acceleration of object based on the gravitational field induced by another object

        :param body: instance of this class; the other object that influences the gravitational acceleration
        """

        relative_position = self.position - body.position
        scalar_distance = np.linalg.norm(self.position - body.position)
        g = - ((G * body.mass) / (scalar_distance ** 2)) * Particle.getUnitVector(relative_position)
        return np.array(g, dtype=float)

    def NBodyAcceleration(self, objects):
        """
        Updates the acceleration of the object based on the resultant acceleration due to the masses of all other
        objects by using the twoBodiesAcceleration method in a loop

        :param objects: list of gravitational particles
        """

        g = 0
        for i in objects:
            if i != self:  # exclude self from the calculation of resultant acceleration
                g += Particle.twoBodiesAcceleration(self, i)
        return np.array(g, dtype=float)

    def kineticEnergy(self):
        """
        Calculates and returns the kinetic energy of the particle

        :return: kinetic energy
        """
        e_k = 0.5 * self.mass * np.linalg.norm(self.velocity) ** 2
        return e_k

    @staticmethod
    def getUnitVector(a):
        """
        Takes a vector as argument and returns its unit vector

        :param a: vector to extract direction from
        :return: a unit vector in the same direction as :param a
        """
        return np.array(a / np.linalg.norm(a), dtype=float)
