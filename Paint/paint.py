import pygame as pg
from collections import deque
from config import Config


class Paint(Config):
    colors = {'prt' : (0,0,0),"vermelho_claro" : (235, 64, 52),"vermelho_escuro" : (158, 41, 33),"laranja" : (235, 111, 40),"marrom" : (138, 71, 33),"amarelo_laranja" : (255, 175, 3),'amarelo' : (250, 231, 20),'marca_texto' : (219, 242, 10),'verde_limao' : (165, 242, 10),
'chroma_key' : (76, 242, 10),'verde' : (45, 204, 24),'verde_escuro' : (31, 135, 18),'verde_azulado' : (23, 232, 138),'azul_esverdeado' : (17, 240, 188),'azul_claro' : (17, 240, 221),'azul_claro2' : (17, 225, 240),'azul_ceu' : (12, 185, 237),
'azul_escuro' : (9, 126, 189),'azul_forte' : (11, 55, 214),'roxo' : (139, 7, 247),'violeta' : (174, 7, 245),'rosa' : (208, 7, 222),'rosa_choque' : (245, 5, 185)}
    
    def __init__(self) -> None:
        self.color = (0,0,0)
        super().__init__()

    def run(self):
        print('Code is running!')
        
        self.render_colors()
        self.drawing = False
        self.drawing_size = self.w / 100
        while True:
            for event in pg.event.get():
                self.page_config(event, self.render_colors)
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.drawing = True
                    pos = pg.mouse.get_pos()
                    self.set_color(pos)
                    self.paint_utils(pos)

                if event.type == pg.MOUSEBUTTONUP:
                    self.drawing = False

                if event.type == pg.MOUSEMOTION and self.drawing:
                    pos = pg.mouse.get_pos()
                    if pos[0] - self.drawing_size < self.wh/2 or pos[0] + self.drawing_size > self.w - (self.wh/2):
                        self.render_colors()
                        self.screen.blit(self.menu, (0,0))
                        pg.display.flip()

                    circle = pg.draw.circle(self.screen,self.color,pos,int(self.drawing_size))
                    pg.display.update(circle)

    def set_color(self, pos):
        for i, color_pos in enumerate(self.color_coordinates):
            if pos[0] < color_pos[0] and pos[1] < color_pos[1]:
                self.color = self.colors[list(self.colors)[i]]
                self.drawing_size = self.w / 100
                break                    

    def render_colors(self):
        self.wh = self.w-self.h
        tx = self.h/3
        tx2 = tx/3
        wh = self.wh
        self.tx = tx
        self.color_positions =  [[0,tx/3,wh/6,tx/3],[wh/6,tx/3,wh/6,tx/3],[wh/3,tx/3,wh/6,tx/3],[0,tx/3*2,wh/6,tx/3],[wh/6,tx/3*2,wh/6,tx/3],[wh/3,tx/3*2,wh/6,tx/3],[0,tx,wh/6,tx/3],[wh/6,tx,wh/6,tx/3],[wh/3,tx,wh/6,tx/3],[0,tx+tx2,wh/6,tx/3],[wh/6,tx+tx2,wh/6,tx/3],[wh/3,tx+tx2,wh/6,tx/3],
                                [0,tx+tx2*2,wh/6,tx/3],[wh/6,tx+tx2*2,wh/6,tx/3],[wh/3,tx+tx2*2,wh/6,tx/3],[0,tx*2,wh/6,tx/3],[wh/6,tx*2,wh/6,tx/3],[wh/3,tx*2,wh/6,tx/3],[0,tx*2+tx2,wh/6,tx/3],[wh/6,tx*2+tx2,wh/6,tx/3],[wh/3,tx*2+tx2,wh/6,tx/3],[0,tx*2+tx2*2,wh/6,tx/3],[wh/6,tx*2+tx2*2,wh/6,tx/3]]
        self.color_coordinates = [[wh/6,tx2*2],[wh/3,tx2*2],[wh/2,tx2*2],[wh/6,tx],[wh/3,tx],[wh/2,tx],[wh/6,tx+tx2],[wh/3,tx+tx2],[wh/2,tx+tx2],[wh/6,tx+tx2*2],[wh/3,tx+tx2*2],[wh/2,tx+tx2*2],[wh/6,tx*2],[wh/3,tx*2],[wh/2,tx*2],[wh/6,tx*2+tx2],[wh/3,tx*2+tx2],[wh/2,tx*2+tx2],
[wh/6,tx*2+tx2*2],[wh/3,tx*2+tx2*2],[wh/2,tx*2+tx2*2],[wh/6,self.h],[wh/3,self.h]]
        
        for color, position in zip(self.colors.values(), self.color_positions):
            pg.draw.rect(self.screen,color,pg.Rect(position))
        
        pg.display.flip()

    def paint_utils(self, pos: tuple):
        if pos[0] > self.w - (self.wh/2):
            if pos[1] < self.tx/2:
                self.erase()
            elif pos[1] < self.tx: 
                self.adjust_size(self.w/150)
            elif pos[1] < self.tx + self.tx/2:
                self.adjust_size(-self.w/150)
            elif pos[1] < self.tx*2:
                self.color_selector()
            elif pos[1] < self.tx*2 + self.tx/2:
                self.color_cleaner()
            else:
                self.paint_bucket()

    def erase(self):
        self.color = (255,255,255)
        self.drawing_size = self.w / 20

    def adjust_size(self, size_value):
        if size_value < 0 and (self.drawing_size + size_value) < 0:
            return
        self.drawing_size += size_value

    def color_selector(self):
        not_selected = True
        while not_selected:
            for event_selected in pg.event.get():
                if event_selected.type == pg.MOUSEBUTTONDOWN:
                    pos_selected = pg.mouse.get_pos()
                    self.color = self.screen.get_at(pos_selected)
                    not_selected = not not_selected

    def color_cleaner(self):
        not_selected = True
        while not_selected:
            for event_selected in pg.event.get():
                if event_selected.type == pg.MOUSEBUTTONDOWN:
                    pos_selected = pg.mouse.get_pos()
                    color = self.screen.get_at(pos_selected)
                    pg.PixelArray(self.screen).surface.lock()

                    for pos_w in range(self.w):
                        for pos_h in range(self.h):
                            if pos_w > self.wh / 2:
                                if self.screen.get_at((pos_w, pos_h)) == color:
                                    self.screen.set_at((pos_w, pos_h), (255, 255, 255))

                    pg.PixelArray(self.screen).surface.unlock()
                    pg.display.flip()
                    not_selected = not not_selected

    def paint_bucket(self):
        not_selected = True
        while not_selected:
            for event_selected in pg.event.get():
                if event_selected.type == pg.MOUSEBUTTONDOWN:
                    pos_selected = pg.mouse.get_pos()
                    target_color = self.screen.get_at(pos_selected)[:3]
                    fill_color = self.color

                    if target_color == fill_color:
                        return

                    queue = deque([pos_selected])
                    visited = set([pos_selected])

                    while queue:
                        '''Will be running until there is no items left, as a result of the popleft method executed in the beggining 
                        and since it only appends on this queue when the coordinates aren't on the set, it will eventually break the loop''' 
                        x, y = queue.popleft()
                        self.screen.set_at((x, y), fill_color)

                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.w and 0 <= ny < self.h:
                                if (nx, ny) not in visited and self.screen.get_at((nx, ny))[:3] == target_color:
                                    queue.append((nx, ny))
                                    visited.add((nx, ny))

                    pg.display.update()
                    not_selected = not not_selected


if __name__ == '__main__':
    game = Paint()
    game.run()