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
        self.hearts = 60
        self.boss_health = 100
        self.heal = 50
        self.stamina = 60
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
    def win(self):
        vid = Video("winner.mp4")
        vid.set_size((WIDTH, HEIGHT))
        self.screen.fill((0,0,0))
        while True:
            vid.draw(self.screen, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vid.close()
                    self.title_screen()
    def lose(self):
        vid = Video("loser.mp4")
        vid.set_size((WIDTH, HEIGHT))
        self.screen.fill((0,0,0))
        while True:
            vid.draw(self.screen, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vid.close()
                    self.title_screen()
    def heartss(self):
        font = pygame.font.Font('Xeliard.ttf', 50)
        text = font.render(str(self.hearts), True, (123,195,129))
        TextRect = text.get_rect()
        TextRect.center = (135, 55)
        self.screen.blit(text, TextRect)
        text = font.render(str(self.boss_health), True, (123,195,129))
        TextRect = text.get_rect()
        TextRect.center = (700, 430)
        self.screen.blit(text, TextRect)
        text = font.render(str(self.stamina), True, (123,195,129))
        TextRect = text.get_rect()
        TextRect.center = (570, 510)
        self.screen.blit(text, TextRect)
    def boss_fight(self):
        sound = pygame.mixer.Sound('Ike Aimes.mp3')
        pygame.mixer.Sound.play(sound)
        while True:
            self.screen.fill((0,0,0))
            # put text on screen
            imp = pygame.image.load("images\Pbossscene2.png").convert()
            self.screen.blit(imp, (0,0))
            self.heartss()
            if self.boss_health <= 0:
                pygame.mixer.Sound.stop(sound)
                self.win()
            if self.hearts <= 0:
                pygame.mixer.Sound.stop(sound)
                self.lose()
            for event in pygame.event.get():
                print(self.hearts)
                print(self.boss_health)
                print(self.heal)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        if self.heal > 0 and self.hearts < 60 and self.stamina > 0:
                            self.hearts += 10
                            self.heal -= 10
                            self.stamina -= 10
                            self.heartss()
                        elif self.stamina <= 0:
                            print("You are out of stamina")
                            self.heartss()
                        elif self.hearts == 60:
                            print("You are at full health")
                            self.heartss()
                        elif self.heal <= 0:
                            print("You cannot heal yourself!")
                            self.heartss()
                    if event.key == pygame.K_f:
                        self.boss_health -= 10
                        self.hearts -= 10
                        self.heartss()
                if event.type == pygame.QUIT:
        
                    # deactivates the pygame library
                    pygame.quit()
        
                    # quit the program.
                    quit()
        
                # Draws the surface object to the screen.
                pygame.display.update()
    def boss_match(self):
        vid = Video("BossFight.mp4")
        vid.set_size((WIDTH, HEIGHT))
        self.screen.fill((0,0,0))
        while True:
            vid.draw(self.screen, (0, 0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    vid.close()
                    self.boss_fight()
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
            if self.level.stuff:
                pygame.mixer.Sound.stop(sound)
                self.boss_match()
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