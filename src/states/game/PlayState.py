from src.states.BaseState import BaseState
from src.GameLevel import GameLevel
from src.AssetManager import *
from src.Tilemap import Tilemap
from src.LevelGenerator import LevelGenerator
from src.Camera import Camera
from src.Cursor import Cursor
from src.Focus import Focus
from src.TerrainEditor import TerrainEditor

from src.Editor import Editor
import pygame



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

        self.cursor = Cursor(gTextures["cursor"],gTextures["cursor_shadow"])


        self.editor = Editor({
            "terrain":lambda:TerrainEditor()
        })
        
        self.editor.changeEditor("terrain",{
            "focus":Focus(gTextures["tile_focus"]),
            "tilemap":self.level.tilemaps[0]
        })

        self.editor.changeBrush("dirt")



        self.camera = Camera(self.level.tilemaps[0], CANVAS_WIDTH, CANVAS_HEIGHT, 0, 0)

        self.editor.changeBrush("dirt")





    def update(self, params):


        self.camera.update({
            "events":params["events"],
            "dt":params["dt"],
        })


        self.cursor.update({
            "dt":params["dt"],
            "events":params["events"]
        })

        self.editor.update({
            "dt":params["dt"],
            "events":params["events"],
            "cursorX":self.cursor.x,
            "cursorY":self.cursor.y,
            "cameraX":self.camera.get_X_offset(),
            "cameraY":self.camera.get_Y_offset()
        })

        self.level.update({
            "dt":params["dt"],
            "events":params["events"],
            "xOffset":self.camera.get_X_offset(),
            "yOffset":self.camera.get_Y_offset()    
            
        })

        

    def render(self, params):

        

        self.level.render({
            "canvas":params["canvas"],
            "xOffset":self.camera.get_X_offset(),
            "yOffset":self.camera.get_Y_offset()

        })

        self.editor.render({
            "canvas":params["canvas"],
            "xOffset":self.camera.get_X_offset(),
            "yOffset":self.camera.get_Y_offset()
        })

        self.cursor.render({
            "canvas":params["canvas"],
            "xOffset":self.camera.get_X_offset(),
            "yOffset":self.camera.get_Y_offset()
        })

