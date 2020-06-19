import pygame as pg
from pygame.locals import *
from random import randint
import sys

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)

class Nave:
    def __init__(self):
        self.vx = 0
        self.vy = 0
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


    def move(self, limSupX, limSupY):
        self.Cx += self.vx
        self.Cy += self.vy

        if self.Cy < self.h //2:
            self.Cy = self.h // 2

        if self.Cy > limSupY - self.h // 2:
            self.Cy = limSupY - self.h // 2

    def estrellado(self, something):
        dx = abs(self.Cx - something.Cx)
        dy = abs(self.Cy - something.Cy)

        if dx < (self.w + something.w )//2 and dy < (self.h + something.h) // 2:
            print("Estrellado") # quitar vida
        else:
            print("No estrellado") # game_over False


class Asteroid:
    def __init__(self):

        self.vx = randint (3, 5)
        self.vy = 0
        self.Cx = 770
        self.Cy = randint (30, 597)       
        self.w = randint (30, 100) 
        self.h = randint (30, 100)


        self.image = pg.image.load("./resources/images/asteroide.png")
        #self.image.fill(WHITE)

    @property
    def posx(self):
        return self.Cx - self.w // 2
    @property
    def posy(self):
        return self.Cy - self.h // 2

    def move(self, limInfX, limSupX):
        if self.Cx <= limInfX:
            self.Cx = limSupX
            self.Cy = randint (30, 597)

        self.Cx -= self.vx

class Game:
    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))
        self.pantalla.fill(BACKGROUND)
        self.espacio = pg.image.load("./resources/images/espacio.png")

        self.nave = Nave()
        self.asteroid1 = Asteroid()
        

        pg.display.set_caption("THE QUEST")

    def main_loop(self):
        game_over = False

        while not game_over:
            for event in pg.event.get():
                if event.type == QUIT:
                    game_over = True                
                '''
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.nave.vy  = -5                        
                        
                    if event.key == K_DOWN:
                        self.nave.vy  = 5
                        '''

            key_pressed = pg.key.get_pressed()
            if key_pressed[K_UP]:
                self.nave.vy = -5
                
            elif key_pressed[K_DOWN]:
                self.nave.vy = 5
            else:
                self.nave.vy = 0
                


            self.pantalla.blit(self.espacio, (0, 0))
            self.pantalla.blit(self.nave.image, (self.nave.posx, self.nave.posy))
            self.pantalla.blit(self.asteroid1.image, (self.asteroid1.posx, self.asteroid1.posy))
            

            
            self.nave.move(800, 600)
            self.asteroid1.move(0, 800)
            self.nave.estrellado(self.asteroid1)            

            pg.display.flip()
            

    def quit(self):
        pg.quit()
        sys.exit()

        
if __name__ == '__main__':
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()