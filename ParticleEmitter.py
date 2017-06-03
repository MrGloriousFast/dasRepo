class ParticleEmitter:
    def __init__(self, pos, particle_type, nparticles, fspeed, fdirection):
        self.particle_type = particle_type
        self.fspeed = fspeed
        self.fdirection = fdirection
        self.particles = [self.particle_type(pos, fspeed(), fdirection()) for i in range(nparticles)]


    def update(self):
        for p in self.particles:
            p.update()

#  def render(self):
        #  self.t += 1

        #glBegin(GL_POINTS);

        #  for p in self.particles:
        #  glVertex3v()

