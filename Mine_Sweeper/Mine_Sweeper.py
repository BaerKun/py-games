import random
import pygame
import time

HEADER_HEIGHT = 100
SCREEN_WIDTH, SCREEN_HEIGHT = 520, 620
GRID_SIZE, COUNT_MINES = 20, 40

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mine Sweeper')

# 加载图片、字体
mine_image = pygame.image.load('mine.png')
mine_image = pygame.transform.scale(mine_image, (GRID_SIZE, GRID_SIZE))
button_image = pygame.image.load('button.png')
button_image = pygame.transform.scale(button_image, (GRID_SIZE, GRID_SIZE))
flag_image = pygame.image.load('button.png')
flag_image = pygame.transform.scale(flag_image, (GRID_SIZE, GRID_SIZE))
flag = pygame.image.load('flag.png')
flag = pygame.transform.scale(flag, (GRID_SIZE * 0.8, GRID_SIZE * 0.8))
flag_image.blit(flag, (GRID_SIZE * 0.1, GRID_SIZE * 0.1))
replay = pygame.image.load('replay.png')
replay = pygame.transform.scale(replay, (80, 80))
replay_image = pygame.surface.Surface((80, 80))
replay_image.fill((200, 255, 255))
replay_image.blit(replay, (0, 0))
font_matrix = pygame.font.Font("../fonts/Arial.ttf", 20)
font_header = pygame.font.Font("../fonts/Arial.ttf", 70)


class Grid:
    def __init__(self):
        self.has_mine = False
        self.obscured = True
        self.marked = False
        self.count_adjacent_mines = 0

    def reset(self):
        self.has_mine = False
        self.obscured = True
        self.marked = False
        self.count_adjacent_mines = 0


class MineMatrix:
    def __init__(self):
        _w, _h = SCREEN_WIDTH, SCREEN_HEIGHT - HEADER_HEIGHT
        self.shape = (_w, _h)
        self.surface = pygame.surface.Surface(self.shape)

        maxtrix_shape = (_w // GRID_SIZE, _h // GRID_SIZE)
        self.matrix = [[Grid() for _ in range(maxtrix_shape[0])] for _ in range(maxtrix_shape[1])]
        self.matrix_shape = maxtrix_shape

        self.__init_mines()

    def __init_mines(self):
        matrix_shape_x, matrix_shape_y = self.matrix_shape

        random_mines = [True if i < COUNT_MINES else False for i in range(matrix_shape_x * matrix_shape_y)]
        random.shuffle(random_mines)

        for idx, has_mine in enumerate(random_mines):
            if has_mine:
                _x, _y = idx % matrix_shape_x, idx // matrix_shape_y
                self.matrix[_x][_y].has_mine = True
                for i in range(max(0, _x - 1), min(matrix_shape_x, _x + 2)):
                    for j in range(max(0, _y - 1), min(matrix_shape_y, _y + 2)):
                        self.matrix[i][j].count_adjacent_mines += 1

        self.surface.fill((230, 255, 255))

        for _x in range(matrix_shape_x):
            for _y in range(matrix_shape_y):
                grid = self.matrix[_x][_y]
                if grid.has_mine:
                    self.surface.blit(mine_image, (_x * GRID_SIZE, _y * GRID_SIZE))
                elif grid.count_adjacent_mines != 0:
                    text_count_mines = font_matrix.render(str(self.matrix[_x][_y].count_adjacent_mines), True,
                                                          (0, 0, 50))
                    u, v = text_count_mines.get_size()
                    self.surface.blit(text_count_mines, (_x * GRID_SIZE + GRID_SIZE / 2 - u / 2,
                                                         _y * GRID_SIZE + GRID_SIZE / 2 - v / 2 + 1))

        for coord_x in range(GRID_SIZE, self.shape[0], GRID_SIZE):
            pygame.draw.line(self.surface, (150, 200, 250), (coord_x, 0), (coord_x, SCREEN_HEIGHT), 2)
        for coord_y in range(GRID_SIZE, self.shape[1], GRID_SIZE):
            pygame.draw.line(self.surface, (150, 200, 250), (0, coord_y), (SCREEN_WIDTH, coord_y), 2)

    def reset(self):
        for gird_row in self.matrix:
            for grid in gird_row:
                grid.reset()
        self.__init_mines()

    def mark_grid(self, click_pos):
        _x = click_pos[0] // GRID_SIZE
        _y = (click_pos[1] - HEADER_HEIGHT) // GRID_SIZE
        if _y < 0:
            return

        clicked_grid = self.matrix[_x][_y]
        clicked_grid.marked = not clicked_grid.marked

    def click_button(self, click_pos):
        _x = click_pos[0] // GRID_SIZE
        _y = (click_pos[1] - HEADER_HEIGHT) // GRID_SIZE
        if _y < 0:
            return True

        clicked_grid = self.matrix[_x][_y]

        if not clicked_grid.obscured:
            return True

        if clicked_grid.has_mine:
            for gird_row in self.matrix:
                for grid in gird_row:
                    grid.obscured = False
            return False

        queue: list = [(_x, _y)]
        clicked_grid.obscured = False
        rear, front = 0, 1
        while front != rear:
            grid_x, grid_y = queue[rear]
            grid = self.matrix[grid_x][grid_y]
            rear += 1
            if grid.count_adjacent_mines == 0:
                for _x in range(max(0, grid_x - 1), min(self.matrix_shape[0], grid_x + 2)):
                    for _y in range(max(0, grid_y - 1), min(self.matrix_shape[1], grid_y + 2)):
                        adj_grid = self.matrix[_x][_y]
                        if adj_grid.obscured and not adj_grid.marked:
                            queue.append((_x, _y))
                            adj_grid.obscured = False
                            front += 1
        return True

    def update(self, _screen):
        _success = True
        _count_flags = 0
        sub_screen = _screen.subsurface((0, HEADER_HEIGHT, *self.shape))
        sub_screen.blit(self.surface, (0, 0))
        for _x in range(self.matrix_shape[0]):
            for _y in range(self.matrix_shape[1]):
                grid = self.matrix[_x][_y]
                if grid.obscured:
                    if grid.marked:
                        sub_screen.blit(flag_image, (_x * GRID_SIZE, _y * GRID_SIZE))
                        _count_flags += 1
                    else:
                        sub_screen.blit(button_image, (_x * GRID_SIZE, _y * GRID_SIZE))
                        _success = False
        return _success, _count_flags


class Header:
    def __init__(self):
        self.time_start = 0.

        self.surface = pygame.surface.Surface((SCREEN_WIDTH, HEADER_HEIGHT))
        self.surface.fill((50, 200, 255))
        pygame.draw.rect(self.surface, (200, 255, 255), (20, 10, 200, 80), 0)
        pygame.draw.rect(self.surface, (200, 255, 255), (400, 10, 100, 80), 0)

    def reset_time(self):
        self.time_start = time.time()

    def update(self, _screen, _game_over, _count_flags):
        time_now = time.time()
        time_second = int(time_now - self.time_start)

        text_time = font_header.render(f"{time_second // 60:02d}:{time_second % 60:02d}", True, (0, 100, 255))
        text_mines = font_header.render(str(COUNT_MINES - _count_flags), True, (0, 100, 255))

        _screen.blit(self.surface, (0, 0))
        _screen.blit(text_time, (35, 10))
        _screen.blit(text_mines, (410, 10))
        if _game_over:
            _screen.blit(replay_image, (270, 10))


def click_replay(pos):
    if 270 < pos[0] < 350 and 10 < pos[1] < 90:
        return True
    return False


game_over = False
clock = pygame.time.Clock()
header = Header()
mine_matrix = MineMatrix()
header.reset_time()

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                if event.button == 1:
                    if click_replay(event.pos):
                        game_over = False
                        count_flags = 0
                        header.reset_time()
                        mine_matrix.reset()
            elif event.button == 1:
                if not mine_matrix.click_button(event.pos):
                    game_over = True
            elif event.button == 3:
                mine_matrix.mark_grid(event.pos)

    game_over, count_flags = mine_matrix.update(screen)
    header.update(screen, game_over, count_flags)
    pygame.display.update()
