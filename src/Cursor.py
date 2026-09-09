#the cursor is the cursor and screen and cannot interact with the tilemap

import pygame

from src.constants import *

class Cursor:
    def __init__(self, texture, shadowTexture):
        pygame.mouse.set_visible(False)
        self.texture = texture
        self.shadowTexture = shadowTexture
        self.x = 0
        self.y = 0

    def update(self, params):
        #pygame.mouse.get_pos() return x and y values
        self.x = pygame.mouse.get_pos()[0] / (SCREEN_WIDTH / CANVAS_WIDTH) #gets x position of mouse
        self.y = pygame.mouse.get_pos()[1] / (SCREEN_HEIGHT / CANVAS_HEIGHT)#gets y position of mouse

    def render(self, params):
        self.shadowTexture.set_alpha(100)

        params["canvas"].blit(self.texture, (self.x, self.y)) #renders the mouse
        params["canvas"].blit(self.shadowTexture, (self.x, self.y + 2)) #renders the shadow