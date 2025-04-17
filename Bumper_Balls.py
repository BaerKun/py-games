from array import array
import math
import itertools
import random
import pygame

pygame.init()
pygame.display.set_caption('Bumper Balls')

w, h = 800, 600
scr = pygame.display.set_mode((w, h))
font = pygame.font.Font('fonts/Arial.ttf', 25)

clock = pygame.time.Clock()
k = 2.4
density = 0.0016
damping = 0.0001

g = 0.2
fps = 60


class Ball:
    def __init__(self, center, radius, color, velocity=(0., 0.)):
        super().__init__()
        self.center = array('d', center)
        self.radius = radius
        self.color = color
        self.vel = array('d', velocity)
        self.mass = density * radius * radius  # 质量
        self.acc = array('d', (0., g))

    def update(self):
        if self.center[0] <= self.radius:
            self.acc[0] += self.force(self.center[0]) / self.mass
        elif self.center[0] >= w - self.radius:
            self.acc[0] -= self.force(w - self.center[0]) / self.mass
        if self.center[1] <= self.radius:
            self.acc[1] += self.force(self.center[1]) / self.mass
        elif self.center[1] >= h - self.radius:
            self.acc[1] -= self.force(h - self.center[1]) / self.mass

        self.vel[0] += self.acc[0]
        self.vel[1] += self.acc[1]
        self.acc[0] = 0.
        self.acc[1] = g

        square_velocity = self.vel[0] * self.vel[0] + self.vel[1] * self.vel[1]
        velocity = math.sqrt(square_velocity)

        damping_acc = damping * square_velocity * self.radius / self.mass
        if damping_acc >= velocity:
            self.vel[0] = 0.
            self.vel[1] = 0.
            return

        self.vel[0] -= damping_acc * self.vel[0] / velocity
        self.vel[1] -= damping_acc * self.vel[1] / velocity

        self.center[0] += self.vel[0]
        self.center[1] += self.vel[1]


    def draw(self):
        pygame.draw.circle(scr, self.color, self.center, self.radius, 0)

    def force(self, x):
        if x >= self.radius:
            return 0.
        return k * (self.radius - x)


class Balls:
    def __init__(self):
        self.__balls = []

    def add(self, ball: Ball):
        self.__balls.append(ball)

    def update(self):
        for one, two in itertools.combinations(self.__balls, 2):
            dx = two.center[0] - one.center[0]
            dy = two.center[1] - one.center[1]
            dist = math.sqrt(dx * dx + dy * dy)
            if dist < one.radius + two.radius:
                if one.radius >= two.radius:
                    force = one.force(dist - two.radius)
                else:
                    force = two.force(dist - one.radius)

                fx = force * dx / dist
                fy = force * dy / dist
                one.acc[0] -= fx / one.mass
                one.acc[1] -= fy / one.mass
                two.acc[0] += fx / two.mass
                two.acc[1] += fy / two.mass

        for ball in self.__balls:
            ball.update()

    def draw(self):
        for ball in self.__balls:
            ball.draw()

    def kinetic_energy(self):
        energy = 0.
        for ball in self.__balls:
            energy += ball.mass * (ball.vel[0] * ball.vel[0] + ball.mass * ball.vel[1] * ball.vel[1]) / 2
        return energy


balls = Balls()
for _ in range(20):
    balls.add(Ball((random.uniform(0, w), random.uniform(0, h)),
                   random.uniform(20, 30),
                   (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.uniform(-10, 10), random.uniform(-10, 10))))

pygame.display.flip()
while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    scr.fill((255, 255, 255))
    balls.update()
    balls.draw()
    scr.blit(font.render(f'kinetic energy: {balls.kinetic_energy()}', True, (0, 0, 0)), (10, 10))

    pygame.display.update()
