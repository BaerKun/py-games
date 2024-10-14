import pygame
import random

pygame.init()

w, h = 1000, 800
scr = pygame.display.set_mode((w, h))
scr.fill((250, 250, 200))

pygame.display.set_caption("贝尔大战斯内克")

# ————snake————
snake_head = (50, 50)
snake_body_r, length, snake_blood_ = 40, 152, 500
snake_head_r = 1.2 * snake_body_r
snake_blood = snake_blood_
snake_body = []
for i in range(length):
    snake_body += [snake_head]
snake_speed = 0, 0
snake_speed_slow, snake_speed_fast = 4.5, 8
snake_speed_ = snake_speed_slow
go = (random.randint(0, w), random.randint(0, h))
acc_slow, acc_fast = 0.1, 2
acc = acc_slow

# ————bear————
bear = w - 50, h - 50
bear_speed = 0, 0
bear_speed_slow, bear_speed_fast = 7, 12
bear_speed_ = bear_speed_slow
bear_r = 30
mouse = bear

# ————bullet————
bullet = []
bullet_if = []
bullet_speed = []
for i in range(10):
    bullet += [bear]
    bullet_if += [False]
    bullet_speed += [0]
bullet_r, bullet_speed_, bullet_number, bullet_harm = 10, 12, 10, 10
fire = 0

snake_cold = pygame.image.load('snake_cold.png')
snake_cold = pygame.transform.scale(snake_cold, (2 * snake_head_r, 2 * snake_head_r))
snake_hot = pygame.image.load('snake_hot.png')
snake_hot = pygame.transform.scale(snake_hot, (2 * snake_head_r, 2 * snake_head_r))
bear_image = pygame.image.load('bear.png')
bear_image = pygame.transform.scale(bear_image, (2 * bear_r, 2 * bear_r))
head_image = snake_cold

font_100 = pygame.font.Font(r"C:\Windows\Fonts\simkai.ttf", 100)
font_50 = pygame.font.Font(r"C:\Windows\Fonts\simkai.ttf", 50)
text_snake = font_50.render('斯内克', True, (100, 50, 0))
text_snake_size = text_snake.get_size()
text_over = font_100.render('GAME OVER', True, (0, 0, 0))
text_over_size = text_over.get_size()

clock = pygame.time.Clock()

pygame.display.flip()


def distance(one, two):
    return ((one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2) ** 0.5


def triangle(beginning, end):
    l = distance(beginning, end)
    c = (end[0] - beginning[0]) / l
    s = (end[1] - beginning[1]) / l
    return c, s


def snake_move(beginning, end, speed):
    l = distance(beginning, end)
    co = (end[0] - beginning[0]) / l
    si = (end[1] - beginning[1]) / l
    a = acc * l / snake_body_r / 5
    v_x = speed[0] + co * a
    v_y = speed[1] + si * a
    v = (v_x ** 2 + v_y ** 2) ** 0.5
    if v > snake_speed_:
        v_x = v_x * snake_speed_ / v
        v_y = v_y * snake_speed_ / v
    return v_x, v_y


def bear_move(beginning, end):
    l = distance(beginning, end)
    if l <= bear_speed_ / 2:
        si = co = 0
    else:
        co, si = triangle(beginning, end)
    return bear_speed_ * co, bear_speed_ * si


while True:
    clock.tick(60)

    snake_body[0] = snake_head
    bear = bear[0] + bear_speed[0], bear[1] + bear_speed[1]
    snake_head = snake_head[0] + snake_speed[0], snake_head[1] + snake_speed[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            fire += 1
            if fire == bullet_number:
                fire -= bullet_number
            if not bullet_if[fire]:
                bullet_if[fire] = True
                cos, sin = triangle(bear, snake_head)
                bullet[fire] = bear[0] + bear_r * cos, bear[1] + bear_r * sin
                bullet_speed[fire] = bullet_speed_ * cos, bullet_speed_ * sin
        if event.type == pygame.KEYDOWN:
            if event.key == 32:
                bear_speed_ = bear_speed_fast
        elif event.type == pygame.KEYUP:
            if event.key == 32:
                bear_speed_ = bear_speed_slow

    scr.fill((250, 250, 200))

    # ————snake's body's move————
    for i in range(length - 1, 0, -1):
        snake_body[i] = snake_body[i - 1]
        if i % 12 <= 5:
            pygame.draw.circle(scr, (100, 100, 100), snake_body[i], snake_body_r, 0)
        else:
            pygame.draw.circle(scr, (200, 200, 0), snake_body[i], snake_body_r, 0)
    pygame.draw.circle(scr, (100, 100, 100), snake_body[0], snake_body_r, 0)

    # ————bear's move————
    bear_speed = bear_move(bear, mouse)
    scr.blit(bear_image, (bear[0] - bear_r, bear[1] - bear_r))

    # ————snake's head's move————
    if snake_speed_ == snake_speed_slow:
        while distance(snake_head, go) <= 5 * snake_body_r:
            go = random.randint(0, w), random.randint(0, h)
    else:
        go = bear
    snake_speed = snake_move(snake_head, go, snake_speed)
    scr.blit(head_image, (snake_head[0] - snake_head_r, snake_head[1] - snake_head_r))

    # ————fire————
    for i in range(bullet_number):
        if bullet_if[i]:
            bullet[i] = bullet[i][0] + bullet_speed[i][0], bullet[i][1] + bullet_speed[i][1]
            pygame.draw.circle(scr, (250, 50, 150), bullet[i], bullet_r, 0)
            if not -bullet_r < bullet[i][0] < w + bullet_r or not -bullet_r < bullet[i][1] < h + bullet_r:
                bullet_if[i] = False
            elif distance(bullet[i], snake_head) <= snake_head_r + bullet_r:
                snake_blood -= bullet_harm
                bullet_if[i] = False

    # ————snake's blood————
    pygame.draw.rect(scr, (255, 50, 50), (0.2 * w, 10, 0.6 * w * snake_blood / snake_blood_, 50))
    scr.blit(text_snake, ((w - text_snake_size[0]) / 2, 35 - text_snake_size[1] / 2))

    pygame.display.update()

    if snake_blood_ / 2 <= snake_blood <= 0.8 * snake_blood_ or snake_blood <= snake_blood_ * 0.4:
        snake_speed_, acc, head_image = snake_speed_fast, acc_fast, snake_hot
    else:
        snake_speed_, acc, head_image = snake_speed_slow, acc_slow, snake_cold
    if snake_blood <= 0 or distance(snake_head, bear) < snake_head_r + bear_r:
        scr.blit(text_over, ((w - text_over_size[0]) / 2, (h - text_over_size[1]) / 2))
        pygame.display.update()

        while True:
            clock.tick(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
