import pygame as pg
from pygame.locals import *
from random import randint
from sprites import *
import sys, os, time, random

BACKGROUND = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 255, 0)
FPS = 60


class Asteroid(pg.sprite.Sprite):
    vx = 0
    vy = 0    
    num_sprites = 29      

    def __init__(self):
        self.w = 40
        self.h = 40      
        super().__init__()
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32,)        
        self.rect = self.image.get_rect()        
        self.images = self.loadImages()                
        self.image_act = 0
        self.image.blit(self.images[self.image_act], [0, 0])
        

    def loadImages(self):
        images = []
        for i in range(self.num_sprites):
            image = pg.image.load("./resources/sprites/asteroid/asteroid_{}.png".format(i))            
            images.append(image)            
        return images
       
    def cambio_asteroid(self):
        if self.w == 40:
            self.loadImages()
        self.loadImages1()

    def estrellado(self, group):
        lista_colision = pg.sprite.spritecollide(self, group, False)
        if len(lista_colision) > 0:
            self.destroy.play()    
    
    def update(self, limSupX, limSupY):
        self.vx = randint(3,10)
        if self.rect.centerx <= 0:
            self.rect.centerx = 800
            self.rect.centery = randint (40, 560)                                      
            
        self.rect.centerx -= self.vx
        #animar asteroide
        self.image_act += 1
        if self.image_act >= self.num_sprites:
            self.image_act = 0

        self.image.blit(self.images[self.image_act], (0, 0))        
        
class AsteroidGold(pg.sprite.Sprite):
    vx = 0
    vx = 0
    num_sprites = 29

    def __init__(self):
        self.w = 80
        self.h = 80
        super().__init__()
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.images_1 = self.loadImages1()
        self.image_act = 0
        self.image.blit(self.images_1[self.image_act], [0, 0])

    def loadImages1(self):
        images_1 = []
        for i in range(self.num_sprites):
            image = pg.image.load("./resources/sprites/asteroid1/asteroid1_{}.png".format(i))            
            images_1.append(image)            
        return images_1

    def update(self, limSupX, limSupY):
        self.vx = randint(3,10)
        if self.rect.centerx <= 0:
            self.rect.centerx = 800
            self.rect.centery = randint (40, 560)

        self.rect.centerx -= self.vx
        #animar asteroide
        self.image_act += 1
        if self.image_act >= self.num_sprites:
            self.image_act = 0

        self.image.blit(self.images_1[self.image_act], (0, 0))

class Nave(pg.sprite.Sprite):
    vx = 0
    vy = 0
    w = 65
    h = 65
    num_sprites = 17      
    clock = pg.time.Clock()
     
    
    def __init__(self, x, y):
        super().__init__()        
        self.image = pg.Surface((self.w, self.h), pg.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.giraCentro = (x, y)

        self.animation_time = FPS//1000 * 3
        self.angle = 0
        self.current_time = 0
        self.frame = pg.image.load('./resources/sprites/nave/Spaceships_0.png').convert_alpha()
        self.image.blit(self.frame, (0, 0), (0, 0, self.w, self.h))

        self.rotando = False
        
        

        #self.destroy = pg.mixer.Sound('./resources/sounds/retro-explosion-07.wav')

        self.rect.centerx = 40
        self.rect.centery = 300

    def estrellado(self, group):
        lista_colision = pg.sprite.spritecollide(self, group, False)
        if len(lista_colision) > 0:
            #self.destroy.play()
            self.__status = 'explotando'       
    
    def loadImages(self):
        images = []
        for i in range(self.num_sprites):
            image = pg.image.load("./resources/sprites/nave/Spaceships_{}.png".format(i))
            images.append(image)
        return images

    def update(self, limSupX, limSupY):        
        dt = self.clock.tick(FPS)
        self.current_time += dt

        if self.rotando is True:
            self.angle = (self.angle +1)%360
            self.image = pg.transform.rotate(self.frame, self.angle)
            rect = self.image.get_rect()
            mitadW = rect.centerx
            mitadH = rect.centery

            dX = mitadW - self.w // 2
            dY = mitadH - self.h // 2

            self.rect.centerx = self.giraCentro[0] - dX
            self.rect.centery = self.giraCentro[1] - dY                        

            if self.angle % 180 == 0:
                self.vx = 1
                self.rect.centerx -= self.vx
                self.rotando = False
                
                
        else:            
            self.rect.centerx += self.vx
            self.rect.centery += self.vy
            if self.rect.centerx >= 570:
                self.vx = 0

            if self.rect.centery < self.rect.h // 2:
                self.rect.centery = self.rect.h // 2

            if self.rect.centery > limSupY - self.rect.h // 2:
                self.rect.centery = limSupY - self.rect.h // 2
            
               


 

class Planeta(pg.sprite.Sprite):
    vx = 0
    vy = 0
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("./resources/images/planeta_arido.png")
        self.rect = self.image.get_rect()
        #self.image.blit(self.image)
        
        self.rect.centerx = 1100
        self.rect.centery = 300        


    def update(self, limSupX, limSupY):
        self.vx = 1
        if self.rect.centerx <= 800:
            self.vx = 0

        self.rect.centerx -= self.vx

