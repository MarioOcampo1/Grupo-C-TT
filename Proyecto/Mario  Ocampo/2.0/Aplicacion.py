import pygame
from pygame.locals import *
from Juego import *
from Jugador import *
from Covid import *
from random import randint
from Computadora import*


import time


class Aplicacion:
    windowWidth = 800
    windowHeight = 600
    jugador = 0
    covid = 0
    computadora=0


    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._covid_surf = None
        self.juego=Juego()
        self.jugador = Jugador(3)
        self.covid = Covid(5, 5)
        self.computadora=Computadora(3)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth, self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('A cazar covid19')
        self._running = True
        self._image_surf = pygame.image.load("E:\TSUP\Metodologia investigacion\Proyecto/block.jpg").convert()
        self._covid_surf = pygame.image.load("E:\TSUP\Metodologia investigacion\Proyecto/virus.jpg").convert()


    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        self.jugador.update()
        self.computadora.update()


        # For que explica cuando se come a un covid
        for i in range(0, self.jugador.longitud):
            if self.juego.isCollision(self.covid.x, self.covid.y, self.jugador.x[i], self.jugador.y[i], 44):
                self.covid.x = randint(2, 9) * 44
                self.covid.y = randint(2, 9) * 44
                self.jugador.longitud = self.jugador.longitud + 1  # aumenta el tamaño de la serpiente en 1
        for i in range(0,self.computadora.longitud):
            if self.juego.isCollision(self.covid.x,self.covid.y,self.computadora.x[i],self.computadora.y[i],44):
                self.covid.x = randint(2, 9) * 44
                self.covid.y = randint(2, 9) * 44
                self.computadora.longitud=self.computadora.longitud+1
        for i in range(0,self.jugador.longitud):
            if self.juego.isCollision(self.computadora.x[0],self.computadora.y[0],self.jugador.x[i],self.jugador.y[i],44):
                print("Chocaste contra la computadora, GAME OVER")
                exit(0)
        # For que maneja cuando la serpiente choca contra si misma.
        for i in range(2, self.jugador.longitud):
            if self.juego.isCollision(self.jugador.x[0], self.jugador.y[0], self.jugador.x[i], self.jugador.y[i], 40):
                print("Chocaste, perdiste!!! ")
                print("x[0] (" + str(self.jugador.x[0]) + "," + str(self.jugador.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.jugador.x[i]) + "," + str(self.jugador.y[i]) + ")")
                exit(0)
            if self.jugador.x[i]>=self.windowHeight or self.jugador.y[i]==self.windowWidth:
                print("Chocaste contra el borde, perdiste!!! ")
                print("x[0] (" + str(self.jugador.x[0]) + "," + str(self.jugador.y[0]) + ")")
                print("x[" + str(i) + "] (" + str(self.jugador.x[i]) + "," + str(self.jugador.y[i]) + ")")
                exit(0)


        pass

    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.jugador.draw(self._display_surf, self._image_surf)
        self.covid.draw(self._display_surf, self._covid_surf)
        self.computadora.draw(self._display_surf, self._image_surf)
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            self.computadora.target(self.covid.x,self.covid.y)

            if (keys[K_RIGHT]):
                self.jugador.moveRight()

            if (keys[K_LEFT]):
                self.jugador.moveLeft()

            if (keys[K_UP]):
                self.jugador.moveUp()

            if (keys[K_DOWN]):
                self.jugador.moveDown()

            if (keys[K_ESCAPE]):
                self._running = False



            self.on_loop()
            self.on_render()

            time.sleep(50.0 / 1000.0);
        self.on_cleanup()