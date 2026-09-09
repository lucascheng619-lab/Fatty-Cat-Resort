

class Tile:
    def __init__(self, texture, ID, x, y):
        self.texture = texture
        self.frame = texture[ID]

        self.x = x
        self.y = y
        

    def render(self, params):

        params["canvas"].blit(self.frame, (self.x - params["xOffset"], self.y - params["yOffset"]))