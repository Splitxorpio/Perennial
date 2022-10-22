from os import walk
import pygame
from csv import reader

def import_folder(path):
    surface_list = []
    for __,__, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
            
    return surface_list
def import_csv_layout(path):
    terrain_list = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_list.append(list(row))
    return terrain_list