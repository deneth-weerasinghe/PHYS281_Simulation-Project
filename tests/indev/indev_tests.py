from poliastro import constants


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

x = list(simulated_objects.values())
print(x)