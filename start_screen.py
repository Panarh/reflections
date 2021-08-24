from button import Button
import pygame as pg
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

def is_in_ellipse(pos, big_axis, small_axis):
    if (((pos[0] - big_axis)/big_axis)**2 + ((pos[1] - small_axis)/small_axis)**2 < 1):
        return True
    else:
        return False

class starting_screen:
    def __init__(self, res, v, pos):
        self.res = res
        self.v = v
        self.pos = pos

    def main_menu(self, screen):
        screen.fill(WHITE)

        start = Button(self.res[0]/2 - 120, self.res[1]/2 - self.res[1]/3, 240, 100, "START")
        start.draw(screen, BLACK, 70)

        settings = Button(self.res[0]/2 - 200, self.res[1]/2 - self.res[1]/3 + 160, 400, 100, "SETTINGS")
        settings.draw(screen, BLACK, 70)

        about = Button(self.res[0]/2 - 130, self.res[1]/2 - self.res[1]/3 + 320, 260, 100, "ABOUT")
        about.draw(screen, BLACK, 70)

        pg.display.update()

        return (start, settings, about)

    def go_auth(self, screen):
        screen.fill(WHITE)

        authors = Button(self.res[0]/2 - 300, self.res[1]/2 - self.res[1]/3 + 160, 600, 100, "Биллиард")
        authors.draw(screen, BLACK, 70)

        back = Button(self.res[0]/2 - 300, self.res[1]/2 - self.res[1]/3 + 320, 600, 100, "BACK")
        back.draw(screen, BLACK, 70)

        pg.display.update()
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    return False

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()

                    if back.pos_x <= mouse[0] <= back.pos_x + back.len_x and back.pos_y <= mouse[1] <= back.pos_y + back.len_y:
                        self.main_menu(screen)
                        running = True
                        return True


    def set_pos(self, screen, mouse):
        if is_in_ellipse(mouse, self.res[0]/2, self.res[1]/2):
            self.pos = np.array([mouse[0], mouse[1]], dtype=float)
            pg.draw.circle(screen, RED, self.pos, 4)
            pg.display.update()
            return True
        return False

            
    def set_v(self, screen, mouse):
        if ((self.pos[0] - mouse[0]) == 0 and (self.pos[1] - mouse[1]) == 0):
            return False

        else:
            velocity = np.array([mouse[0] - self.pos[0], mouse[1] - self.pos[1]], dtype=float)
            pg.draw.line(screen, BLACK, self.pos, mouse, 3)
            norm = np.linalg.norm(velocity)
            self.v = velocity / norm
            pg.display.update()
            return True
        
        

    def make_set(self, screen):
        screen.fill(WHITE)
        pg.draw.ellipse(screen, BLACK, (0, 0, self.res[0], self.res[1]), 5)
        pg.display.update()
        setting = True

        while setting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    setting = False
                    return False

                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()

                    if (self.set_pos(screen, mouse) == True):
                        while setting:
                            for event in pg.event.get():
                                if event.type == pg.QUIT:
                                    setting = False
                                    return False

                                if event.type == pg.MOUSEBUTTONDOWN:
                                    mouse = pg.mouse.get_pos()
                                    if (self.set_v(screen, mouse) == True):
                                        pg.display.update()
                                        setting = False

        back = Button(10, 10, 200, 70, "BACK")
        back.draw(screen, BLACK, 70)
        pg.display.update()

        waiting = True

        while waiting:
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    waiting = False
                    return False
                           
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    if back.pos_x <= mouse[0] <= back.pos_x + back.len_x and back.pos_y <= mouse[1] <= back.pos_y + back.len_y:
                        self.main_menu(screen)
                        waiting = False
                        return True

        


