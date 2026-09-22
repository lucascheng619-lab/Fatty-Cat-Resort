import pygame

from src.editors.BaseEditor import BaseEditor
from src.Focus import Focus
from src.AssetManager import *
from src.buildings.CardboardBox import CardboardBox


class AccommodationEditor(BaseEditor):
    def __init__(self):
        self.ID = "accommodation_editor"
        self.currentBrush = None
        self.enabled = False
        self.cursorTexture = gTextures["hammer_wrench"]
        self.cursorShadowTexture = gTextures["hammer_wrench_shadow"]
        self.focus = Focus(gTextures["32x32_building_focus"])
        
        

    def enter(self, params):
        self.level = params["level"]

    def areaClear(self, tileX, tileY, accommodation): #checks if the building can be placed in the area
        buildingTileWidth = accommodation.tileWidth
        buildingTileHeight = accommodation.tileHeight

        #check if the building is within the confines of the map
        if tileX > LEVEL_WIDTH - buildingTileWidth:
            return False

        if tileY > LEVEL_HEIGHT - buildingTileHeight:
            return False

        #checks if any of the tiles the accommodation is going to placed is already occupied
        for y in range(buildingTileHeight):
            for x in range(buildingTileWidth):
                if self.level.tilemap.tilemap[tileY + y][tileX + x].occupied:
                    return False


        return True

                

    def update(self, params):
        
        if self.enabled:
            self.cursorTexture = gTextures["hammer_wrench"]
            self.cursorShadowTexture = gTextures["hammer_wrench_shadow"]
        else:
            self.cursorTexture = gTextures["cursor"]
            self.cursorShadowTexture = gTextures["cursor_shadow"]

        self.focus.update(params)

        tilemap = self.level.tilemap.tilemap
        if self.currentBrush == "cardboard_box":
            accommodation = CardboardBox(
                self.focus.tileX * TILE_WIDTH,
                self.focus.tileY * TILE_HEIGHT
            )

        if self.areaClear(self.focus.tileX, self.focus.tileY, accommodation):
            self.focus.texture = gTextures["32x32_building_focus"]
            if pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and self.enabled: #checks if the left click button is being pressed
                    if tilemap[self.focus.tileY][self.focus.tileX].editable:
                        self.level.objects.append(accommodation)
                        for y in range(accommodation.tileHeight):
                            for x in range(accommodation.tileWidth):
                                tilemap[y+self.focus.tileY][x+self.focus.tileX].occupied = True
                        

        else:
            self.focus.texture = gTextures["32x32_building_red_focus"]
                    

    def render(self, params):
        self.focus.render(params)