

class Editor:
    def __init__(self, gui, level, editors):
        self.gui = gui
        self.empty = type('Empty', (), {
                    "enter": lambda params=None: None,
                    "exit": lambda: None,
                    "update": lambda params=None: None,
                    "render": lambda params=None: None
                })
        self.level = level
        self.editors = editors
        self.currentEditor = self.empty

    def changeEditor(self, editor):
        assert editor in self.editors, f"editor {editor} does not exist."
        self.currentEditor.exit()
        self.currentEditor = self.editors[editor]()
        self.currentEditor.enter({
            "level":self.level,
        })


    def changeBrush(self, brush):
        self.currentEditor.currentBrush = brush

    def update(self, params):
        self.currentEditor.enabled = True #always set this to true before the editor is updated, so that it always resets, if the editor is updated first then it won't detect if button on the editor are being hovered on


        for element in self.gui.elements:
            

            if element.checkHovering(params): #if the cursor is hovering above any gui disable the editor functionality
                self.currentEditor.enabled = False
            
            if element.ID == "select_editor_button": #select editor button
                element.pressed = False

                if element.checkPressed(params):#checks if the select editor button is being pressed
                    
                    self.changeEditor("select")
                if self.currentEditor.ID == "select_editor":
                    element.pressed = True
                
                
                

            if element.ID == "terrain_editor_button": #terrain editor button
                element.pressed = False

                if element.checkPressed(params):#checks if the terrain editor button is being pressed
                                                
                    self.changeEditor("terrain")
                    self.changeBrush("dirt")

                    
                if self.currentEditor.ID == "terrain_editor":
                    element.pressed = True

            if element.ID == "accommodation_editor_button": #accommodation editor button
                element.pressed = False

                if element.checkPressed(params):#checks if the terrain editor button is being pressed
                                                
                    self.changeEditor("accommodation")
                    self.changeBrush("cardboard_box")

                    

                    
                if self.currentEditor.ID == "accommodation_editor":
                    element.pressed = True
                
        

        self.currentEditor.update(params)
        
    def render(self, params):
        self.currentEditor.render(params)

