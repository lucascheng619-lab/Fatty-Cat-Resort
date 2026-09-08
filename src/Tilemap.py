

class Tilemap:
    def __init__(self, tilemap):
        self.tilemap = tilemap

    def update(self, params):
        pass

    def render(self, params):
        for row in self.tilemap:
            for tile in row:
                tile.render(params)

        