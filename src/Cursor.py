#the cursor is the cursor and screen and cannot interact with the tilemap

import pygame

from src.constants import *

class Cursor:
    def __init__(self):
        pygame.mouse.set_visible(False)

        self.x = 0
        self.y = 0
        self.leftButtonPressed = False

        

    def update(self, params):
        #pygame.mouse.get_pos() return x and y values

        self.texture = params["editor"].cursorTexture
        self.shadowTexture = params["editor"].cursorShadowTexture
        
        self.leftButtonPressed = False

        if pygame.mouse.get_pressed()[0]:#checks if left button is being held down
            self.leftButtonPressed = True


        self.x = pygame.mouse.get_pos()[0] / (SCREEN_WIDTH / CANVAS_WIDTH) #gets x position of mouse in regard to canvas
        self.y = pygame.mouse.get_pos()[1] / (SCREEN_HEIGHT / CANVAS_HEIGHT)#gets y position of mouse in regard to canvas

    def render(self, params):
        self.shadowTexture.set_alpha(100)

        params["canvas"].blit(self.shadowTexture, (self.x, self.y + 2)) #renders the shadow

        if self.leftButtonPressed:
            params["canvas"].blit(self.texture, (self.x, self.y + 1))
        else:
            params["canvas"].blit(self.texture, (self.x, self.y)) #renders the mouse