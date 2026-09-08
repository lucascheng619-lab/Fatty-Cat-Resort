from src.Tile import Tile
from src.constants import *

class LevelGenerator:
    def generate_empty_grassland(tileset, width, height):
        tiles = []
        row = 0
        ID = PLAIN_GRASS_ID
        for y in range(height):
            tiles.append([])
            for x in range(width):
                tiles[row].append(Tile(
                    tileset,
                    ID,
                    x * TILE_WIDTH,
                    y * TILE_HEIGHT
                    
                ))
            row += 1

        return tiles
