import pygame as pg

# 普通方格
class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('../assets/Blue_Block.png')
        self.x = x
        self.y = y
        self.BLOCK_SIZE = self.image.get_width()
    def draw(self, screen, offset):
        screen.blit(self.image, (self.y * self.BLOCK_SIZE + offset[0], self.x * self.BLOCK_SIZE + offset[1]))

# 终点
class Ending_Block(Block):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pg.image.load('../assets/Ending_Block.png')