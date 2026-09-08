from src.states.BaseState import BaseState
from src.GameLevel import GameLevel
from src.AssetManager import *
from src.Tilemap import Tilemap
from src.LevelGenerator import LevelGenerator
from src.Camera import Camera
from src.Player import Player



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

        self.player = Player(0, 0, self.level.tilemaps[0])

        self.camera = Camera(self.level.tilemaps[0], CANVAS_WIDTH, CANVAS_HEIGHT)




    def update(self, params):

        self.player.update(params)

        self.camera.update({
            "events":params["events"],
            "dt":params["dt"],
            "x":self.player.x,
            "y":self.player.y

        })

        
        
        self.level.update({
            "dt":params["dt"],
            "events":params["events"]
        })

    def render(self, params):

        self.level.render(params)

        self.player.render(params)
