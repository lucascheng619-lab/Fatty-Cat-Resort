

class GameLevel:
    def __init__(self, tilemap, entities, objects):
        self.tilemap = tilemap
        self.entities = entities
        self.objects = objects

    def update(self, params):
        self.tilemap.update()

        for entity in self.entities:
            entity.render({
                "dt":params["dt"],
                "events":params["events"],
                "map":self.tilemap
            })

        for object in self.objects:
            object.render({
                "dt":params["dt"],
                "events":params["events"],
                "map":self.tilemap
            })

    def render(self, params):
        self.tilemap.render({
            "canvas":params["canvas"],
        })

        for entity in self.entities:
            entity.render({
                "canvas":params["canvas"]
            })

        for object in self.objects:
            object.render({
                "canvas":params["canvas"]
            })