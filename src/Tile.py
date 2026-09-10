from src.constants import *

class Tile:
    def __init__(self, texture, x, y, type):
        self.texture = texture

        self.type = type

        self.ID = None

        
        

        self.x = x
        self.y = y


    def update(self, params):

        self.frame = self.texture[self.ID]
        

    def render(self, params):

        params["canvas"].blit(self.frame, (self.x - params["xOffset"], self.y - params["yOffset"]))