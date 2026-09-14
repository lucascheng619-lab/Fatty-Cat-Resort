

class Editor:
    def __init__(self, editors):
        self.empty = type('Empty', (), {
                    "enter": lambda params=None: None,
                    "exit": lambda: None,
                    "update": lambda params=None: None,
                    "render": lambda params=None: None
                })
        self.editors = editors
        self.currentEditor = self.empty

    def changeEditor(self, editor, params):
        assert editor in self.editors, f"editor {editor} does not exist."
        self.currentEditor.exit()
        self.currentEditor = self.editors[editor]()
        self.currentEditor.enter(params)

    def changeBrush(self, brush):
        self.currentEditor.currentBrush = brush

    def update(self, params):
        self.currentEditor.update(params)

    def render(self, params):
        self.currentEditor.render(params)

