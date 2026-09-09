
import pygame

from src.constants import *

from src.util import *

gTextures = {
    "tileset":pygame.image.load("assets/Overworld_Tileset.png"),
    "cursor":pygame.image.load("assets/cursor.png"),
    "cursor_shadow":pygame.image.load("assets/cursor_shadow.png"),
    "tile_focus":pygame.image.load("assets/tile_focus.png")
}

gFrames = {
    "tileset":generateTileSets(gTextures["tileset"], TILE_WIDTH, TILE_HEIGHT)
}