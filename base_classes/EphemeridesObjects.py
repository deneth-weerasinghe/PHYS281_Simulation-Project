import astropy.constants
import numpy as np
from base_classes.Particle import Particle
from spiceypy import sxform, mxvg
from astropy.time import Time
from astropy.coordinates import get_body_barycentric_posvel
from poliastro import constants


class EphemeridesObjects:
    """
    Stores initial conditions pulled from JPL to be used for instances of Particle
    """

    def __init__(self, raw_t_0="2021-12-04 00:00:00.0",
                 labels=None,
                 raw_masses=None):

        #  default values; this format of setting default values has been suggested by my IDE
        if raw_masses is None:
            raw_masses = [constants.GM_sun,
                          constants.GM_mercury,
                          constants.GM_venus,
                          constants.GM_earth,
                          constants.GM_moon,
                          constants.GM_mars,
                          constants.GM_jupiter,
                          constants.GM_saturn,
                          constants.GM_uranus,
                          constants.GM_neptune,
                          constants.GM_pluto,
                          ]
        if labels is None:
            labels = ["Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune",
                      "Pluto"]

        self.t_0 = Time(raw_t_0, scale="tdb")
        self.labels = labels
        self.raw_masses = raw_masses

    def getInitialConditions(self, obj):
        """
        Obtains initials conditions to be used in creating Particle objects in the loop in obtainObjects
        :param obj: index value used to determine which celestial object within the labels attribute list is being used
        :return: 2 numpy arrays containing the initial position and velocity of the object
        """
        pos, vel = get_body_barycentric_posvel(self.labels[obj].lower(), self.t_0, ephemeris="jpl")

        state_vec = [
            pos.xyz[0].to("m").value,
            pos.xyz[0].to("m").value,
            pos.xyz[0].to("m").value,
            vel.xyz[0].to("m/s").value,
            vel.xyz[0].to("m/s").value,
            vel.xyz[0].to("m/s").value,
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
                    acceleration=np.array([0, 0, 0], dtype=float),
                    name=label,
                    mass=EphemeridesObjects.getMass(self.raw_masses[i])
                )
            )
        return system_list
