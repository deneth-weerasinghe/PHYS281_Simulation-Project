from base_classes.particle import Particle

particle_1 = Particle(name="particle_1")
print(particle_1)
for i in range(5):
    particle_1.update(0.1)
    print(particle_1)