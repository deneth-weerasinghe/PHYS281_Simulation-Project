import numpy as np
from astropy.constants import G


class Particle:

    def __init__(self,
                 position=np.array([0, 0, 0], dtype=float),
                 velocity=np.array([0, 0, 0], dtype=float),
                 acceleration=np.array([0, -10, 0], dtype=float),
                 name="Ball",
                 mass=1.0,
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

        :param delta_t: integer; time interval
        """
        self.position += self.velocity * delta_t
        self.velocity += self.acceleration * delta_t

    def updateEulerCromer(self, delta_t):
        """
        Euler-Cromer method for updating the position of an object: object velocity is updated before position

        :param delta_t: integer; time interval
        """
        self.velocity += self.acceleration * delta_t
        self.position += self.velocity * delta_t

    def updateEulerRichardson(self, delta_t, objects):
        """
        Euler-Richardson method for updating position and velocity: position, velocity and acceleration are
        calculated for t = delta_t / 2 and these values are used to calculate the position and velocity class
        attributes
        :param delta_t: integer; time interval
        :param objects: list of Particle objects, used to calculate a_mid
        """
        x_mid = self.position + 0.5 * self.velocity * delta_t
        v_mid = self.velocity + 0.5 * self.acceleration * delta_t
        a_mid = self.NBodyAcceleration(objects, x_mid=x_mid)

        self.velocity += a_mid * delta_t
        self.position += v_mid * delta_t

    def updateVerler(self, delta_t, objects):
        """
        Verler method for updating position and velocity: position is calculate according to classical kinematics and
        velocity requires both the current acceleration (saved in a dummy variable) and the updated acceleration using
        the newly updated position
        :param delta_t: integer; time interval
        :param objects: list of Particle objects, used as a argument for the new acceleration
        :return:
        """
        current_a = self.acceleration

        self.position += self.velocity * delta_t + 0.5 * self.acceleration * delta_t ** 2
        self.setAcceleration(self.NBodyAcceleration(objects))
        self.velocity += 0.5 * (self.acceleration + current_a) * delta_t

    def setAcceleration(self, g):
        self.acceleration = np.array(g, dtype=float)

    def twoBodiesAcceleration(self, body, richardson=False, x_mid=None):
        """
        Updates acceleration of object based on the gravitational field induced by another object
        :param body: instance of this class; the other object that influences the gravitational acceleration
        :param richardson: boolean; checks if this method has been called by updateEulerRichardson; default: False
        :param x_mid: the "middle" position used in EulerRichardson calculations
        """

        temp_pos = self.position
        # changes the position vector if called by updateEulerRichardson
        if richardson:
            temp_pos = x_mid

        relative_position = temp_pos - body.position
        # print(relative_position)
        scalar_distance = np.linalg.norm(temp_pos - body.position)
        g = - ((G * body.mass) / (scalar_distance ** 2)) * Particle.getUnitVector(relative_position)
        return np.array(g, dtype=float)

    def NBodyAcceleration(self, objects, x_mid=None):
        """
        Updates the acceleration of the object based on the resultant acceleration due to the masses of all other
        objects by using the twoBodiesAcceleration method in a loop

        :param objects: list of Particle objects
        :param x_mid: "middle" position for se in EulerRichardson calculations
        """

        g = 0
        for i in objects:
            if i != self:  # exclude self from the calculation of resultant acceleration
                g += Particle.twoBodiesAcceleration(self, i, x_mid=x_mid)
        return np.array(g, dtype=float)

    def getKineticEnergy(self):
        """
        Calculates and returns the kinetic energy of the particle

        :return: float; kinetic energy
        """
        e_k = 0.5 * self.mass * np.linalg.norm(self.velocity) ** 2
        return e_k

    def getMomentum(self):
        """
        Method for obtaining the momentum vector of the particle
        :return: numpy array of floats; 3-vector of momentum
        """
        momentum = self.mass * self.velocity
        return np.array(momentum, dtype=float)

    @staticmethod
    def getUnitVector(a):
        """
        Takes a vector as argument and returns its unit vector

        :param a: vector to extract direction from
        :return: a unit vector in the same direction as :param a
        """
        return np.array(a / np.linalg.norm(a), dtype=float)
