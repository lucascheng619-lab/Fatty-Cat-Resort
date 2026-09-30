from src.constants import *
from src.animation_defs import TILE_ANIMATIONS
from src.Animation import Animation

class Tile:
    def __init__(self, texture, x, y, type, editable = True):
        self.texture = texture
        self.editable = editable
        self.occupied = False

        self.type = type

        self.ID = None

        self.animation = Animation(None, None) #sets a filler animation until the Tile gets its ID
        

        self.x = x
        self.y = y
        self.lastID = self.ID


    def update(self, params):

        self.animation.frames = TILE_ANIMATIONS[self.ID]["frames"]
        self.animation.interval = TILE_ANIMATIONS[self.ID]["interval"]

        #if the frames changes reset the current animation back to 0
        if self.lastID != self.ID:
            self.animation.currentFrame = 0



        self.animation.update(params)

        


        self.frame = self.texture[self.animation.getFrame()]
        self.lastID = self.ID
        

    def render(self, params):

        params["canvas"].blit(self.frame, (self.x - params["xOffset"], self.y - params["yOffset"]))