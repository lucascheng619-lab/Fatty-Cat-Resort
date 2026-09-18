
import pygame

pygame.init() #initialises pygame, so the pygame.Font works

from src.constants import *

from src.util import *

gTextures = {
    "tileset":pygame.image.load("assets/Overworld_Tileset.png"),
    "cursor":pygame.image.load("assets/gui/cursor.png"),
    "cursor_shadow":pygame.image.load("assets/gui/cursor_shadow.png"),
    "tile_focus":pygame.image.load("assets/gui/tile_focus.png"),
    "select_editor_button":pygame.image.load("assets/gui/select_editor_button.png"),
    "select_editor_button_selected":pygame.image.load("assets/gui/select_editor_button_selected.png"),
    "brush":pygame.image.load("assets/gui/brush.png"),
    "brush_shadow":pygame.image.load("assets/gui/brush_shadow.png"),
    "terrain_editor_button":pygame.image.load("assets/gui/terrain_editor_button.png"),
    "terrain_editor_button_selected":pygame.image.load("assets/gui/terrain_editor_button_selected.png"),
    "grass_tile_brush_button":pygame.image.load("assets/gui/grass_tile_brush_button.png"),
    "grass_tile_brush_button_selected":pygame.image.load("assets/gui/grass_tile_brush_button_selected.png"),
    "dirt_tile_brush_button":pygame.image.load("assets/gui/dirt_tile_brush_button.png"),
    "dirt_tile_brush_button_selected":pygame.image.load("assets/gui/dirt_tile_brush_button_selected.png"),

}

gFrames = {
    "tileset":generateTileSets(gTextures["tileset"], TILE_WIDTH, TILE_HEIGHT)
}

gFonts = {
    "normal_font":pygame.font.Font("fonts/pixelFont.ttf", 11)
}