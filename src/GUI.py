

class GUI:
    def __init__(self, elements):
        self.elements = elements

    def update(self, params):
        for element in self.elements:
            element.update(params)

    def render(self, params):
        for element in self.elements:
            element.render(params)