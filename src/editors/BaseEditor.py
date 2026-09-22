

class BaseEditor:
    def __init__(self):
        pass

    def enter(self, params):
        pass

    def exit(self):
        pass

    def changeBrush(self, brush):
        self.currentBrush = brush

    def update(self, params):
        pass

    def render(self, params):
        pass