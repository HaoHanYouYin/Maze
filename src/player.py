import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, start_x, start_y):
        pg.sprite.Sprite.__init__(self)
        self.x = start_x
        self.y = start_y
        self.image = pg.image.load('../assets/Red_Block.png')

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def draw(self, screen, offset):
        L = self.image.get_width()
        screen.blit(self.image, (L * self.y + offset[0], L * self.x + offset[1]))