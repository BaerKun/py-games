import pygame
import itertools
from random import randint

pygame.init()
pygame.display.set_caption('Colorful Balls')

w, h = 800, 600
scr = pygame.display.set_mode((w, h))

ziti = pygame.font.Font('C:/Windows/Fonts/STXINGKA.TTF', 25)

pygame.display.flip()


class ForceField(pygame.sprite.Sprite):
    def __init__(self, x,y,w,h):
        super().__init__()
        self.rect = pygame.Rect(x,y,w,h)

    def


clock = pygame.time.Clock()
g = 0.1
frequency = 60
force = 10


class Ball(pygame.sprite.Sprite):
    def __init__(self, position, radius, color, speed=(0, 0)):
        super().__init__()
        self.pos = position
        self.radius = radius
        self.rect = pygame.Rect(position[0] - radius / 2, position[1] - radius / 2, radius, radius)
        self.col = color
        self.spe = speed
        self.mass = radius ** 2 // 100
        self.acc = 0, g

    def update(self):
        if self.pos[0] >= w - self.radius:
            self.acc = self.acc[0] - 20 * g, self.acc[1]
        elif self.pos[0] <= self.radius:
            self.acc = self.acc[0] + 20 * g, self.acc[1]
        if self.pos[1] >= h - self.radius:
            self.acc = self.acc[0], self.acc[1] - 20 * g
        elif self.pos[1] <= self.radius:
            self.acc = self.acc[0], self.acc[1] + 20 * g
        self.spe = self.spe[0] + self.acc[0], self.spe[1] + self.acc[1]
        self.pos = self.pos[0] + self.spe[0], self.pos[1] + self.spe[1]
        self.acc = 0, g
        self.rect = pygame.Rect(self.pos[0] - self.radius / 2, self.pos[1] - self.radius / 2, self.radius, self.radius)


class Balls(pygame.sprite.Group):
    def collide(self):
        for one, two in itertools.combinations(self, 2):
            if (dd := (one.pos[0] - two.pos[0]) ** 2 + (one.pos[1] - two.pos[1]) ** 2) <= (
                    one.radius + two.radius) ** 2:
                one.acc = (one.acc[0] + force * (one.pos[0] - two.pos[0]) * (one.radius + two.radius) / one.mass / dd,
                           one.acc[1] + force * (one.pos[1] - two.pos[1]) * (one.radius + two.radius) / one.mass / dd)
                two.acc = (two.acc[0] - force * (one.pos[0] - two.pos[0]) * (one.radius + two.radius) / two.mass / dd,
                           two.acc[1] - force * (one.pos[1] - two.pos[1]) * (one.radius + two.radius) / two.mass / dd)

    def draw(self, **kwargs):
        for ball in self:
            pygame.draw.circle(scr, ball.col, ball.pos, ball.rad, 0)


balls = Balls()
for i in range(10):
    balls.add(
        Ball((randint(50, 750), randint(50, 550)), randint(30, 50), (randint(0, 255), randint(0, 255), randint(0, 255)),
             ))
balls.add(Ball((400, 300), 80, (129, 232, 93)))

while True:
    clock.tick(frequency)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    scr.fill((255, 255, 255))
    balls.update()
    balls.collide()
    balls.draw()
    pygame.display.update()
