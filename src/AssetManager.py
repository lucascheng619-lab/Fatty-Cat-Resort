
import pygame

pygame.init() #initialises pygame, so the pygame.Font works

from src.constants import *

from src.util import *

gTextures = {
    #tileset
    "tileset":pygame.image.load("assets/Overworld_Tileset.png"),

    #special cursors
    "cursor":pygame.image.load("assets/gui/cursors/cursor.png"),
    "cursor_shadow":pygame.image.load("assets/gui/cursors/cursor_shadow.png"),
    "brush":pygame.image.load("assets/gui/cursors/brush.png"),
    "brush_shadow":pygame.image.load("assets/gui/cursors/brush_shadow.png"),
    "hammer_wrench":pygame.image.load("assets/gui/cursors/hammer_wrench.png"), #I have no idea if what I have drawn is a hammer or wrench
    "hammer_wrench_shadow":pygame.image.load("assets/gui/cursors/hammer_wrench_shadow.png"),

    #focus
    "tile_focus":pygame.image.load("assets/gui/focus/tile_focus.png"),
    "32x32_building_focus":pygame.image.load("assets/gui/focus/32x32_building_focus.png"),
    "32x32_building_red_focus":pygame.image.load("assets/gui/focus/32x32_building_red_focus.png"),


    #editor buttons

    "select_editor_button":pygame.image.load("assets/gui/buttons/select_editor_button.png"),
    "select_editor_button_selected":pygame.image.load("assets/gui/buttons/select_editor_button_selected.png"),
    "terrain_editor_button":pygame.image.load("assets/gui/buttons/terrain_editor_button.png"),
    "terrain_editor_button_selected":pygame.image.load("assets/gui/buttons/terrain_editor_button_selected.png"),
    "accommodation_editor_button":pygame.image.load("assets/gui/buttons/accommodation_editor_button.png"),
    "accommodation_editor_button_selected":pygame.image.load("assets/gui/buttons/accommodation_editor_button_selected.png"),


    
    #terrain editor buttons

    "grass_tile_brush_button":pygame.image.load("assets/gui/buttons/grass_tile_brush_button.png"),
    "grass_tile_brush_button_selected":pygame.image.load("assets/gui/buttons/grass_tile_brush_button_selected.png"),
    "dirt_tile_brush_button":pygame.image.load("assets/gui/buttons/dirt_tile_brush_button.png"),
    "dirt_tile_brush_button_selected":pygame.image.load("assets/gui/buttons/dirt_tile_brush_button_selected.png"),

    #accommodation buildings 


    "single_cardboard_box":pygame.image.load("assets/buildings/single_cardboard_box.png"),



}

gFrames = {
    "tileset":generateTileSets(gTextures["tileset"], TILE_WIDTH, TILE_HEIGHT)
}

gFonts = {
    "normal_font":pygame.font.Font("fonts/pixelFont.ttf", 11)
}