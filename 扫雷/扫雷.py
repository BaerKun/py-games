import pygame
from random import sample
import time

pygame.init()

w, h, l, mines_number = 520, 620, 20, 70
scr = pygame.display.set_mode((w, h))
pygame.display.set_caption('扫雷')

# 加载图片、字体
mine_image = pygame.image.load('mine.png')
mine_image = pygame.transform.scale(mine_image, (l, l))
button_image = pygame.image.load('button.png')
button_image = pygame.transform.scale(button_image, (l, l))
flag_image = pygame.image.load('button.png')
flag_image = pygame.transform.scale(flag_image, (l, l))
flag = pygame.image.load('flag.png')
flag = pygame.transform.scale(flag, (l * 0.8, l * 0.8))
flag_image.blit(flag, (l * 0.1, l * 0.1))
replay = pygame.image.load('replay.png')
replay = pygame.transform.scale(replay, (80, 80))
replay_image = pygame.surface.Surface((80, 80))
replay_image.fill((200, 255, 255))
replay_image.blit(replay, (0, 0))
font_num = pygame.font.Font(r"C:\Windows\Fonts\simkai.ttf", 20)
font_up = pygame.font.Font(r"C:\Windows\Fonts\simkai.ttf", 70)


class Button(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = button_image
        self.rect = position
        self.Rect = pygame.Rect(position[0], position[1], l, l)


def build_map():
    buttons = pygame.sprite.Group()
    map1 = {}
    for a in range(0, w, l):
        for b in range(100, h, l):
            buttons.add(Button((a, b)))
            map1[(a, b)] = False
    mines = set(sample(list(map1), mines_number))
    for mine in mines:
        map1[mine] = True

    background = pygame.Surface((w, h))
    background.fill((230, 255, 255))
    pygame.draw.rect(background, (50, 200, 255), (0, 0, w, 100), 0)
    pygame.draw.rect(background, (200, 255, 255), (20, 10, 200, 80), 0)
    pygame.draw.rect(background, (200, 255, 255), (400, 10, 100, 80), 0)
    for a in range(l, w, l):
        pygame.draw.line(background, (150, 200, 250), (a, 100), (a, h), 2)
    for b in range(100, h, l):
        pygame.draw.line(background, (150, 200, 250), (0, b), (w, b), 2)
    map2 = {}
    scr.blit(background, (0, 0))
    for pos, jud in map1.items():
        x, y = pos
        if jud:
            map2[pos] = -1
            background.blit(mine_image, pos)
        else:
            mine_num = 0
            for a in range(-l, l + 1, l):
                for b in range(-l, l + 1, l):
                    if (x + a, y + b) in map1 and map1[(x + a, y + b)]:
                        mine_num += 1
            map2[pos] = mine_num
            if mine_num:
                text_num = font_num.render(str(mine_num), True, (0, 0, 0))
                u, v = text_num.get_size()
                background.blit(text_num, (x + l / 2 - u / 2, y + l / 2 - v / 2))
    return map2, mines, buttons, background


Map, Mines, Buttons, Background = build_map()
flags = set([])


def click_button(pos_set):
    change_if = False
    for button in Buttons:
        pos = button.rect
        if pos in pos_set:
            if not Map[pos] and pos not in flags:
                Buttons.remove(button)
                x, y = pos
                pos_set.update([(x + l, y), (x, y + l), (x - l, y), (x, y - l),
                                (x + l, y + l), (x + l, y - l), (x - l, y + l), (x - l, y - l)])
                change_if = True

    if change_if:
        click_button(pos_set)
    else:
        for button in Buttons:
            if button.rect in pos_set and button.rect not in flags:
                Buttons.remove(button)


def timekeeping(time):
    minute, second = str(time // 60), str(time % 60)
    if len(minute) == 1:
        minute = '0' + minute
    if len(second) == 1:
        second = '0' + second
    return minute + ':' + second


clock = pygame.time.Clock()
start_time = time.time()

while True:
    clock.tick(30)

    scr.blit(Background, (0, 0))

    time_now = int(time.time() - start_time)
    text_time = font_up.render(timekeeping(time_now), True, (0, 100, 255))
    scr.blit(text_time, (35, 10))

    mines_num = mines_number - len(flags)
    text_mines = font_up.render(str(mines_num), True, (0, 100, 255))
    scr.blit(text_mines, (410, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in Buttons:
                if button.Rect.collidepoint(event.pos):
                    if event.button == 1 and button.rect not in flags:
                        if button.rect not in Mines:
                            click_button({button.rect})
                        else:
                            del Buttons
                            scr.blit(replay_image, (270, 10))
                            pygame.display.update()

                            f = True
                            while f:
                                for eve in pygame.event.get():
                                    if eve.type == pygame.QUIT:
                                        exit()
                                    elif eve.type == pygame.MOUSEBUTTONDOWN:
                                        if 270 < eve.pos[0] < 350 and 10 < eve.pos[1] < 90:
                                            Map, Mines, Buttons, Background = build_map()
                                            flags = set([])
                                            f = False
                            start_time = time.time()
                            break

                    elif event.button == 3:
                        if button.rect not in flags:
                            button.image = flag_image
                            flags.add(button.rect)
                        else:
                            button.image = button_image
                            flags.remove(button.rect)

    Buttons.draw(scr)

    pygame.display.update()

    if flags == Mines and len(Buttons) == mines_number:
        scr.blit(replay_image, (270, 10))
        pygame.display.update()

        f = True
        while f:
            for eve in pygame.event.get():
                if eve.type == pygame.QUIT:
                    exit()
                elif eve.type == pygame.MOUSEBUTTONDOWN:
                    if 270 < eve.pos[0] < 350 and 10 < eve.pos[1] < 90:
                        Map, Mines, Buttons, Background = build_map()
                        flags = set([])
                        f = False
        start_time = time.time()
