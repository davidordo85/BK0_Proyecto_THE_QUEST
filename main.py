import pygame as pg
from pygame.locals import *
from random import randint
from sprites import *
import sys

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 0)

class Asteroid(pg.sprite.Sprite):
    vx = 0
    vy = 0
    num_sprites = 29

    def __init__(self):
        self.image = pg.Surface((40, 40), pg.SRCALPHA, 32)        
        self.rect = self.image.get_rect()
        self.images = self.loadImages()
        self.image_act = 0
        self.image.blit(self.images[self.image_act], [0, 0])

        self.destroy = pg.mixer.Sound('./resources/sounds/retro-explosion-07.wav')

    def loadImages(self):
        images = []
        for i in range(self.num_sprites):
            image = pg.image.load("./resources/sprites/asteroid/asteroid_{}.png".format(i))
            images.append(image)
        return images

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
        self.vx = 10
        if self.rect.centerx <= 0:
            self.rect.centerx = 3000
            self.rect.centery = randint (40, 560)

        self.rect.centerx -= self.vx
        #animar asteroide
        self.image_act += 1
        if self.image_act >= self.num_sprites:
            self.image_act = 0

        self.image.blit(self.images[self.image_act], (0, 0))
    '''
    def reset(self):
        self.rect.centerx = 770
        self.rect.centery = randint (30, 597) 
    '''
class Nave(pg.sprite.Sprite):
    vx = 0
    vy = 0
    num_sprites = 5
    
    def __init__(self):
        self.image = pg.Surface((65, 65), pg.SRCALPHA, 32)        
        self.rect = self.image.get_rect()
        self.images = self.loadImages()
        self.image_act = 4
        self.image.blit(self.images[self.image_act], [0, 0])

        self.rect.centerx = 40
        self.rect.centery = 300
        

    def loadImages(self):
        images = []
        for i in range(self.num_sprites):
            image = pg.image.load("./resources/sprites/nave/Spaceships__{}.png".format(i))
            images.append(image)
        return images

    def update(self, limSupY):
        self.rect.centerx += self.vx
        self.rect.centery += self.vy

        if self.rect.centery < self.rect.h // 2:
            self.rect.centery = self.rect.h // 2

        if self.rect.centery > limSupY - self.rect.h // 2:
            self.rect.centery = limSupY - self.rect.h // 2