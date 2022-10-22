import pygame, sys
from random import randint
from settings import *
from level import *
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((0,0,100))
            self.level.run()
            pygame.display.flip()
            self.clock.tick(TICK_SPEED)
            
if __name__ == '__main__':
    game = Game()
    game.run()