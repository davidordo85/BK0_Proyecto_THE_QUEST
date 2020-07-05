

import pygame as pg
from pygame.locals import *
from random import randint
import sys, os, time
from sprites import *
from Objetos import *


WHITE = (255,255,255)
BLUE = (0,255,0)
BLACK = (0, 0, 0)
WIN_SCORE_GAME = 1000
WIN_SCORE_GAME_01 = 4000

FPS = 60

class Game():
    clock = pg.time.Clock()

    def __init__(self):
        self.pantalla = pg.display.set_mode((800, 600))
        self.espacio1 = pg.image.load("./resources/images/orion.jpg")
        
        self.titulo = pg.font.Font('./resources/fonts/OdibeeSans-Regular.ttf', 100)
        self.k_space = pg.font.Font('./resources/fonts/Lobster-Regular.ttf', 35)

        self.text_inicial = self.titulo.render("THE QUEST", False, BLACK, BLUE)
        self.text_space = self.k_space.render("PRESIONAR <SPACE> PARA CONTINUAR", False, BLACK)
        self.text_aterrizar = self.k_space.render("PRESIONAR TECLA <T> PARA ATERRIZAR", False, WHITE)

        self.status = 'Portada'
        
        self.pantalla = pg.display.set_mode((800, 600))
        self.espacio = pg.image.load("./resources/images/fondo_espacio.png")
        self.font = pg.font.Font('./resources/fonts/lobster-Regular.ttf', 30)
        self.nave = Nave(50, 300)
        self.asteroid = Asteroid()
        self.asteroid1 = Asteroid()
        self.asteroidG = AsteroidGold()
        self.planeta_desert = Planeta()

        self.asteroidsGroup = pg.sprite.Group()

        self.asteroidsGroup.add(self.asteroid)
        self.asteroidsGroup.add(self.asteroid1)
        self.asteroidsGroup.add(self.asteroidG)
                

        self.puntuacion = self.font.render("0", True, WHITE)

        self.allSprites = pg.sprite.Group()
        self.allSprites.add(self.nave)
        self.allSprites.add(self.asteroidsGroup)
        #self.allSprites.add(self.planeta_desert)
        

        self.score = 0

        pg.display.set_caption("THE QUEST")
        
    def bucle_principal(self):
        inicio_partida = False
        while not inicio_partida:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        inicio_partida = True

            self.pantalla.blit(self.espacio1, (0,0))
            self.pantalla.blit(self.text_inicial, (200, 150))
            self.pantalla.blit(self.text_space, (100, 400))            

            pg.display.flip()
        
        self.status = 'Empezar'

    def handlenEvent(self):
        for event in pg.event.get():            
            if event.type == QUIT:
                return self.quit()
                
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.nave.vy  = -5                        
                        
                if event.key == K_DOWN:
                    self.nave.vy  = 5                
                if event.key == K_t:                   
                    self.nave.rotando = True
                    

        key_pressed = pg.key.get_pressed()
        if key_pressed[K_UP]:
            self.nave.vy -= 1
                
        elif key_pressed[K_DOWN]:
            self.nave.vy += 1
        else:
            self.nave.vy = 0

        return False

    def primer_nivel(self):
        self.status = 'Empezar'
        primerN = False
        
        while not primerN:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        primerN = True            

            self.pantalla.blit(self.espacio, (0,0))
            self.pantalla.blit(self.nave. image, (30, 270))
            self.pantalla.blit(self.puntuacion, (30, 30))
            self.pantalla.blit(self.text_space, (100, 400))
            pg.display.flip()
            self.status = 'Partida'

        else:
            primerN = True
        

    def pantalla_primer_nivel(self):        
        primer = False        
        self.score = 0
        x = 0        
        self.puntuacion = self.font.render(str(self.score), True, WHITE)
        while not primer:            
            primer = self.handlenEvent()
            self.allSprites.update(800, 600)
            self.nave.update(800, 600)
            #self.planeta_desert.update(800, 600)
            self.nave.estrellado(self.asteroidsGroup)                       

            if self.asteroid.rect.centerx <= 0 or self.asteroid1.rect.centerx <= 0:                
                self.score += 20
                self.puntuacion = self.font.render(str(self.score), True, WHITE)
            elif self.asteroidG.rect.centerx <= 0:
                self.score += 40
                self.puntuacion = self.font.render(str(self.score), True, WHITE)
                    
            
            if self.score >= WIN_SCORE_GAME:                
                self.planeta_desert.update(800, 600)
                self.nave.rotate(20)
                self.pantalla.blit(self.text_aterrizar, (100, 400))
                pg.display.flip()
                # desaparezcan asteroidGroup
                    
                if self.nave.rect.centerx == 570:
                    primer = True

            #Animación pantalla        
            x -= 0.5
            if x <= -2400:
                x = 0

            self.pantalla.blit(self.espacio, (x, 0))    
            self.pantalla.blit(self.espacio, (x+2400, 0))
            
            self.allSprites.draw(self.pantalla)
                        
            self.pantalla.blit(self.planeta_desert.image, (self.planeta_desert.rect.x, self.planeta_desert.rect.y))                      
            self.pantalla.blit(self.puntuacion, (30, 30))            

            pg.display.flip()
            self.status = 'EntreJuego'            

    # Aún en proceso
    def bucle_intermedio(self):
        bucle_entreJuego = False
        self.puntuacion = self.font.render(str(self.score), True, WHITE)
        while not bucle_entreJuego:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        bucle_entreJuego = True

            self.nave.rect.centerx = 50
            self.planeta_desert.rect.centerx = 1100

            self.pantalla.fill((0, 0, 255))
            self.pantalla.blit(self.text_space, (100, 400))
            self.pantalla.blit(self.puntuacion, (400, 300))
            
         

            pg.display.flip()

            self.status = 'Partida_1'
            
        

    def pantalla_segundo_nivel(self):
        segundo = False        
        x = 0
        self.puntuacion = self.font.render(str(self.score), True, WHITE)
        while not segundo:
            segundo = self.handlenEvent()                    
            self.allSprites.update(800, 600)
            self.nave.update(800, 600)
            #self.asteroid.estrellado(self.nave)
            self.nave.estrellado(self.asteroidsGroup)
            

            if self.asteroid.rect.centerx <= 0 or self.asteroid1.rect.centerx <= 0:                
                self.score += 40
                self.puntuacion = self.font.render(str(self.score), True, WHITE)
            elif self.asteroidG.rect.centerx <= 0:
                self.score += 80
                self.puntuacion = self.font.render(str(self.score), True, WHITE)
                
            if self.score >= WIN_SCORE_GAME_01:
                self.planeta_desert.update(800, 600)
                self.nave.rotate(20)
                if self.nave.rect.centerx == 570:
                    segundo = True
            else:
                segundo = False
                
            x -= 0.5
            if x <= -2400:
                x = 0

            self.pantalla.blit(self.espacio, (x, 0))    
            self.pantalla.blit(self.espacio, (x+2400, 0))
            self.allSprites.draw(self.pantalla)            
            self.pantalla.blit(self.planeta_desert.image, (self.planeta_desert.rect.x, self.planeta_desert.rect.y))                      
            self.pantalla.blit(self.puntuacion, (30, 30))
            
            pg.display.flip()
            self.status = 'EntreJuego'     

    
    def main_loop(self):
        while True:
            if self.status == 'Portada':
                self.bucle_principal()
            elif self.status == 'Partida':
                self.pantalla_primer_nivel()
            elif self.status == 'Partida_1':
                self.pantalla_segundo_nivel()
            elif self.status == 'EntreJuego':
                self.bucle_intermedio()
            elif self.status == 'Empezar':
                self.primer_nivel()                    
            else:
                pass

    def quit(self):
        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.main_loop()
    game.quit()