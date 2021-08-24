import pygame as pg

class Button:
    def __init__(self, pos_x, pos_y, len_x, len_y, title):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.len_x = len_x
        self.len_y = len_y
        self.title = title

    def draw(self, screen, col, size):
        pg.draw.rect(screen, col, (self.pos_x, self.pos_y, self.len_x, self.len_y), 2)
        font = pg.font.SysFont('verdana', size)
        img = font.render(self.title, True, col)
        img_rect = img.get_rect(center=(self.pos_x + self.len_x/2, self.pos_y + self.len_y/2))
        screen.blit(img, img_rect)
    