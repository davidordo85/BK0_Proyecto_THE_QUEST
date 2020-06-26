import pygame as pg
from pygame.locals import *
from random import randint
import sys

MULTICOLOR = (0, 0, 255)
WHITE = (255, 255, 255)
BLUE = (0, 255, 0)
#TEXTITO = ('''LA BUSQUEDA COMIENZA EN UN PLANETA TIERRA MORIBUNDO  POR EL CAMBIO CLIMÁTICO. PARTIREMOS A LA BUSQUEDA DE UN PLANETA COMPATIBLE CON LA VIDA HUMANA PARA COLONIZARLO''')


class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))
        self.espacial = pg.image.load("./resources/images/imagen-del-espacio.png")

        self.font = pg.font.Font('./resources/fonts/OdibeeSans-Regular.ttf', 30)

        self.text_inicial = self.font.render("LA BUSQUEDA COMIENZA EN UN PLANETA TIERRA ", False, WHITE)
        self.text_inicial1 = self.font.render("MORIBUNDO POR EL CAMBIO CLIMÁTICO.", False, WHITE)
        self.text_inicial2 = self.font.render("PARTIREMOS A LA BUSQUEDA DE UN PLANETA", False, WHITE)
        self.text_inicial3 = self.font.render("COMPATIBLE CON LA VIDA HUMANA PARA COLONIZARLO.", False, WHITE)
        pg.display.set_caption("THE QUEST")

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == QUIT:
                    game_over = True
                    
                

            self.pantalla.blit(self.espacial, (0,0))
            self.pantalla.blit(self.text_inicial, (30, 30))
            self.pantalla.blit(self.text_inicial1, (30, 80))
            self.pantalla.blit(self.text_inicial2, (30, 130))
            self.pantalla.blit(self.text_inicial3, (30, 180))
            pg.display.flip()

    def bucle_partida(self):
        game_over = False
    
        
        

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()