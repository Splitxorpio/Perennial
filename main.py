from email import message
from pydoc import TextRepr
import pygame, sys
from random import randint
from settings import *
from level import *
from pyvidplayer import *
from support import *
class Game:
    def __init__(self):
        pygame.init()
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
        sound = pygame.mixer.Sound('testt.mp3')
        pygame.mixer.Sound.play(sound)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill((0,0,100))
            self.level.run()
            pygame.display.flip()
            self.clock.tick(TICK_SPEED) 
    def title_screen(self):
        sound = pygame.mixer.Sound('Perrenial Title Screen.mp3')

        pygame.mixer.Sound.play(sound)
        while True:
            self.screen.fill((0,0,0))
            # put text on screen
            imp = pygame.image.load("images\PerennialTitle.png").convert()
            font = pygame.font.Font('Xeliard.ttf', 32)
            text = font.render('Click Anywhere To Start', True, (0,0,0))
            TextRect = text.get_rect()
            TextRect.center = (WIDTH // 2, HEIGHT // 1.3)
            self.screen.blit(imp, (0,0))
            self.screen.blit(text, TextRect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.stop(sound)
                    self.intro()
                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if event.type == pygame.QUIT:
        
                    # deactivates the pygame library
                    pygame.quit()
        
                    # quit the program.
                    quit()
        
                # Draws the surface object to the screen.
                pygame.display.update()
if __name__ == '__main__':
    game = Game()
    game.title_screen()