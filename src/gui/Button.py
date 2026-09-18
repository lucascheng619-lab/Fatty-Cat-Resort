import pygame

class Button:
    def __init__(self, ID, x, y, texture, pressedTexture):
        self.ID = ID

        self.x = x
        self.y = y
        self.texture = texture
        self.pressedTexture = pressedTexture
        self.pressed = False
        self.rect = self.texture.get_rect()

        self.width = texture.get_width()
        self.height = texture.get_height()

    def update(self, params):
        pass

    def checkHovering(self, params):
        
        return self.rect.collidepoint((params["cursorX"],params["cursorY"]))


    def checkPressed(self, params):

        for event in params["events"]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.rect.collidepoint((params["cursorX"],params["cursorY"])):
                    
                    return True

        return False

    def render(self, params):
        self.rect.topleft = (self.x, self.y)

        if self.pressed:
            params["canvas"].blit(self.pressedTexture, self.rect)
        else:
            params["canvas"].blit(self.texture, self.rect)