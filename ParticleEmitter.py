import random

class ParticleEmitter:
    def __init__(self, pos, particle_type, nparticles, speed, fdirection):
        self.particle_type = particle_type
        self.speed = speed
        self.fdirection = fdirection
        self.pos = pos
        self.die_after = 1000
        self.t = 0


        # Initialize particles width rand speed and direction and emitters pos
        self.particles = []
        for p in range(nparticles):
            speed_seed = [
                    random.random(),
                    random.random(),
                    random.random()
                    ]
            direction_seed = [
                    random.random(),
                    random.random(),
                    random.random()
                    ]
            self.particles.append(self.particle_type(pos, speed_seed, direction_seed, die_after=self.die_after))

    def update(self):
        self.t += 1
        for p in self.particles:
            p.update()
            p.render()

#  def render(self):
        #  self.t += 1

        #glBegin(GL_POINTS);

        #  for p in self.particles:
        #  glVertex3v()

