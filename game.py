import pygame
from character import *
import math, time

class Game:
    def __init__(self, width = 500, height = 500) -> None:
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((width, height))
        
        #init the pool
        self.pool_center = (width // 2, height // 2)
        self.pool_r = 100
        
        
        #init mouse and cat
        mouse_veloc = math.pi/24
        cat_veloc = 4 * mouse_veloc
        self.mouse = character(
            init_position = (10, 0), #init at the center of the pool
            veloc = mouse_veloc,
            center= self.pool_center,
            image = pygame.image.load('mouse.png').convert_alpha() #image type in pygame
        )
        
        self.cat = character(
            init_position = (self.pool_r, 0), #init at the border of the pool
            veloc = cat_veloc,
            center= self.pool_center,
            image = pygame.image.load('cat.png').convert_alpha() #image type in pygame
        )
        #define some colors
        self.BACKGROUNDCOLOR = (255, 255, 255) # WHITE
        self.POOLCOLOR = (86, 161, 255)
        self.RED = (255, 0, 0)
        self.PINK = (255, 124, 124)

    def draw(self):
        self.screen.fill(self.BACKGROUNDCOLOR)
        #draw pool
        pygame.draw.circle(
            surface= self.screen,
            color= self.POOLCOLOR,
            center= self.pool_center,
            radius= self.pool_r
        )
        
        #draw mouse
        self.mouse.draw(self.screen)
        #draw cat
        self.cat.draw(self.screen)
        
        #draw center of the pool
        pygame.draw.circle(
            surface=self.screen,
            color=self.PINK,
            center= self.pool_center,
            radius= 5)
    def update(self):
        self.draw()
        pygame.display.flip()
        self.mouse.update()
        self.cat.update()
        pass

def main():
    game = Game()
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                break
        
        game.update()
        time.sleep(0.05)

main()
        
        