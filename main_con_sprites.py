import pygame as pg
from pygame.locals import *
from random import randint
import sys
from sprites import *

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))
        self.espacio = pg.image.load("./resources/images/fondo_espacio.png")

        pg.display.set_caption("THE QUEST")

    def handlenEvent(self):
        
        for event in pg.event.get():
            if event.type == QUIT:
                self.quit()        

    def main_loop(self):
        x = 0
        while True:
            self.handlenEvent()

            self.pantalla.blit(self.espacio, (x, 0))
            self.pantalla.blit(self.espacio, (x+2400, 0))

            pg.display.flip()

            x -= 10
            if x <= -2400:
                x = 0                
        

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()