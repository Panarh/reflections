from button import Button
import pygame as pg
import math
import numpy as np
from func import slope, meet, reflect
from start_screen import starting_screen



if __name__ == '__main__':
    #Colors:
    VIOLET = (150, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0 , 0)

    #Ellipse settings:
    big_axis = 600
    small_axis = 400

    #Ball start conditions:
    pos = np.array([300.0, 180.0])
    rad = 1
    v = np.array([0.6, 0.0])

    #Options: 1, 2 not implemented yet
    Show_trace = "Path"
    Tangent_lines = "Vector"
    Ellipse_col = RED
    Ball_col = VIOLET
    Butt_col = BLACK
    Tangent_col = BLACK
    
    
    #Logic
    pg.init()
    pg.display.set_caption("Beta-version-1.1")
    res = np.array([2*big_axis, 2*small_axis])
    screen = pg.display.set_mode(res)

    #System_variables
    start_clicked = False
    end_clicked = False
    pause_v = np.array([0, 0])
    screen.fill(WHITE)
    intersection_point = np.array([0.0, 0.0])

    #Phase_1:
    Menu = starting_screen(res, v, pos)
    (St, Set, Auth) = Menu.main_menu(screen)

    while not start_clicked:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                end_clicked = True
                start_clicked = True
                pg.quit()
            
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()

                if St.pos_x <= mouse[0] <= St.pos_x + St.len_x and St.pos_y <= mouse[1] <= St.pos_y + St.len_y:
                    start_clicked = True
                    screen.fill(WHITE)
                    pg.display.update()

                if Set.pos_x <= mouse[0] <= Set.pos_x + Set.len_x and Set.pos_y <= mouse[1] <= Set.pos_y + Set.len_y:
                    if (Menu.make_set(screen) == False):
                        end_clicked = True
                        start_clicked = True
                        pg.quit()
                    else:
                        pos = Menu.pos
                        v = Menu.v
                        print(v)
                        Menu.main_menu(screen)

                if Auth.pos_x <= mouse[0] <= Auth.pos_x + Auth.len_x and Auth.pos_y <= mouse[1] <= Auth.pos_y + Auth.len_y:
                    if (Menu.go_auth(screen) == False):
                        end_clicked = True
                        start_clicked = True
                        pg.quit()
           
    #Phase_2:
    
    if end_clicked == False:
        pg.draw.circle(screen, Ball_col, (pos[0], pos[1]), rad)
        pg.draw.ellipse(screen, Ellipse_col, (0, 0, 2*big_axis, 2*small_axis), 5)
        B = Button(50, 50, 130, 30, "pause/break")
        B.draw(screen, Butt_col, 20)

        while not end_clicked:
            if any(v != np.array([0.0, 0.0])):
                intersection_point = meet(v, pos, big_axis, small_axis)
            
                while (np.linalg.norm(pos + v - intersection_point) > np.linalg.norm(v)):
                    pg.draw.circle(screen, Ball_col, pos, rad)  
                    pos += v  
                
                pg.draw.circle(screen, Ball_col, pos, rad)
                pg.draw.circle(screen, Ball_col, intersection_point, rad)
                
                v = reflect(v, intersection_point, big_axis, small_axis)
                pos = intersection_point

                pos += v

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    end_clicked = True
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pos()
                    if 50 <= mouse[0] <= 50+130 and 50 <= mouse[1] <= 50+30:
                        if all(pause_v == np.array([0, 0])):
                            pause_v = v
                            v = np.array([0, 0])
                            Butt_col = RED
                            B.draw(screen, Butt_col, 20)
                        else:
                            v = pause_v
                            pause_v = np.array([0, 0])
                            Butt_col = BLACK
                            B.draw(screen, Butt_col, 20)                
            
            pg.display.update()
        pg.quit()