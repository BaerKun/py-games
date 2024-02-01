import pygame

pygame.init()
pygame.display.set_caption('球王争霸赛')

w, h = 600, 600
scr = pygame.display.set_mode((w, h))

ziti = pygame.font.Font('C:/Windows/Fonts/STXINGKA.TTF', 25)

pygame.display.flip()

clock = pygame.time.Clock()
r = 35
a = 0.5
ball_number = 0
ball_start = 0
v_start = 10
dert = 20


def move(x, y, v_x, v_y):
    if h - r > y > r:
        v_y += a
    else:
        v_y = -v_y
    if x >= w - r or x <= r:
        v_x = -v_x
    return v_x, v_y


def collide(x, v, y, u):
    dx = x[0] - y[0]
    dy = x[1] - y[1]
    vx, vy, ux, uy = v[0], v[1], u[0], u[1]
    s = abs(dy) / d
    c = abs(dx) / d
    if dx == 0 or dy / dx < 0:
        s = -s
    v_x = ux * c ** 2 - uy * s * c + vx * s ** 2 + vy * s * c
    v_y = - ux * s * c + uy * s ** 2 + vx * s * c + vy * c ** 2
    u_x = vx * c ** 2 - vy * s * c + ux * s ** 2 + uy * s * c
    u_y = - vx * s * c + vy * s ** 2 + ux * s * c + uy * c ** 2
    return v_x, v_y, u_x, u_y


while True:
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = event.pos
            ball_start += 1

        elif ball_start == 1 and event.type == pygame.MOUSEBUTTONUP:
            x1, y1 = mouse_down
            mouse_up_x, mouse_up_y = event.pos
            l = ((mouse_up_x-x1)**2+(mouse_up_y-y1)**2)**0.5
            if l == 0:
                sin = cos = 0
            else:
                sin = (mouse_up_y-y1)/l
                cos = (mouse_up_x-x1)/l
            if l > r:
                l = r
            v1_x, v1_y = v_start * cos * l / r, v_start * sin * l / r
            ball_number = 1

        elif ball_start == 2 and event.type == pygame.MOUSEBUTTONUP:
            x2, y2 = mouse_down
            mouse_up_x, mouse_up_y = event.pos
            l = ((mouse_up_x-x2)**2+(mouse_up_y-y2)**2)**0.5
            sin = (mouse_up_y-y2)/l
            cos = (mouse_up_x-x2)/l
            if l > r:
                l = r
            v2_x, v2_y = v_start * cos * l / r, v_start * sin * l / r
            ball_number = 2

        elif ball_number == 2 and event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                y1 += dert
                y2 += dert
            elif keys[pygame.K_DOWN]:
                y1 -= dert
                y2 -= dert
            elif keys[pygame.K_LEFT]:
                x1 += dert
                x2 += dert
            elif keys[pygame.K_RIGHT]:
                x1 -= dert
                x2 -= dert

        elif event.type == pygame.QUIT:
            exit()

    if ball_number >= 1:
        x1 += v1_x
        y1 += v1_y
        v1_x, v1_y = move(x1, y1, v1_x, v1_y)

    if ball_number == 2:
        x2 += v2_x
        y2 += v2_y
        v2_x, v2_y = move(x2, y2, v2_x, v2_y)
        d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if d <= 2 * r:
            v1_x, v1_y, v2_x, v2_y = collide((x1, y1), (v1_x, v1_y), (x2, y2), (v2_x, v2_y))

    scr.fill((255, 255, 255))
    if ball_number >= 1:
        pygame.draw.circle(scr, (255, 0, 0), (x1, y1), r, 0)
    if ball_number == 2:
        pygame.draw.circle(scr, (0, 0, 255), (x2, y2), r, 0)

    if ball_start == ball_number + 1 and ball_start <= 2:
        pygame.draw.circle(scr, (150, 150, 150), mouse_down, 1.5 * r, 10)
        pygame.draw.circle(scr, (50, 50, 50), mouse_down, 0.8 * r, 10)
    pygame.display.update()
