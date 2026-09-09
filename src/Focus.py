#The focus is able to interact with the tilemap and is rendered according to the tilemap

from src.constants import *

class Focus:
    def __init__(self, texture):
        self.texture = texture
        self.x = 0
        self.y = 0

    def update(self, params):
        self.tileX = (params["cursorX"] + params["cameraX"]) //TILE_WIDTH #makes the focus lock on to the nearest tile
        self.tileY = (params["cursorY"] + params["cameraY"]) //TILE_HEIGHT

        self.x = self.tileX * TILE_WIDTH
        self.y = self.tileY * TILE_HEIGHT

    def render(self, params):
        params["canvas"].blit(self.texture, (self.x - params["xOffset"], self.y - params["yOffset"]))