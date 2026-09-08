import pygame

from src.constants import *

class Player:
    def __init__(self, x, y, tilemap):

        self.tilemap = tilemap

        self.mapWidth = self.tilemap.width * TILE_WIDTH
        self.mapHeight = self.tilemap.height * TILE_WIDTH


        self.x = x
        self.y = y

        self.dy = 0
        self.dx = 0

    def update(self, params):

        self.dx = 0
        self.dy = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]: #checks if the up key is pressed and makes sure the down key is not pressed
            self.dy = -CAMERA_SPEED
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.dy = CAMERA_SPEED

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.dx = -CAMERA_SPEED
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.dx = CAMERA_SPEED

        self.x += (self.dx * params["dt"])
        self.y += (self.dy * params["dt"])

        self.x = max(0, min(self.x, self.mapWidth)) #Clamps the x and y coroinates of the player
        self.y = max(0, min(self.y, self.mapHeight))


    def render(self, params):
        self.surf = pygame.surface.Surface((2,2))

        self.surf.fill((255, 255, 255))

        params["canvas"].blit(self.surf, (self.x, self.y))

