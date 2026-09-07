
import pygame

from src.constants import *

from src.util import *

gTextures = {
    "tileset":pygame.image.load("assets/Overworld_Tileset.png")
}

gFrames = {
    "tileset":generateTileSets(gTextures["tileset"], TILE_WIDTH, TILE_HEIGHT)
}