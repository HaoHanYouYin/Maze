import pygame as pg
from maze.init import init_maze
from player import *
from block import *

class Game:
    def __init__(self, width, height):
        # 迷宫默认的长和宽
        self.HEIGHT = height
        self.WIDTH = width

        # 方块的长
        self.BLOCK_SIZE = pg.image.load('../assets/Blue_Block.png').get_width()

        # 界面默认的长和宽
        self.SCREEN_HEIGHT = self.BLOCK_SIZE * height
        self.SCREEN_WIDTH = self.BLOCK_SIZE * width
        self.screen = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), pg.RESIZABLE)

        # 帧数
        self.FPS = 60
        self.clock = pg.time.Clock()

        # 程序
        self.running = True
        self.maze = init_maze(width, height, 'kruskal')
        self.player = Player(1, 1)

        # 终点坐标，传入迷宫长度
        self.ending_block = Ending_Block(height - 2, width - 2)

        # 初始偏移量
        self.offset = (self.SCREEN_WIDTH // 2 - self.BLOCK_SIZE * (self.WIDTH // 2),
                       self.SCREEN_HEIGHT // 2 - self.BLOCK_SIZE * (self.HEIGHT // 2))

    # 判断是否到达终点
    def is_to_ending(self):
        if self.player.x == self.ending_block.x and self.player.y == self.ending_block.y:
            return True
        else:
            return False

    # 胜利
    def win(self):
        print('你赢了！')
        pass

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
                self.win()
                break
            for event in pg.event.get():
                # 关闭
                if event.type == pg.QUIT:
                    self.running = False
                    break
                # 如果界面的大小改变
                elif event.type == pg.VIDEORESIZE:
                    self.screen = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

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
            # 填充背景颜色
            self.screen.fill((211, 211, 211))
            SCREEN_WIDTH, SCREEN_HEIGHT = self.screen.get_size()

            # 防止长和宽过小
            cur_screen_width, cur_screen_height = self.screen.get_size()
            if self.screen.get_width() < self.SCREEN_WIDTH:
                self.screen = pg.display.set_mode((self.SCREEN_WIDTH, cur_screen_height), pg.RESIZABLE)
            if self.screen.get_height() < self.SCREEN_HEIGHT:
                self.screen = pg.display.set_mode((cur_screen_width, self.SCREEN_HEIGHT), pg.RESIZABLE)

            # 设定偏移量，让迷宫永远处于中间
            self.offset = (SCREEN_WIDTH // 2 - self.SCREEN_WIDTH // 2,  SCREEN_HEIGHT // 2 - self.SCREEN_HEIGHT // 2)

            # 渲染每一个方块
            for block in blocks:
                block.draw(self.screen, self.offset)
            self.player.draw(self.screen, self.offset)
            self.ending_block.draw(self.screen, self.offset)
            pg.display.update()
        pg.quit()