

class GameLevel:
    def __init__(self, tilemaps, entities, objects):
        self.tilemaps = tilemaps
        self.entities = entities
        self.objects = objects

    def update(self, params):
        for tilemap in self.tilemaps:
            tilemap.update(params)

        for entity in self.entities:
            entity.render({
                "dt":params["dt"],
                "events":params["events"],
                "map":self.tilemap[0] #should be changed later
            })

        for object in self.objects:
            object.render({
                "dt":params["dt"],
                "events":params["events"],
                "map":self.tilemap[0] #should be changed later
            })

    def render(self, params):
        for tilemap in self.tilemaps:
            tilemap.render({
                "canvas":params["canvas"]
            })

        for entity in self.entities:
            entity.render({
                "canvas":params["canvas"]
            })

        for object in self.objects:
            object.render({
                "canvas":params["canvas"]
            })