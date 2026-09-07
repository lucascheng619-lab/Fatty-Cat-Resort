import pygame
from src.Tile import Tile

def generateTileSets(tilesheet, tile_width, tile_height):

    #set up tile table
    tiles = []
    #iterates over every row
    for y in range(tilesheet.get_height() // tile_height):
        #adds a empty table which will store all the tile values for in the row
        tiles.append([])
        #then iterates over every coloumn in the row
        for x in range(tilesheet.get_width() // tile_width):
            rect = pygame.Rect(
                x * tile_width, #x position of tile on tilesheet
                y * tile_height, #y position of tile on tilesheet
                tile_width,
                tile_height
                )
            tiles.append(tilesheet.subsurface(rect))

    return tiles
            