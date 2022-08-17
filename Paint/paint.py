import pygame as pg
from pygame.locals import *
pg.init()
tc = True
w, h = pg.display.Info().current_w, (pg.display.Info().current_h)
wh = w-h
tamanho = w,h
tx = h/3
tx2 = tx/3
tela = pg.display.set_mode(tamanho,RESIZABLE)
lista = [[(w-h)/2,0,tx,tx],[(w-h)/2+tx,0,tx,tx],[(w-h)/2+tx*2,0,tx,tx],[(w-h)/2,tx,tx,tx],[(w-h)/2+tx,tx,tx,tx],[(w-h)/2+tx*2,tx,tx,tx],[(w-h)/2,tx*2,tx,tx],[(w-h)/2+tx,tx*2,tx,tx],[(w-h)/2+tx*2,tx*2,tx,tx]]
tabuleiro = [[0,0,tx/3,tx/3],[0,h/8,tx/3,tx/3],[0,(h/8)*2,tx/3,tx/3],[0,(h/8)*3,tx/3,tx/3],[0,(h/8)*4,tx/3,tx/3],[0,(h/8)*5,tx/3,tx/3],[0,(h/8)*6,tx/3,tx/3],[0,(h/8)*7,tx/3,tx/3],[(h/8),(h/8)*7,tx/3,tx/3],[(h/8)*2,(h/8)*7,tx/3,tx/3],[(h/8)*2,(h/8)*6,tx/3,tx/3],[(h/8)*2,(h/8)*5,tx/3,tx/3],[(h/8)*2,(h/8)*4,tx/3,tx/3],[(h/8)*2,(h/8)*3,tx/3,tx/3],[(h/8)*2,(h/8)*2,tx/3,tx/3],[(h/8)*2,(h/8),tx/3,tx/3],[(h/8)*2,0,tx/3,tx/3],[(h/8)*3,0,tx/3,tx/3],[(h/8)*4,0,tx/3,tx/3],[(h/8)*5,0,tx/2,tx/2]]
class paint():
    preto = True
    def config(self,cor):
        global tc, tela
        if self.event.type == pg.KEYDOWN:
            if self.event.key == pg.K_F11:
                if tc == True:
                    tela = pg.display.set_mode(tamanho,FULLSCREEN)
                    tc = False
                    menu = pg.transform.scale(pg.image.load('paint.png'),(w,h))
                    tela.blit(menu,(0,0))
                    pg.draw.rect(tela,(cor),pg.Rect((w-h)/2,0,h,h))
                else:
                    tela = pg.display.set_mode(tamanho)
                    tc = True
                    menu = pg.transform.scale(pg.image.load('paint.png'),(w,h))
                    tela.blit(menu,(0,0))
                    pg.draw.rect(tela,(cor),pg.Rect((w-h)/2,0,h,h))
        if self.event.type == pg.QUIT:
            pg.quit()
            exit()
    desenho = 0
    pos_tabela = [[0,tx/3,wh/6,tx/3],[wh/6,tx/3,wh/6,tx/3],[wh/3,tx/3,wh/6,tx/3],[0,tx/3*2,wh/6,tx/3],[wh/6,tx/3*2,wh/6,tx/3],[wh/3,tx/3*2,wh/6,tx/3],[0,tx,wh/6,tx/3],[wh/6,tx,wh/6,tx/3],[wh/3,tx,wh/6,tx/3],[0,tx+tx2,wh/6,tx/3],[wh/6,tx+tx2,wh/6,tx/3],[wh/3,tx+tx2,wh/6,tx/3],
[0,tx+tx2*2,wh/6,tx/3],[wh/6,tx+tx2*2,wh/6,tx/3],[wh/3,tx+tx2*2,wh/6,tx/3],[0,tx*2,wh/6,tx/3],[wh/6,tx*2,wh/6,tx/3],[wh/3,tx*2,wh/6,tx/3],[0,tx*2+tx2,wh/6,tx/3],[wh/6,tx*2+tx2,wh/6,tx/3],[wh/3,tx*2+tx2,wh/6,tx/3],[0,tx*2+tx2*2,wh/6,tx/3],[wh/6,tx*2+tx2*2,wh/6,tx/3]]
    cor_pos = [[wh/6,tx2*2],[wh/3,tx2*2],[wh/2,tx2*2],[wh/6,tx],[wh/3,tx],[wh/2,tx],[wh/6,tx+tx2],[wh/3,tx+tx2],[wh/2,tx+tx2],[wh/6,tx+tx2*2],[wh/3,tx+tx2*2],[wh/2,tx+tx2*2],[wh/6,tx*2],[wh/3,tx*2],[wh/2,tx*2],[wh/6,tx*2+tx2],[wh/3,tx*2+tx2],[wh/2,tx*2+tx2],
[wh/6,tx*2+tx2*2],[wh/3,tx*2+tx2*2],[wh/2,tx*2+tx2*2],[wh/6,h],[wh/3,h]]
    cor_tabela = {'prt' : (0,0,0),"vermelho_claro" : (235, 64, 52),"vermelho_escuro" : (158, 41, 33),"laranja" : (235, 111, 40),"marrom" : (138, 71, 33),"amarelo_laranja" : (255, 175, 3),'amarelo' : (250, 231, 20),'marca_texto' : (219, 242, 10),'verde_limao' : (165, 242, 10),
'chroma_key' : (76, 242, 10),'verde' : (45, 204, 24),'verde_escuro' : (31, 135, 18),'verde_azulado' : (23, 232, 138),'azul_esverdeado' : (17, 240, 188),'azul_claro' : (17, 240, 221),'azul_claro2' : (17, 225, 240),'azul_ceu' : (12, 185, 237),
'azul_escuro' : (9, 126, 189),'azul_forte' : (11, 55, 214),'roxo' : (139, 7, 247),'violeta' : (174, 7, 245),'rosa' : (208, 7, 222),'rosa_choque' : (245, 5, 185)}
    cortabela = list(cor_tabela)
    prt = (0,0,0)
    branco = (255,255,255)
    cor = (0,0,0)
    def __init__(self):
        pg.draw.rect(tela,(255,255,255),pg.Rect((w-h)/2,0,h,h))
        desenho_tamanho = w/200
        menu2 = pg.transform.scale(pg.image.load('paint.png'),(w,h))
        tela.blit(menu2,(0,0))
        pos_desenho = []
        pos1_desenho = []
        while self.desenho == 0:
            for i in range(len(self.cor_tabela)):
                pg.draw.rect(tela,self.cor_tabela[self.cortabela[i]],pg.Rect(self.pos_tabela[i]))
            preto = True
            for self.event in pg.event.get():
                self.config((255,255,255))
                if self.event.type == pg.KEYDOWN:
                    if self.event.key == pg.K_ESCAPE:
                        self.desenho = 1
                if self.event.type == pg.MOUSEBUTTONUP:
                    pos = pg.mouse.get_pos()
                    for i in range(len(self.cor_pos)):
                        if pos[0] < wh/2 and pos[1] < tx2:
                            tela.blit(menu2,(0,0))
                            break
                        if pos[0] < self.cor_pos[i][0] and pos[1] < self.cor_pos[i][1]:
                            tela.blit(menu2,(0,0))
                            self.cor = self.cor_tabela[self.cortabela[i]]
                            desenho_tamanho = w/200
                            break
                    if pos[0] > ((w-h)/2) + h and pos[1] < tx/2:
                        tela.blit(menu2,(0,0))
                        self.cor = self.branco
                        desenho_tamanho = w/20
                    elif pos[0] > ((w-h)/2) + h and pos[1] < tx:
                        tela.blit(menu2,(0,0))
                        desenho_tamanho += w/150
                    elif pos[0] > ((w-h)/2) + h and pos[1] < tx + tx/2:
                        if not (desenho_tamanho - w/150) < 0:
                            tela.blit(menu2,(0,0))
                            desenho_tamanho -= w/150
                    elif pos[0] > ((w-h)/2) + h and pos[1] < tx*2:
                        tela.blit(menu2,(0,0))
                        pg.display.update()
                        gotas = 0
                        while gotas == 0:
                            for event in pg.event.get():
                                if event.type == pg.MOUSEBUTTONUP:
                                    pos = pg.mouse.get_pos()
                                    self.cor = tela.get_at(pos)
                                    gotas = 1
                    elif pos[0] > ((w-h)/2) + h and pos[1] < tx*2 + tx/2:
                        tela.blit(menu2,(0,0))
                        pg.display.update()
                        gotas = 0
                        while gotas == 0:
                            for event in pg.event.get():
                                if event.type == pg.MOUSEBUTTONUP:
                                    pos = pg.mouse.get_pos()
                                    cor2 = tela.get_at(pos)
                                    for i in range(w):
                                        for i2 in range(h):
                                            if tela.get_at((i,i2)) == cor2:
                                                pg.draw.rect(tela,self.branco,pg.Rect(i,i2,1,1))
                                    gotas = 1
                    elif pos[0] > ((w-h)/2) + h and pos[1] < h:
                        tela.blit(menu2,(0,0))
                        pg.display.update()
                        gotas = 0
                        while gotas == 0:
                            pintar2 = []
                            for event in pg.event.get():
                                if event.type == pg.MOUSEBUTTONUP:
                                    pos = pg.mouse.get_pos()
                                    for a in range(20):
                                        for i in range(h):
                                            pintar = []
                                            pos_inicial = (0,0)
                                            saas = 0
                                            for i2 in range(int(wh/2),int(wh/2+h)):
                                                if tela.get_at((i2,i)) == self.prt:
                                                    if i2 > pos_inicial[0]+10:
                                                        if saas == 2:
                                                            pint = list(set(pintar))
                                                            for i3 in range(len(pint)): 
                                                                pg.draw.rect(tela,self.cor,pg.Rect(pint[i3][0],pint[i3][1],2,2))
                                                                pg.display.update() 
                                                            saas = 0
                                                    pos_inicial = (i2,i)
                                                    saas = 1
                                                if saas == 1:
                                                    if tela.get_at((i2,i)) == self.branco:
                                                        pintar.append((i2,i))
                                                        saas = 2
                                            gotas = 1
                if pg.mouse.get_pressed()[0]:
                    pos = pg.mouse.get_pos()
                    pg.draw.circle(tela,self.cor,pos,int(desenho_tamanho))
                    if pos[0] - desenho_tamanho < wh/2:
                        tela.blit(menu2,(0,0))
                    if pos is not pos_desenho:
                        pos_desenho.append(pos[0])
                        pos1_desenho.append([pos[1]])
            pg.display.update()
paint()