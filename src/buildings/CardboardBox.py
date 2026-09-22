from src.buildings.Accommodation import Accommodation
from src.AssetManager import *
from src.constants import *

class CardboardBox(Accommodation):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.texture = gTextures["single_cardboard_box"]
        self.tileWidth = self.texture.get_width() // TILE_WIDTH
        self.tileHeight = self.texture.get_height() // TILE_HEIGHT