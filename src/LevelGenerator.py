from src.Tile import Tile
from src.constants import *

class LevelGenerator:
    def generate_empty_grassland(tileset, width, height):
        tiles = []
        row = 0
        for y in range(height):
            tiles.append([])
            for x in range(width):
                tiles[row].append(Tile(
                    tileset,
                    x * TILE_WIDTH,
                    y * TILE_HEIGHT,
                    "grass" # sets the type as grass
                    
                ))
            row += 1

        return tiles
