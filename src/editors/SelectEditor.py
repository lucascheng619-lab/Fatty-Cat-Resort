from src.AssetManager import *

from src.editors.BaseEditor import BaseEditor

class SelectEditor(BaseEditor):
    def __init__(self):
        self.ID = "select_editor"
        self.enabled = True
        self.cursorTexture = gTextures["cursor"]
        self.cursorShadowTexture = gTextures["cursor_shadow"]