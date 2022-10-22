import pygame
from settings import *
class Tile:
    def __init__(self, pos, groups, image): 
        super().__init__(groups)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0,-10)