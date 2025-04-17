import pygame

pygame.init()

s = 50
w, h = s * 18, s * 12
scr = pygame.display.set_mode((w, h))

font_path = 'fonts/Arial.ttf'
font_small = pygame.font.Font(font_path, 11)
font_big = pygame.font.Font(font_path, 50)
clock = pygame.time.Clock()
t = 0

i = 0
for a in range(6):
    for b in range(6):
        for c in range(6):
            pygame.draw.rect(scr, (50 * a, 50 * b, 50 * c), (i % 18 * s, i // 18 * s, s, s), 0)
            text = font_small.render("%a,%a,%a" % (50 * a, 50 * b, 50 * c), True,
                                     (255 - 50 * a, 255 - 50 * b, 255 - 50 * c))
            scr.blit(text, (i % 18 * s, i // 18 * s))
            i += 1

pygame.display.flip()

while True:
    clock.tick(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            t += 1
            if t % 2 == 0:
                i = 0
                for a in range(6):
                    for b in range(6):
                        for c in range(6):
                            pygame.draw.rect(scr, (50 * a, 50 * b, 50 * c), (i % 18 * s, i // 18 * s, s, s), 0)
                            text = font_small.render("%a,%a,%a" % (50 * a, 50 * b, 50 * c), True,
                                                     (255 - 50 * a, 255 - 50 * b, 255 - 50 * c))
                            scr.blit(text, (i % 18 * s, i // 18 * s))
                            i += 1
            else:
                i = 0
                mouse = event.pos
                for a in range(6):
                    for b in range(6):
                        for c in range(6):
                            rect = pygame.Rect(i % 18 * s, i // 18 * s, s, s)
                            if rect.collidepoint(mouse):
                                pygame.draw.rect(scr, (50 * a, 50 * b, 50 * c), (0, 0, w, h))
                                text = font_big.render("%a,%a,%a" % (50 * a, 50 * b, 50 * c), True,
                                                       (255 - 50 * a, 255 - 50 * b, 255 - 50 * c))
                                scr.blit(text, (0, 0))
                            i += 1
    pygame.display.update()
