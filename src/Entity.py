
class Entity:
    def __init__(self, params):


        self.x = params["x"]
        self.y = params["y"]

        self.dx = 0
        self.dy = 0

        self.width = params["width"]
        self.height = params["height"]

        self.texture = params["texture"]
        self.frame = 0
        self.stateMachine = params["stateMachine"]

        self.direction = "up"
        self.map = params["map"]


    def update(self, params):
        self.stateMachine.update({
            "dt":params["dt"],
            "events":params["events"]
        })

    def render(self, params):
        params["canvas"].blit(self.texture[self.frame], (self.x, self.y))



        