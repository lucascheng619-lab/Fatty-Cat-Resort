from src.constants import *
import pygame


class Camera:
    def __init__(self, tilemap, viewWidth, viewHeight, x, y):
        self.mapWidth = tilemap.width * TILE_WIDTH
        self.mapHeight = tilemap.height * TILE_HEIGHT
        self.viewWidth = viewWidth
        self.viewHeight = viewHeight
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def update(self, params):

        self.dx = 0
        self.dy = 0

        keys = pygame.key.get_pressed()

        #checks arrow keys

        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]: #checks if the up key is pressed and makes sure the down key is not pressed
            self.dy = -CAMERA_SPEED
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]: #checks if the down key is pressed and makes sure the up key is not being pressed
            self.dy = CAMERA_SPEED

        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]: #checks if the left key is pressed and makes sure the right key is not being pressed
            self.dx = -CAMERA_SPEED
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]: #checks if the right key is pressed and makes sure the left key is not being pressed
            self.dx = CAMERA_SPEED

        #checks wasd

        if keys[pygame.K_w] and not keys[pygame.K_s]: #checks if the w key is pressed and makes sure the s key is not being pressed
            self.dy = -CAMERA_SPEED
        elif keys[pygame.K_s] and not keys[pygame.K_w]: #checks if the s key is pressed and makes sure the w key is not being pressed
            self.dy = CAMERA_SPEED
        
        if keys[pygame.K_a] and not keys[pygame.K_d]: #checks if the a key is pressed and makes sure the d key is not being pressed
            self.dx = -CAMERA_SPEED
        elif keys[pygame.K_d] and not keys[pygame.K_a]: #checks if the d key is pressed and makes sure the a key is not being pressed
            self.dx = CAMERA_SPEED

        self.x += (self.dx * params["dt"])
        self.y += (self.dy * params["dt"])

        self.x = max(0, min(self.mapWidth - self.viewWidth, self.x))
        self.y = max(0, min(self.mapHeight - self.viewHeight, self.y))


    def get_X_offset(self):
        return round(self.x)

    def get_Y_offset(self):
        return round(self.y)