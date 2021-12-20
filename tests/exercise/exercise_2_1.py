from simulations.two_bodies_sim import *

print("The Earth and Satellites Location after {0} seconds is:".format((2000 * 6)))
for particle in [Earth, satellite_1]:
    print("  Particle: {}".format(particle.name))
    print("    Mass: {0:.3e}, ".format(particle.mass))
    for attribute in ["position", "velocity", "acceleration"]:
        print("    {}: {}".format(attribute,
                                  particle.__getattribute__(attribute) + 0.0))  # add 0.0 to avoid negative zeros!
