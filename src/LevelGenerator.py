from src.Tile import Tile
from src.constants import *

class LevelGenerator:
    def generate_empty_island(tileset, width, height):
        tiles = []
        row = 0
        for y in range(height):
            tiles.append([])
            for x in range(width):
                if x > 2 and x < width - 3 and y > 2 and y < height - 3:
                    tiles[row].append(Tile(
                        tileset,
                        x * TILE_WIDTH,
                        y * TILE_HEIGHT,
                        "grass", # sets the type as grass
                        True #means the tile cannot be edited
                        
                    ))
                else:
                    tiles[row].append(Tile(
                        tileset,
                        x * TILE_WIDTH,
                        y * TILE_HEIGHT,
                        "water", # sets the type as water
                        False #means the tile cannot be edited
                    ))
            row += 1

        return tiles
    
    def generate_water(tileset, width, height):
        tiles = []
        row = 0
        for y in range(height):
            tiles.append([])
            for x in range(width):
                tiles[row].append(Tile(
                    tileset,
                    x * TILE_WIDTH,
                    y * TILE_HEIGHT,
                    "water" # sets the type as grass
                    
                ))
            row += 1

        return tiles
