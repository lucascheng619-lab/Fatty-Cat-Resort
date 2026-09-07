

class Tile:
    def __init__(self, texture, x, y):
        self.texture = texture

        self.x = x
        self.y = y

    def render(params):
        params["canvas"].blit(self.texture, self.x, self.y)