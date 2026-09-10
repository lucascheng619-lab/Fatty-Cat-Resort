from src.states.BaseState import BaseState
from src.GameLevel import GameLevel
from src.AssetManager import *
from src.Tilemap import Tilemap
from src.LevelGenerator import LevelGenerator
from src.Camera import Camera
from src.Cursor import Cursor
from src.Focus import Focus
from src.TerrainEditor import TerrainEditor
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

        self.terrainEditor = TerrainEditor(Focus(gTextures["tile_focus"]), self.level.tilemaps[0]) #tilemap 0 means its editing the lowest tilemap which is the terrain

        self.camera = Camera(self.level.tilemaps[0], CANVAS_WIDTH, CANVAS_HEIGHT, 0, 0)

        self.terrainEditor.changeBrush("dirt")




    def update(self, params):


        self.camera.update({
            "events":params["events"],
            "dt":params["dt"],
        })


        self.cursor.update({
            "dt":params["dt"],
            "events":params["events"]
        })

        self.terrainEditor.update({
            "dt":params["dt"],
            "events":params["events"],
            "cursorX":self.cursor.x,
            "cursorY":self.cursor.y,
            "cameraX":self.camera.get_X_offset(),
            "cameraY":self.camera.get_Y_offset()
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

        self.terrainEditor.render({
            "canvas":params["canvas"],
            "xOffset":self.camera.get_X_offset(),
            "yOffset":self.camera.get_Y_offset()
        })

        self.cursor.render({
            "canvas":params["canvas"],
            "xOffset":self.camera.get_X_offset(),
            "yOffset":self.camera.get_Y_offset()
        })

