import pygame, sys
from random import randint
from settings import *
from level import *
from pyvidplayer import *
class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
    def intro(self):
        vid = Video("Retropix.mp4")
        vid.set_size((WIDTH, HEIGHT))
        while True:
            vid.draw(self.screen, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vid.close()
                    self.run()
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill((0,0,100))
            print(self.level.player.rect.centerx)
            print(self.level.player.rect.centery)
            self.level.run()
            pygame.display.flip()
            self.clock.tick(TICK_SPEED)
    
if __name__ == '__main__':
    game = Game()
    game.intro()