class Particle:
    def __init__(self, pos, speed, direction):
        self.pos = pos
        self.speed = speed
        self.direction = direction
        self.tdelta = 10

    def update(self):
        pos = pos+speed
        self.speed[2] -= self.tdelta * self.speed[2]
        self.pos[0] += self.speed[0] * self.tdelta
        self.pos[1] += self.speed[1] * self.tdelta
        self.pos[2] += self.speed[2] * self.tdelta

    def render(self):
        glVertex3v(*self.pos);
