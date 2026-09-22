import pygame

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.texture = None


    def update(self, params):
        pass

    def render(self, params):
        params["canvas"].blit(self.texture, (self.x - params["xOffset"], self.y - params["yOffset"]))