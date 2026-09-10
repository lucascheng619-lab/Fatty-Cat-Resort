import pygame

class TerrainEditor:
    def __init__(self, focus, tilemap):
        self.currentBrush = None
        self.focus = focus
        self.tilemap = tilemap

    def update(self, params):
        self.focus.update(params)


        if pygame.mouse.get_pressed()[0]: #checks if the left click button is being pressed
            self.tilemap.tilemap[self.focus.tileY][self.focus.tileX].type = self.currentBrush



    def changeBrush(self, brush):
        self.currentBrush = brush

    def render(self, params):
        self.focus.render(params)