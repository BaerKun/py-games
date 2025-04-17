import pygame
import random
import os

pygame.init()

w, h = 1000, 800
scr = pygame.display.set_mode((w, h))
scr.fill((250, 250, 200))

pygame.display.set_caption("foodie snake")

# ————snake————
snake_head = 100, 100
snake_r, length = 25, 24
snake_body = []
for i in range(length):
    snake_body += [snake_head]
snake_speed = 0, 0
snake_speed_ = 5

food_all = {}
food_size = 40
apple_image = pygame.image.load('apple.png')
apple = pygame.transform.scale(apple_image, (food_size, food_size))
banana_image = pygame.image.load('banana.png')
banana = pygame.transform.scale(banana_image, (food_size, food_size))
shit_image = pygame.image.load('shit.png')
shit = pygame.transform.scale(shit_image, (food_size, food_size))
food_total = [apple, banana]
score = 0
shit_if = False
have_eaten = 0

font_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'fonts/Arial.ttf')
font_50 = pygame.font.Font(font_path, 50)
font_200 = pygame.font.Font(font_path, 200)
pause = font_200.render('PAUSE', True, (0, 0, 0))
pause_size = pause.get_size()
clock = pygame.time.Clock()
t = 0

pygame.display.flip()


def distance(one, two):
    return ((one[0] - two[0]) ** 2 + (one[1] - two[1]) ** 2) ** 0.5


while True:
    clock.tick(60)
    t += 1

    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            exit()
        if event1.type == pygame.KEYDOWN:
            match event1.key:
                case 119:
                    snake_speed = (0, -snake_speed_)
                case 115:
                    snake_speed = (0, snake_speed_)
                case 97:
                    snake_speed = (-snake_speed_, 0)
                case 100:
                    snake_speed = (snake_speed_, 0)
                case 27:
                    scr.blit(pause, ((w - pause_size[0]) / 2, (h - pause_size[1]) / 2))
                    pygame.display.update()
                    flag = True
                    while flag:
                        for event2 in pygame.event.get():
                            if event2.type == pygame.QUIT:
                                exit()
                            if event2.type == pygame.KEYDOWN:
                                if event2.key == 27:
                                    flag = False

    scr.fill((250, 250, 200))

    # ————snake's body————
    for i in range(length - 1, 0, -1):
        snake_body[i] = snake_body[i - 1]
        if i % 12 <= 5:
            pygame.draw.circle(scr, (100, 100, 100), snake_body[i], snake_r, 0)
        else:
            pygame.draw.circle(scr, (200, 200, 0), snake_body[i], snake_r, 0)

    # ————food————
    if t == 300:
        food_pos = (random.randint(food_size // 2, w - food_size // 2),
                    random.randint(food_size // 2, h - food_size // 2))
        while distance(snake_head, food_pos) < 10 * snake_r:
            food_pos = (random.randint(food_size // 2, w - food_size // 2),
                        random.randint(food_size // 2, h - food_size // 2))
        food_all[food_pos] = random.choice(food_total)
        t -= 180

    for pos, food in food_all.items():
        scr.blit(food, (pos[0] - food_size // 2, pos[1] - food_size // 2))

    # ————snake's head————
    snake_body[0] = snake_head
    pygame.draw.circle(scr, (100, 100, 100), snake_body[0], snake_r, 0)

    snake_head = snake_head[0] + snake_speed[0], snake_head[1] + snake_speed[1]
    pygame.draw.circle(scr, (200, 200, 200), snake_head, snake_r, 0)

    # ————eat————
    food_del = []
    for eat in food_all:
        if distance(snake_head, eat) <= snake_r + food_size // 3:
            food_del += [eat]
            if food_all[eat] == shit:
                for short in range(6):
                    del snake_body[length - 1 - short]
                length -= 6
                snake_r -= 0.5
                score -= 5
            else:
                for grow in range(6):
                    snake_body += [snake_body[length - 1]]
                have_eaten += 1
                length += 6
                snake_r += 0.5
                score += 1
                if have_eaten == 3:
                    shit_if = True
                    have_eaten -= 3
    for eaten in food_del:
        del food_all[eaten]
    if shit_if:
        food_all[snake_body[length-1]] = shit
        shit_if = False

    # ————score————
    score_image = font_50.render(f'Score: {score}', True, (0, 0, 0))
    scr.blit(score_image, (20, 10))

    pygame.display.update()
