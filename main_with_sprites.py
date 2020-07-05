import pygame as pg
from pygame.locals import *
from random import randint
import sys, os, time
from sprites import *
from Objetos import *


WHITE = (255,255,255)
BLUE = (0,255,0)
BLACK = (0, 0, 0)
WIN_SCORE_GAME = 200
WIN_SCORE_GAME_01 = 2000

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

        self.status = 'Portada'
        
        self.text_siguiente = pg.font.Font('./resources/fonts/odibeeSans-Regular.ttf', 30)        

        self.text_inicial0 = self.text_siguiente.render("LA BUSQUEDA COMIENZA EN UN PLANETA TIERRA ", False, WHITE)
        self.text_inicial1 = self.text_siguiente.render("MORIBUNDO POR EL CAMBIO CLIMÁTICO.", False, WHITE)
        self.text_inicial2 = self.text_siguiente.render("PARTIREMOS A LA BUSQUEDA DE UN PLANETA", False, WHITE)
        self.text_inicial3 = self.text_siguiente.render("COMPATIBLE CON LA VIDA HUMANA PARA COLONIZARLO.", False, WHITE)
        
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
        
        self.status = 'Partida'
    '''
    def bucle_introduccion(self):
        inicio_portada = False
        while not inicio_portada:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        inicio_portada = True            

            self.pantalla.fill((0, 0, 255))            
            self.pantalla.blit(self.text_inicial0, (30, 30))
            self.pantalla.blit(self.text_inicial1, (30, 80))
            self.pantalla.blit(self.text_inicial2, (30, 130))
            self.pantalla.blit(self.text_inicial3, (30, 180))

            pg.display.flip()

        self.status = 'Partida'
    '''
    def handlenEvent(self):
        for event in pg.event.get():            
            if event.type == QUIT:
                return self.quit()
                
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.nave.vy  = -5                        
                        
                    if event.key == K_DOWN:
                        self.nave.vy  = 5                        

        key_pressed = pg.key.get_pressed()
        if key_pressed[K_UP]:
            self.nave.vy -= 1
                
        elif key_pressed[K_DOWN]:
            self.nave.vy += 1
        else:
            self.nave.vy = 0

        return False
        
    def bucle_partida(self):        
        bucle_juego = False        
        self.score = 0
        x = 0
        
        
        self.puntuacion = self.font.render(str(self.score), True, WHITE)
        while not bucle_juego:            
            bucle_juego = self.handlenEvent()

            self.allSprites.update(800, 600)
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
                self.nave.rotando = True

                
                #bucle_juego = True
                                
            else:
                bucle_juego = False

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

    def bucle_intermedio(self):
        bucle_entreJuego = False
        self.puntuacion = self.font.render(str(self.score), True, WHITE)
        while not bucle_entreJuego:
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        bucle_entreJuego = True

            self.pantalla.fill((0, 0, 255))
            self.pantalla.blit(self.text_space, (100, 400))
            self.pantalla.blit(self.puntuacion, (400, 300))

            pg.display.flip()

            self.status = 'Partida_1'
            
        

    def bucle_partida_1(self):
        bucle_juego1 = False        
        x = 0
        self.puntuacion = self.font.render(str(self.score), True, WHITE)
        while not bucle_juego1:
            bucle_juego1 = self.handlenEvent()             
               
            self.allSprites.update(800, 600)
            #self.asteroid.estrellado(self.nave)
            self.nave.estrellado(self.asteroidsGroup)          

            if self.asteroid.rect.centerx <= 0:                
                self.score += 40
                self.puntuacion = self.font.render(str(self.score), True, WHITE)                
                
                if self.score == WIN_SCORE_GAME:
                    bucle_juego1 = True
                    
                
            x -= 0.5
            if x <= -2400:
                x = 0

            self.pantalla.blit(self.espacio, (x, 0))    
            self.pantalla.blit(self.espacio, (x+2400, 0))
            self.allSprites.draw(self.pantalla)
            '''         
            self.pantalla.blit(self.nave.image, (self.nave.rect.x, self.nave.rect.y))
            self.pantalla.blit(self.asteroid.image, (self.asteroid.rect.x, self.asteroid.rect.y))
            '''
            self.pantalla.blit(self.puntuacion, (740, 30))

            pg.display.flip()
    '''
    def Game_over(self):
        game_over = False

        while not game_over:
            game_over = self.handlenEvent()
    '''       

    
    def main_loop(self):
        while True:
            if self.status == 'Portada':
                self.bucle_principal()
            elif self.status == 'Partida':
                self.bucle_partida()
            elif self.status == 'Partida_1':
                self.bucle_partida_1()
            elif self.status == 'EntreJuego':
                self.bucle_intermedio()                    
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