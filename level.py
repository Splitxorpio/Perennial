import pygame, sys
from settings import *
from tile import *
from player import *
from support import *
from random import choice
class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles = pygame.sprite.Group()
        self.create_map()
    def create_map(self):
        layout = {
            'boundary' : import_csv_layout('Border.csv'),
            'obstacles': import_csv_layout('PerennialMapObstacles_obstacles.csv'),
            'walls': import_csv_layout('Walls.csv'),
        }
        graphics = {
            'obstacles': import_folder('images/Obstacles'),
            'walls': import_folder('images/Walls'),
        }
        print(graphics)
        for style, layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILE_SIZE
                        y = row_index * TILE_SIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacles], 'invisible' )
                        if style == 'obstacles':
                            random_obstacle = choice(graphics['obstacles'])
                            Tile((x,y), [self.visible_sprites,self.obstacles], 'obstacles', random_obstacle)
                        if style == 'walls':
                            random_wall = choice(graphics['walls'])
                            Tile((x,y), [self.visible_sprites,self.obstacles], 'walls', random_wall)
        #         tileName = WORLD_MAP[row_index][col_index].split("-")
        #         if col == 'x':
        #             Tile((x,y), [self.visible_sprites, self.obstacles], 'images\character\Rock1.png')
        #         elif col == 'p':
        #             self.player = Player((x,y), [self.visible_sprites], self.obstacles)
        self.player = Player((877,722), [self.visible_sprites], self.obstacles)

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

        self.floor = pygame.image.load('images\PerennialMap.png').convert()
        self.floor_rect = self.floor.get_rect(topleft = (0,0))
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor, floor_offset_pos)
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

            