import pygame
from src.AssetManager import *
from src.editors.BaseEditor import BaseEditor
from src.Focus import Focus
from src.gui.Button import Button
from src.GUI import GUI

class TerrainEditor(BaseEditor):
    def __init__(self):
        self.ID = "terrain_editor"
        self.currentBrush = None
        self.cursorTexture = gTextures["brush"] #sets the texture for the cursor
        self.cursorShadowTexture = gTextures["brush_shadow"] #sets shadow cursor texture
        self.focus = Focus(gTextures["tile_focus"])
        self.enabled = False #Editor is disabled whilst hoving over GUI


    def enter(self, params):
        self.tilemap = params["level"].tilemap
        self.gui = GUI([
            Button("grass_tile_brush_button", CANVAS_WIDTH / 2 - 25, CANVAS_HEIGHT - 40, gTextures["grass_tile_brush_button"],gTextures["grass_tile_brush_button_selected"]),
            Button("dirt_tile_brush_button", CANVAS_WIDTH / 2 + 5, CANVAS_HEIGHT - 40, gTextures["dirt_tile_brush_button"],gTextures["dirt_tile_brush_button_selected"])
            ])

    def getSurroundingTiles(self, tileX, tileY, tilemap):
        surroundingTiles = {}
        if tileY != 0: #checks that it is not the top row, if it is top row assign none to topLeft, topCentre, topRight
            surroundingTiles["topCentre"] = tilemap[tileY - 1][tileX]
            if tileX != 0:
                surroundingTiles["topLeft"] = tilemap[tileY - 1][tileX - 1]


            if tileX != LEVEL_WIDTH - 1:
                surroundingTiles["topRight"] = tilemap[tileY - 1][tileX + 1]




        if tileX != 0:
            surroundingTiles["middleLeft"] = tilemap[tileY][tileX - 1]

        
        if tileX != LEVEL_WIDTH - 1:
            surroundingTiles["middleRight"] = tilemap[tileY][tileX + 1]

        if tileY != LEVEL_HEIGHT - 1: #checks that it is not the bottom row, if it is bottom row assign none to bottomLeft, bottomCentre, bottomRight
            surroundingTiles["bottomCentre"] = tilemap[tileY + 1][tileX]
            if tileX != 0:
                surroundingTiles["bottomLeft"] = tilemap[tileY + 1][tileX - 1]
 
        
            if tileX != LEVEL_WIDTH - 1:
                surroundingTiles["bottomRight"] = tilemap[tileY + 1][tileX + 1]



        return surroundingTiles

    def update(self, params):

        for element in self.gui.elements:
            

            if element.checkHovering(params): #if the cursor is hovering above any gui disable the editor functionality
                self.enabled = False
            
            if element.ID == "grass_tile_brush_button":
                element.pressed = False
                if element.checkPressed(params):#checks if the select editor button is being pressed
                    
                    self.changeBrush("grass")

        
                if self.currentBrush == "grass": #makes element pressed to true if it is the right brush
                    element.pressed = True
                
                
                

            if element.ID == "dirt_tile_brush_button": 
                element.pressed = False

                if element.checkPressed(params):#checks if the terrain editor button is being pressed
                                
                    self.changeBrush("dirt")

            
                if self.currentBrush == "dirt":
                    element.pressed = True
                            
                
        
        if self.enabled:

            self.focus.update(params)
            self.cursorTexture = gTextures["brush"] #sets the texture for the cursor
            self.cursorShadowTexture = gTextures["brush_shadow"] #sets shadow cursor texture

        else:
            self.cursorTexture = gTextures["cursor"]
            self.cursorShadowTexture = gTextures["cursor_shadow"]

        tilemap = self.tilemap.tilemap #stored self.tilemap.tilemap in local variable because i'm too lazy to write the entire thing out everytime




        if pygame.mouse.get_pressed()[0] and self.enabled: #checks if the left click button is being pressed
            if tilemap[self.focus.tileY][self.focus.tileX].editable:
                tilemap[self.focus.tileY][self.focus.tileX].type = self.currentBrush
                if self.currentBrush == "grass":
                    y = self.focus.tileY
                    x = self.focus.tileX



                    surroundingTiles = self.getSurroundingTiles(x, y, tilemap)

                    if "middleLeft" in surroundingTiles and "middleRight" in surroundingTiles:
                        if surroundingTiles["middleLeft"].type == "dirt" and surroundingTiles["middleRight"].type == "dirt":
                            for tile in surroundingTiles:
                                surroundingTiles[tile].type = "grass"

                    if "topCentre" in surroundingTiles and "bottomCentre" in surroundingTiles:
                        if surroundingTiles["topCentre"].type == "dirt" and surroundingTiles["bottomCentre"].type == "dirt":
                            for tile in surroundingTiles:
                                surroundingTiles[tile].type = "grass"


        self.gui.update(params)




    def changeBrush(self, brush):
        self.currentBrush = brush

    def render(self, params):
        if self.enabled:
            self.focus.render(params)

        self.gui.render(params)