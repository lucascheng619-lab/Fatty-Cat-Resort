
class Camera:
    def __init__(self, tilemap, viewWidth, viewHeight):
        self.mapWidth = tilemap.width
        self.mapHeight = tilemap.height
        self.viewWidth = viewWidth
        self.viewHeight = viewHeight

    def update(self, params):

        self.x = max(0, min(params["x"], self.mapWidth - self.viewWidth))

        self.y = max(0, min(params["y"], self.mapHeight - self.mapHeight))

    def get_X_offset(self):
        return self.x

    def get_Y_offset(self):
        return self.y