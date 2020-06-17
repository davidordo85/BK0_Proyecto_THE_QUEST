import pygame as pg
from pygame.locals import *
from random import randint
import sys

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)

class Nave:
    def __init__(self):
        self.vx = 5
        self.vy = 5
        self.Cx = 30
        self.Cy = 300
        self.h = 42
        self.w = 45
    
        self.image = pg.image.load("./resources/images/mini_nave.png")
        #self.image.fill()    
    
    @property
    def posx(self):
        return self.Cx - self.w // 2
    @property
    def posy(self):
        return self.Cy - self.h // 2


    def move(self, limSupY):
        if self.Cy < self.h //2:
            self.Cy = self.h // 2

        if self.Cy > limSupY - self.h // 2:
            self.Cy = limSupY - self.h // 2      

class Asteroid:
    def __init__(self):

        self.vx = 3
        self.vy = 0
        self.Cx = 770
        self.Cy = randint (30, 597)       
        self.w = 30
        self.h = 30

        self.image = pg.image.load("./resources/images/asteroide.png")
        #self.image.fill(WHITE)

    @property
    def posx(self):
        return self.Cx - self.w // 2
    @property
    def posy(self):
        return self.Cy - self.h // 2

    
    


class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))
        self.pantalla.fill(BACKGROUND)
        self.espacio = pg.image.load("./resources/images/espacio.png")

        self.nave = Nave()
        self.asteroid = Asteroid()

        pg.display.set_caption("THE QUEST")

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == QUIT:
                    game_over = True

                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.nave.Cy -= self.nave.vy
                        
                    if event.key == K_DOWN:
                        self.nave.Cy += self.nave.vy
            key_pressed = pg.key.get_pressed()
            if key_pressed[K_UP]:
                self.nave.Cy -= self.nave.vy
            if key_pressed[K_DOWN]:
                self.nave.Cy += self.nave.vy

            self.pantalla.blit(self.espacio, (0, 0))
            self.pantalla.blit(self.nave.image, (self.nave.posx, self.nave.posy))
            self.pantalla.blit(self.asteroid.image, (self.asteroid.posx, self.asteroid.posy))
            self.asteroid.Cx -= self.asteroid.vx

            
            self.nave.move(600)            
            pg.display.flip()
            

    def quit(self):
        pg.quit()
        sys.exit()

        
if __name__ == '__main__':
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()
    
