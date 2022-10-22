import pygame, sys
from settings import *
from tile import *
from player import *
class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles = pygame.sprite.Group()
        self.create_map()
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                tileName = WORLD_MAP[row_index][col_index].split("-")
                if col == 'x':
                    Tile((x,y), [self.visible_sprites, self.obstacles], 'images\character\Rock1.png')
                elif col == 'p':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacles)
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2(100, 200)

    def custom_draw(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
            