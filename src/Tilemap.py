from src.constants import *

class Tilemap:
    def __init__(self, tilemap):
        self.tilemap = tilemap
        self.width = len(self.tilemap[0])
        self.height = len(self.tilemap)

    def update(self, params):

        for row in self.tilemap:
            for tile in row:
                
                if tile.type == "grass":
                    tile.ID = PLAIN_GRASS_ID
        
                elif tile.type == "dirt":
                    tile.ID = PLAIN_DIRT_ID
        
        for row in self.tilemap: #changes tile IDs depending on the types of surrounding 
            for tile in row:
                y = self.tilemap.index(row)
                x = row.index(tile)

                if x != 0:
                    middleLeft = self.tilemap[y][x - 1]
                else:
                    middleLeft = None
                
                if x != self.width - 1:
                    middleRight = self.tilemap[y][x + 1]
                else:
                    middleRight = None

                if y != self.width - 1: #checks that it is not the bottom row, if it is bottom row assign none to bottomLeft, bottomCentre, bottomRight
                    bottomCentre = self.tilemap[y + 1][x]
                    if x != 0:
                        bottomLeft = self.tilemap[y + 1][x - 1]
                    else:
                        bottomLeft = None
                
                    if x != self.width - 1:
                        bottomRight = self.tilemap[y + 1][x + 1]
                    else:
                        bottomRight = None

                else:
                    bottomLeft = None
                    bottomCentre = None
                    bottomRight = None 

                    

                if y != 0: #checks that it is not the top row, if it is top row assign none to topLeft, topCentre, topRight
                    topCentre = self.tilemap[y - 1][x]
                    if x != 0:
                        topLeft = self.tilemap[y - 1][x - 1]
                    else:
                        topLeft = None

                    if x != self.width - 1:
                        topRight = self.tilemap[y - 1][x + 1]
                    else:
                        topRight = None

                else:
                    topLeft = None
                    topCentre = None
                    topRight = None
                


                

                tile.update(params)

    def render(self, params):
        for row in self.tilemap:
            for tile in row:
                tile.render(params)

        