import astropy.constants
import numpy as np
from base_classes.Particle import Particle
from spiceypy import sxform, mxvg
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from poliastro import constants


class EphemeridesObjects:
    """
    Class that stores initial conditions pulled from the JPL Ephemeris to be used for instantiating the Particle class

    -----------
    Constructor
    :param raw_t_0: string; the real date and time of the initial conditions, i.e. t_0
    :param simulated_objects: dictionary containing the string name of each simulated object and the corresponding
    masses, the latter pulled from poliastro
    this is preferable to pulling the actual mass as it is less accurate than mass * G in the Ephemeris3
    """

    def __init__(self, raw_t_0="2021-12-04 00:00:00.0", simulated_objects=None
                 ):

        #  default values; this format of setting default values has been suggested by my IDE

        if simulated_objects is None:
            simulated_objects = {"Sun": constants.GM_sun,
                                 "Mercury": constants.GM_mercury,
                                 "Venus": constants.GM_venus,
                                 "Earth": constants.GM_earth,
                                 "Mars": constants.GM_mars,
                                 "Jupiter": constants.GM_jupiter,
                                 "Saturn": constants.GM_saturn,
                                 "Uranus": constants.GM_uranus,
                                 "Neptune": constants.GM_neptune,
                                 "Pluto": constants.GM_pluto}
        self.t_0 = Time(raw_t_0, scale="tdb")
        self.labels = list(simulated_objects.keys())
        self.raw_masses = list(simulated_objects.values())

    def getInitialConditions(self, obj):
        """
        Obtains initials conditions to be used in creating Particle objects in the loop in obtainObjects
        :param obj: index value used to determine which celestial object within the labels attribute list is being used
        :return: 2 numpy arrays containing the initial position and velocity of the object
        """
        pos, vel = get_body_barycentric_posvel(self.labels[obj].lower(), self.t_0, ephemeris="jpl")

        state_vec = [
            pos.xyz[0].to("m").value,
            pos.xyz[1].to("m").value,
            pos.xyz[2].to("m").value,
            vel.xyz[0].to("m/s").value,
            vel.xyz[1].to("m/s").value,
            vel.xyz[2].to("m/s").value,
        ]

        #  get transformation matrix to the ecliptic (use time in Julian days)
        transform = sxform("J2000", "ECLIPJ2000", self.t_0.jd)

        #  transform state vector to ecliptic
        state_vec_ec = mxvg(transform, state_vec, 6, 6)

        #  positions and velocities
        position = [state_vec_ec[0], state_vec_ec[1], state_vec_ec[2]]  # FINAL VALUE
        velocity = [state_vec_ec[3], state_vec_ec[4], state_vec_ec[5]]  # FINAL VALUE

        return np.array(position, dtype=float), np.array(velocity, dtype=float)

    @staticmethod
    def getMass(raw_mass):
        """
        Calculates the mass of the object using the mass multiplied by G from the poliastro module. This is more
        accurate than directly using the mass provided by poliastro
        :param raw_mass: the G * mass from poliastro; an object in a class within poliastro
        :return: float mass of object in kg
        """
        mass = (raw_mass / astropy.constants.G).value
        return mass

    def obtainObjects(self):
        """
        Generates a list of Particle objects using the arguments provided to an instance of this class
        :return: list of Particle objects
        """
        system_list = []
        for i, label in enumerate(self.labels):
            pos, vel = self.getInitialConditions(i)

            system_list.append(
                Particle(
                    position=np.array(pos, dtype=float),
                    velocity=np.array(vel, dtype=float),
                    acceleration=np.array([0, -10, 0], dtype=float),
                    name=label,
                    mass=EphemeridesObjects.getMass(self.raw_masses[i])
                )
            )
        return system_list
