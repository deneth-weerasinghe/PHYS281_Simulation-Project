from poliastro import constants
from base_classes.EphemeridesObjects import EphemeridesObjects

labels = ["Sun", "Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
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

t_raw = "2021-12-04 00:00:00.0"

solar_system = EphemeridesObjects(t_raw, labels, raw_masses)
objects = solar_system.obtainObjects()
