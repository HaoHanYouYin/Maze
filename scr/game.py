import pygame as pg
from maze.init import *
from scr.player import Player


class game:
    def __init__(self):
        pass

# 设置长和宽（奇数）
width = 21
height = 11
block_length = pg.image.load('../assets/Blue_Block.png').get_width()
screen_width = block_length * width
screen_height = block_length * height

class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('../assets/Blue_Block.png')
        self.x = x
        self.y = y
    def draw(self, screen):
        screen.blit(self.image, (self.y * block_length, self.x * block_length))

def main():

    maze = init_maze(width, height, 'kruskal')

    blocks = []
    for i in range(height):
        for j in range(width):
            if maze[i][j] == 1:
                blocks.append(Block(i, j))

    pg.init()
    player = Player(1, 1)

    screen = pg.display.set_mode((screen_width, screen_height))
    pg.display.set_caption('迷宫')

    isRunning = True
    while isRunning:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                isRunning = False
                break
            if event.type == pg.KEYDOWN:
                x, y = player.x, player.y
                if event.key == pg.K_UP:
                    if maze[x - 1][y] == 0:
                        player.move(-1, 0)
                elif event.key == pg.K_DOWN:
                    if maze[x + 1][y] == 0:
                        player.move(1, 0)
                elif event.key == pg.K_LEFT:
                    if maze[x][y - 1] == 0:
                        player.move(0, -1)
                elif event.key == pg.K_RIGHT:
                    if maze[x][y + 1] == 0:
                        player.move(0, 1)

        screen.fill((211, 211, 211))

        for i in blocks:
            i.draw(screen)
        player.draw(screen)
        pg.display.update()

    pg.quit()