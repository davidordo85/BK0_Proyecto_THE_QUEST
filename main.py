import pygame as pg
from pygame.locals import *
from random import randint
from sprites import *
import sys

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 0)
WIN_SCORE_GAME = 100

class Asteroid(pg.sprite.Sprite):
    vx = 0
    vy = 0
    __color= WHITE

    def __init__(self):
        self.image = pg.Surface((40, 40))
        self.image.fill(self.__color)
        self.destroy = pg.mixer.Sound('./resources/sounds/retro-explosion-07.wav')
        self.rect = self.image.get_rect()


    @property
    def color(self):
        return self.__color

    @color.setter #función cambia color
    def color(self, tupla_color):
        self.__color = tupla_color
        self.image.fill(self.__color)

    def estrellado(self, something):
        dx = abs(self.rect.centerx - something.rect.centerx)
        dy = abs(self.rect.centery - something.rect.centery)        

        if dx < (self.rect.w + something.rect.w )//2 and dy < (self.rect.h + something.rect.h) // 2:
            # quitar vida
            self.destroy.play()   
        else:
            #print("No estrellado") # game_over False
            pass

    def update(self, limSupX, limSupY):
        self.vx = 5
        if self.rect.centerx <= 0:
            self.rect.centerx = 770
            self.rect.centery = randint (30, 597)

        self.rect.centerx -= self.vx

    def reset(self):
        self.rect.centerx = 770
        self.rect.centery = randint (30, 597) 

class Nave(pg.sprite.Sprite):
    vx = 0
    vy = 0
    __color = BLUE
    
    def __init__(self):
        self.image = pg.Surface((65, 25))
        self.image.fill(self.__color)
        self.rect = self.image.get_rect()        
        self.rect.centerx = 30
        self.rect.centery = 300

    @property
    def color(self):
        return self.__color

    @color.setter #función cambia color
    def color(self, tupla_color):
        self.__color = tupla_color
        self.image.fill(self.__color)

    def update(self, limSupY):
        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        if self.rect.centery < self.rect.h // 2:
            self.rect.centery = self.rect.h // 2

        if self.rect.centery > limSupY - self.rect.h // 2:
            self.rect.centery = limSupY - self.rect.h // 2

        
