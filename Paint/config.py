import pygame as pg
from pygame.event import Event
from pygame.locals import RESIZABLE, FULLSCREEN
from typing import Callable

class Config():
    def __init__(self) -> None:
        pg.init()
        self.fullscreen = False
        self.screen_info = pg.display.Info()
        self.w, self.h = int(self.screen_info.current_w * 0.9), int(self.screen_info.current_h * 0.9)
        self.render_image((255,255,255), RESIZABLE)
    
    def render_image(self, color: tuple, flags: int):
        self.size = self.w, self.h
        self.screen = pg.display.set_mode(self.size, flags)
        self.menu = pg.transform.scale(pg.image.load('paint.png'), self.size)
        self.screen.blit(self.menu, (0,0))
        pg.draw.rect(self.screen, color, pg.Rect((self.size[0] - self.size[1]) / 2, 0, self.size[1], self.size[1]))

    def page_config(self, event: Event, rendering: Callable, color: tuple = (255,255,255)):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_F11:
                self.fullscreen = not self.fullscreen
                if self.fullscreen:
                    self.w, self.h = self.screen_info.current_w, self.screen_info.current_h
                    self.render_image(color, FULLSCREEN)
                else:
                    self.w, self.h = int(self.screen_info.current_w * 0.9), int(self.screen_info.current_h * 0.9)
                    self.render_image(color, RESIZABLE)
                rendering()   
            elif event.key == pg.K_ESCAPE:
                print('Code stopped!')
                pg.quit()
                exit()

        if event.type == pg.QUIT:
            print('Code stopped!')
            pg.quit()
            exit()