from src.states.BaseState import BaseState
from src.GameLevel import GameLevel
from src.AssetManager import *
from src.Tilemap import Tilemap
from src.LevelGenerator import LevelGenerator

class PlayState(BaseState):
    def __init__(self):
        self.levelGenerator = LevelGenerator
        self.level = GameLevel(
            tilemap = Tilemap(self.levelGenerator.generate_empty_grassland(
                tileset=gFrames["tileset"],
                width=LEVEL_WIDTH,
                height=LEVEL_HEIGHT
            )),
            entities = [],
            objects = []
        )



    def update(self, params):
        
        self.level.update(params)

    def render(self, params):
        self.level.render(params)