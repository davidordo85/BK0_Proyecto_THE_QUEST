import pygame as pg
from pygame.locals import *
from random import randint
import sys


WHITE = (255,255,255)
BLUE = (0,255,0)
BLACK = (0, 0, 0)
WIN_SCORE_GAME = 1000

class Movil:
    vx = 0
    vy = 0
    __color = WHITE
    def __init__(self, w, h, centerx=0, centery=0): # inicia con las funciones que usan los objetos móviles
        self.w = w
        self.h = h
        self.Cx = centerx
        self.Cy = centery

        self.image = pg.Surface((self.w, self.h))
        self.image.fill(self.__color)

    @property
    def posx(self):
        return self.Cx - self.w // 2
    @property
    def posy(self):
        return self.Cy - self.h // 2

    
    @property
    def color(self):
        return self.__color

    @color.setter #función cambia color
    def color(self, tupla_color):
        self.__color = tupla_color
        self.image.fill(self.__color)
    
    def move(self, limSupX, limSupY):
        pass


class Nave(Movil):
    def __init__(self):
        #Movil.__init__(self, 60, 25, 30, 300) #Llamo a clase madre movil, con su metodo init 
        super().__init__(60, 25, 30, 300) #estas dos clases hacen lo mismo        
        self.color = BLUE
        self.image = pg.image.load('./resources/images/Rocket11_poquet.png')
        self.destroy = pg.mixer.Sound('./resources/sounds/retro-explosion-07.wav')
    
    def move(self, limSupX, limSupY):
        self.Cx += self.vx
        self.Cy += self.vy

        if self.Cy < self.h // 2:
            self.Cy = self.h // 2

        if self.Cy > limSupY - self.h // 2:
            self.Cy = limSupY - self.h // 2

    def estrellado(self, something):
        dx = abs(self.Cx - something.Cx)
        dy = abs(self.Cy - something.Cy)        

        if dx < (self.w + something.w )//2 and dy < (self.h + something.h) // 2:
            # quitar vida
            self.destroy.play()            
        else:
            #print("No estrellado") # game_over False
            pass

class Asteroid(Movil):
    def __init__(self):
        super().__init__(40, 36, 770, 300)
        self.image = pg.image.load("./resources/images/asteroide.png")
        

    def move(self, limSupX, limSupY):
        self.vx = 5
        if self.Cx <= 0:
            self.Cx = 770
            self.Cy = randint (30, 597)

        self.Cx -= self.vx