from src.states.BaseState import BaseState
from src.GameLevel import GameLevel
from src.AssetManager import *
from src.Tilemap import Tilemap
from src.LevelGenerator import LevelGenerator
from src.Camera import Camera



class PlayState(BaseState):
    def __init__(self):
        self.levelGenerator = LevelGenerator
        self.level = GameLevel(
            tilemaps = [
                Tilemap(self.levelGenerator.generate_empty_grassland(
                tileset=gFrames["tileset"],
                width=LEVEL_WIDTH,
                height=LEVEL_HEIGHT
            )
            )],
            entities = [],
            objects = []
        )


        self.camera = Camera(self.level.tilemaps[0], CANVAS_WIDTH, CANVAS_HEIGHT, 0, 0)




    def update(self, params):


        self.camera.update({
            "events":params["events"],
            "dt":params["dt"],
        })

        
        
        self.level.update({
            "dt":params["dt"],
            "events":params["events"]
        })

    def render(self, params):

        

        self.level.render({
            "canvas":params["canvas"],
            "xOffset":self.camera.get_X_offset(),
            "yOffset":self.camera.get_Y_offset()

        })

