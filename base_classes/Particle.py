import numpy as np


class Particle:
    """
    Class constants

    :cvar G: gravitational constant
    """

    G = 6.67408E-11

    def __init__(self,
                 position=np.array([0, 0, 0], dtype=float),
                 velocity=np.array([0, 0, 0], dtype=float),
                 acceleration=np.array([0, -10, 0], dtype=float),
                 name="Ball",
                 mass=1.0
                 ):
        """
        Instance constructor

        :param position: position of particle at t=0; 3D vector as a numpy array
        :param velocity: velocity of particle at t=0; 3D vector as a numpy array
        :param acceleration: acceleration of particle at t=0; 3D vector as a numpy array
        :param name: identifier for particle
        :param mass: mass of particle; assume no relativistic effects on mass
        """

        # class variables
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype=float)  # Copies input array and converts all elements into floats
        self.velocity = np.array(velocity, dtype=float)
        self.acceleration = np.array(acceleration, dtype=float)

    def __str__(self):
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass, self.position, self.velocity, self.acceleration
        )

    def update(self, deltaT):
        self.position += self.velocity * deltaT
        self.velocity += self.acceleration * deltaT
