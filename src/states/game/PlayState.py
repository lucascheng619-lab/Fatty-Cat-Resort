from src.states.BaseState import BaseState
from src.GameLevel import GameLevel
from src.AssetManager import *
from src.Tilemap import Tilemap
from src.LevelGenerator import LevelGenerator
from src.Camera import Camera
from src.Cursor import Cursor
from src.Focus import Focus


from src.editors.TerrainEditor import TerrainEditor
from src.editors.SelectEditor import SelectEditor

from src.GUI import GUI
from src.gui.Button import Button

from src.Editor import Editor
import pygame



class PlayState(BaseState):
    def __init__(self):

        self.levelGenerator = LevelGenerator
        self.level = GameLevel(
            tilemap = 
                Tilemap(self.levelGenerator.generate_empty_grassland(
                tileset=gFrames["tileset"],
                width=LEVEL_WIDTH,
                height=LEVEL_HEIGHT
            )
            ),
            entities = [],
            objects = []
        )


        self.gui = GUI([
            Button("select_editor_button",10, 50, gTextures["select_editor_button"], gTextures["select_editor_button_selected"]), #cursor select button
            Button("terrain_editor_button",10, 65, gTextures["terrain_editor_button"], gTextures["terrain_editor_button_selected"])

            ])

        
        self.cursor = Cursor()


        self.editor = Editor(self.gui, self.level,{
            "select":lambda:SelectEditor(),
            "terrain":lambda:TerrainEditor()
        })
        
        self.editor.changeEditor("terrain")

        self.editor.changeBrush("dirt")

        



        self.camera = Camera(self.level.tilemap, CANVAS_WIDTH, CANVAS_HEIGHT, 0, 0)

        self.editor.changeBrush("dirt")





    def update(self, params):


        self.camera.update({
            "events":params["events"],
            "dt":params["dt"],
        })


        self.cursor.update({
            "dt":params["dt"],
            "events":params["events"],
            "editor":self.editor.currentEditor
        })

        self.gui.update({
            "dt":params["dt"],
            "events":params["events"],
            "cursorX":self.cursor.x,
            "cursorY":self.cursor.y,
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

        self.gui.render({
            "canvas":params["canvas"]
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

