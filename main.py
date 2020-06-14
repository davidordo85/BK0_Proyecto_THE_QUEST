import pygame as pg
from pygame.locals import *
import sys

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)

class Nave:
    def __init__(self):
        self.vx = 5
        self.vy = 5
        self.x = 30
        self.y = 300
        self.h = 40
        self.w = 25
        self.centerx = self.x - self.w // 2

        self.image = pg.Surface((40, 25))
        self.image.fill(WHITE)



class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))
        self.pantalla.fill(BACKGROUND)
        espacio = pg.image.load("./resources/images/espacio.png")
        self.pantalla.blit(espacio, (0, 0))
        self.nave = Nave()
        


        pg.display.set_caption("THE QUEST")

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == QUIT:
                    game_over = True

            self.pantalla.blit(self.nave.image, (self.nave.x, self.nave.y))
            pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()

        
if __name__ == '__main__':
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()
    
