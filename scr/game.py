import pygame as pg
from maze.init import init_maze
from scr.player import *
from scr.block import *


class Game:
    def __init__(self, width, height):
        self.HEIGHT = height
        self.WIDTH = width
        self.BLOCK_SIZE = pg.image.load('../assets/Blue_Block.png').get_width()
        self.SCREEN_HEIGHT = self.BLOCK_SIZE * height
        self.SCREEN_WIDTH = self.BLOCK_SIZE * width
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.FPS = 60
        self.clock = pg.time.Clock()
        self.running = True
        self.maze = init_maze(width, height, 'kruskal')
        self.player = Player(1, 1)
        self.ending_block = Ending_Block(height - 2, width - 2)

    def is_to_ending(self):
        if self.player.x == self.ending_block.x and self.player.y == self.ending_block.y:
            return True
        else:
            return False

    def run(self):
        blocks = []
        for block in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.maze[block][j] == 1:
                    blocks.append(Block(block, j))
        pg.init()
        while self.running:
            self.clock.tick(self.FPS)
            if self.is_to_ending():
                self.running = False
                break
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    break
                if event.type == pg.KEYDOWN:
                    x, y = self.player.x, self.player.y
                    if event.key == pg.K_UP:
                        if self.maze[x - 1][y] == 0:
                            self.player.move(-1, 0)
                    elif event.key == pg.K_DOWN:
                        if self.maze[x + 1][y] == 0:
                            self.player.move(1, 0)
                    elif event.key == pg.K_LEFT:
                        if self.maze[x][y - 1] == 0:
                            self.player.move(0, -1)
                    elif event.key == pg.K_RIGHT:
                        if self.maze[x][y + 1] == 0:
                            self.player.move(0, 1)
            self.screen.fill((211, 211, 211))
            for block in blocks:
                block.draw(self.screen)
            self.player.draw(self.screen)
            self.ending_block.draw(self.screen)
            pg.display.update()
        pg.quit()