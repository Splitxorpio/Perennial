from turtle import distance
import pygame
from settings import *
from support import *

class Lizard(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):

    # general setup
        super().__init__(groups)
        self.sprite_type = 'bossindicator'

        # graphics setup
        self.status = 'idle'
        self.image = pygame.image.load('images/bossIndicator/bossIndicator.png')

        # movement
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        self.obstacle_sprites = obstacle_sprites