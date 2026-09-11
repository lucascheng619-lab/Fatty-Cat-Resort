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

                

                if tile.type == "grass":
                    if bottomCentre != None:
                        if bottomCentre.type == "dirt":
                            tile.ID = UPPER_DIRT_EDGE_ID

                    if middleRight != None:
                        if middleRight.type == "dirt":
                            tile.ID = LEFT_DIRT_EDGE_ID

                    if middleLeft != None:
                        if middleLeft.type == "dirt":
                            tile.ID = RIGHT_DIRT_EDGE_ID

                    if topCentre != None:
                        if topCentre.type == "dirt":
                            tile.ID = BOTTOM_DIRT_EDGE_ID

                    if topCentre != None and middleLeft != None: #checks if needs top left 
                        if topCentre.type == "dirt" and middleLeft.type == "dirt":
                            tile.ID = TOP_LEFT_DIRT_EDGE_ID

                    if topCentre != None and middleRight != None:
                        if topCentre.type == "dirt" and middleRight.type == "dirt":
                            tile.ID = TOP_RIGHT_DIRT_EDGE_ID

                    if bottomCentre != None and middleRight != None:
                        if bottomCentre.type == "dirt" and middleRight.type == "dirt":
                            tile.ID = BOTTOM_RIGHT_DIRT_EDGE_ID

                    if bottomCentre != None and middleLeft != None:
                                            if bottomCentre.type == "dirt" and middleLeft.type == "dirt":
                                                tile.ID = BOTTOM_LEFT_DIRT_EDGE_ID


                    #if the tile above is dirt and the tile below is dirt, make this tile also dirt
                    if topCentre != None and bottomCentre != None:
                        if topCentre.type == "dirt" and bottomCentre.type == "dirt":
                            tile.type = "dirt"

                    if middleRight != None and middleLeft != None:
                        if middleRight.type == "dirt" and middleLeft.type == "dirt":
                            tile.type = "dirt"

                    

                    

                


                

                tile.update(params)

    def render(self, params):
        for row in self.tilemap:
            for tile in row:
                tile.render(params)

        