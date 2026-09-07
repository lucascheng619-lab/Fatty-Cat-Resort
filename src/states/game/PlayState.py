from src.states.BaseState import BaseState
from src.GameLevel import GameLevel
from src.AssetManager import *

class PlayState(BaseState):
    def __init__(self):
        self.level = GameLevel(
            tilemap = [],
            entities = [],
            objects = []
        )

        print(len(gFrames["tileset"]))


    def update(self, params):
        pass
        #self.level.update(params)

    def render(self, params):
        pass
        #self.level.update(params)