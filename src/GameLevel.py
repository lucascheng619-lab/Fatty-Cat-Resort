

class GameLevel:
    def __init__(self, tilemap, entities, objects):
        self.tilemap = tilemap
        self.entities = entities
        self.objects = objects

    def update(self, params):
        self.tilemap.update({
            "dt":params["dt"],
            "events":params["events"],
            "xOffset":params["xOffset"],
            "yOffset":params["yOffset"]
            })


        for entity in self.entities:
            entity.update({
                "dt":params["dt"],
                "events":params["events"],
                "map":self.tilemap[0] #should be changed later
            })

        for object in self.objects:
            object.update({
                "dt":params["dt"],
                "events":params["events"],
                "map":self.tilemap[0] #should be changed later
            })

    def render(self, params):
        self.tilemap.render(params)

        for entity in self.entities:
            entity.render(params)

        for object in self.objects:
            object.render(params)