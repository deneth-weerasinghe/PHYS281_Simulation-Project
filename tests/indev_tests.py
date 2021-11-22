import numpy as np
from base_classes.Particle import Particle

# print(Particle.getUnitVector(np.array([1, 2, 3])))

particle_1 = Particle(position=np.array([0, 10, 0]))
particle_2 = Particle(position=np.array([0, 0, 0]))

particle_2.updateGravitationalAcceleration(particle_1)

print("The Earth and Satellites Location after {0} seconds is:".format((2000 * 6)))
for particle in [Earth, Satellite]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute,
                                  particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!
