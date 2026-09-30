from src.constants import *
from src.LevelGenerator import LevelGenerator
from src.AssetManager import *

class Tilemap:
    def __init__(self, tilemap):
        self.tilemap = tilemap
        self.width = len(self.tilemap[0])
        self.height = len(self.tilemap)
        self.visibleTilemap = []
        self.visibleWaterTilemap = []

        self.levelGenerator = LevelGenerator
        self.waterTilemap = self.levelGenerator.generate_water(gFrames["tileset"], self.width, self.height)

    def getSurroundingTiles(self, tileX, tileY, tilemap):
        surroundingTiles = {}
        if tileY != 0: #checks that it is not the top row, if it is top row assign none to topLeft, topCentre, topRight
            surroundingTiles["topCentre"] = tilemap[tileY - 1][tileX]
            if tileX != 0:
                surroundingTiles["topLeft"] = tilemap[tileY - 1][tileX - 1]

            if tileX != self.visibleColomns - 1:
                surroundingTiles["topRight"] = tilemap[tileY - 1][tileX + 1]

        if tileX != 0:
            surroundingTiles["middleLeft"] = tilemap[tileY][tileX - 1]

        
        if tileX != self.visibleColomns - 1:
            surroundingTiles["middleRight"] = tilemap[tileY][tileX + 1]


        if tileY != self.visibleRows - 1: #checks that it is not the bottom row, if it is bottom row assign none to bottomLeft, bottomCentre, bottomRight
            surroundingTiles["bottomCentre"] = tilemap[tileY + 1][tileX]
            if tileX != 0:
                surroundingTiles["bottomLeft"] = tilemap[tileY + 1][tileX - 1]

        
            if tileX != self.visibleColomns - 1:
                surroundingTiles["bottomRight"] = tilemap[tileY + 1][tileX + 1]


        return surroundingTiles



    def getVisibleTilemap(self, tilemap, xOffset, yOffset):
        visibleTilemap = []

        
        self.visibleColomns = CANVAS_WIDTH // TILE_WIDTH +4#x columns visible + adds 4 extra colomns 2 infront 2 behind
        self.visibleRows = CANVAS_HEIGHT // TILE_HEIGHT +4#y colomns visible + adds 4 extra rows 2 
        self.firstVisibleColomn = max(0,min(xOffset // TILE_WIDTH - 2, self.width - self.visibleColomns)) #shifts first visible rows backwards by two so that the actually first rows we can see are in front of those first rows being updated
        self.firstVisibleRow = max(0, min(yOffset // TILE_HEIGHT - 2, self.height - self.visibleRows))#shift 



        y = 0


        for row in tilemap[self.firstVisibleRow:self.firstVisibleRow + self.visibleRows]:
            visibleTilemap.append([])
            
            for column in range(len(row[self.firstVisibleColomn:self.firstVisibleColomn + self.visibleColomns])):
                visibleTilemap[y].append(tilemap[y + self.firstVisibleRow][column + self.firstVisibleColomn])
            

            y += 1

        

        return visibleTilemap


    def adjustWaterTiles(self, tilemap):
        adjustedTilemap = tilemap
        for row in adjustedTilemap:
            for tile in row:
                y = adjustedTilemap.index(row)
                x = row.index(tile)
                
                surroundingTiles = self.getSurroundingTiles(x, y, adjustedTilemap)
                if tile.type == "grass":
                    if "middleRight" in surroundingTiles:
                        if surroundingTiles["middleRight"].type == "water":
                            tile.ID = RIGHT_CLIFF_EDGE_ID
                            tile.editable = False

                    if "middleLeft" in surroundingTiles:
                        if surroundingTiles["middleLeft"].type == "water":
                            tile.ID = LEFT_CLIFF_EDGE_ID
                            tile.editable = False

                    if "topCentre" in surroundingTiles:
                        if surroundingTiles["topCentre"].type == "water":
                            tile.ID = UPPER_CLIFF_EDGE_ID
                            tile.editable = False

                    if "bottomCentre" in surroundingTiles:
                        if surroundingTiles["bottomCentre"].type == "water":
                            tile.ID = SUBMERGED_BOTTOM_CLIFF_EDGE_ID
                            tile.editable = False


                    if "topCentre" in surroundingTiles and "middleLeft" in surroundingTiles: #checks if needs top left 
                        if surroundingTiles["topCentre"].type == "water" and surroundingTiles["middleLeft"].type == "water":
                            tile.ID = TOP_LEFT_CLIFF_CORNER_ID
                            tile.editable = False

                    if "topCentre" in surroundingTiles and "middleRight" in surroundingTiles:
                        if surroundingTiles["topCentre"].type == "water" and surroundingTiles["middleRight"].type == "water":
                            tile.ID = TOP_RIGHT_CLIFF_CORNER_ID
                            tile.editable = False

        return adjustedTilemap

                

    def adjustDirtTiles(self, tilemap):
        adjustedTilemap = tilemap

        for row in adjustedTilemap:
            for tile in row:
                
                if tile.type == "grass":
                    tile.ID = PLAIN_GRASS_ID
        
                elif tile.type == "dirt":
                    tile.ID = PLAIN_DIRT_ID

        
        for row in adjustedTilemap: #changes tile IDs depending on the types of surrounding 
            for tile in row:
                y = adjustedTilemap.index(row)
                x = row.index(tile)

                surroundingTiles = self.getSurroundingTiles(x, y, adjustedTilemap)

                if tile.type == "grass":
                    if "topCentre" in surroundingTiles and "bottomCentre" in surroundingTiles:
                        if surroundingTiles["topCentre"].type == "dirt" and surroundingTiles["bottomCentre"].type == "dirt":
                            tile.type = "dirt"

                    if "middleRight" in surroundingTiles and "middleLeft" in surroundingTiles:
                        if surroundingTiles["middleRight"].type == "dirt" and surroundingTiles["middleLeft"].type == "dirt":
                            tile.type = "dirt"




                if tile.type == "dirt":
                    if "bottomCentre" in surroundingTiles and "middleRight" in surroundingTiles:
                        if surroundingTiles["bottomCentre"].type == "dirt" and surroundingTiles["middleRight"].type == "dirt":
                            if "topCentre" in surroundingTiles and "middleLeft" in surroundingTiles:
                                if surroundingTiles["topCentre"].type == "grass" and surroundingTiles["middleLeft"].type == "grass":
                                    tile.ID = TOP_LEFT_DIRT_CORNER_ID
                            else:
                                tile.ID = TOP_LEFT_DIRT_CORNER_ID

                            
                    if "bottomCentre" in surroundingTiles and "middleLeft" in surroundingTiles:
                        if surroundingTiles["bottomCentre"].type == "dirt" and surroundingTiles["middleLeft"].type == "dirt":
                            if "topCentre" in surroundingTiles and "middleRight" in surroundingTiles:
                                if surroundingTiles["topCentre"].type == "grass" and surroundingTiles["middleRight"].type == "grass":
                                    tile.ID = TOP_RIGHT_DIRT_CORNER_ID
                            else:
                                tile.ID = TOP_RIGHT_DIRT_CORNER_ID

                    if "topCentre" in surroundingTiles and "middleRight" in surroundingTiles:
                        if surroundingTiles["topCentre"].type == "dirt" and surroundingTiles["middleRight"].type == "dirt":
                            if "bottomCentre" in surroundingTiles and "middleLeft" in surroundingTiles:
                                if surroundingTiles["bottomCentre"].type == "grass" and surroundingTiles["middleLeft"].type == "grass":
                                    tile.ID = BOTTOM_LEFT_DIRT_CORNER_ID
                            else:
                                tile.ID = BOTTOM_LEFT_DIRT_CORNER_ID

                    if "topCentre" in surroundingTiles and "middleLeft" in surroundingTiles:
                        if surroundingTiles["topCentre"].type == "dirt" and surroundingTiles["middleLeft"].type == "dirt":
                            if "bottomCentre" in surroundingTiles and "middleRight" in surroundingTiles:
                                if surroundingTiles["bottomCentre"].type == "grass" and surroundingTiles["middleRight"].type == "grass":
                                    tile.ID = BOTTOM_RIGHT_DIRT_CORNER_ID
                            else:
                                tile.ID = BOTTOM_RIGHT_DIRT_CORNER_ID

                    
                    if x == 0 or x == self.visibleColomns - 1:
                        tile.ID = PLAIN_DIRT_ID
                    if y == 0 or y == self.visibleRows - 1:
                        tile.ID = PLAIN_DIRT_ID


        for row in adjustedTilemap: #changes tile IDs depending on the types of surrounding 
            for tile in row:
                y = adjustedTilemap.index(row)
                x = row.index(tile)


                surroundingTiles = self.getSurroundingTiles(x, y, adjustedTilemap)

         

                if tile.type == "grass":
                    if "bottomCentre" in surroundingTiles:
                        if surroundingTiles["bottomCentre"].ID == PLAIN_DIRT_ID:
                            tile.ID = UPPER_DIRT_EDGE_ID

                    if "middleRight" in surroundingTiles:
                        if surroundingTiles["middleRight"].ID == PLAIN_DIRT_ID:
                            tile.ID = LEFT_DIRT_EDGE_ID

                    if "middleLeft" in surroundingTiles:
                        if surroundingTiles["middleLeft"].ID == PLAIN_DIRT_ID:
                            tile.ID = RIGHT_DIRT_EDGE_ID

                    if "topCentre" in surroundingTiles:
                        if surroundingTiles["topCentre"].ID == PLAIN_DIRT_ID:
                            tile.ID = BOTTOM_DIRT_EDGE_ID

                    if "topCentre" in surroundingTiles and "middleLeft" in surroundingTiles: #checks if needs top left 
                        if surroundingTiles["topCentre"].ID == PLAIN_DIRT_ID and surroundingTiles["middleLeft"].ID == PLAIN_DIRT_ID:
                            tile.ID = TOP_LEFT_DIRT_EDGE_ID

                    if "topCentre" in surroundingTiles and "middleRight" in surroundingTiles:
                        if surroundingTiles["topCentre"].ID == PLAIN_DIRT_ID and surroundingTiles["middleRight"].ID == PLAIN_DIRT_ID:
                            tile.ID = TOP_RIGHT_DIRT_EDGE_ID

                    if "bottomCentre" in surroundingTiles and "middleRight" in surroundingTiles:
                        if surroundingTiles["bottomCentre"].ID == PLAIN_DIRT_ID and surroundingTiles["middleRight"].ID == PLAIN_DIRT_ID:
                            tile.ID = BOTTOM_RIGHT_DIRT_EDGE_ID

                    if "bottomCentre" in surroundingTiles and "middleLeft" in surroundingTiles:
                        if surroundingTiles["bottomCentre"].ID == PLAIN_DIRT_ID and surroundingTiles["middleLeft"].ID == PLAIN_DIRT_ID:
                            tile.ID = BOTTOM_LEFT_DIRT_EDGE_ID

        return adjustedTilemap

    def emptyWaterTiles(self, tilemap):
        updatedTilemap = tilemap
        for row in updatedTilemap:
            for tile in row:
                if tile.type == "water":
                    tile.ID = EMPTY_ID

        return updatedTilemap


    def update(self, params):
        self.visibleTilemap = self.getVisibleTilemap(self.tilemap, params["xOffset"], params["yOffset"])
        self.visibleTilemap = self.emptyWaterTiles(self.visibleTilemap)

        self.visibleTilemap = self.adjustDirtTiles(self.visibleTilemap)
        self.visibleTilemap = self.adjustWaterTiles(self.visibleTilemap) #make sure that adjust water tiles is always after adjust Dirt Tiles


        self.visibleWaterTilemap = self.getVisibleTilemap(self.waterTilemap, params["xOffset"], params["yOffset"])

        for row in self.visibleTilemap:
            for tile in row:
                tile.update(params)

        for row in self.visibleWaterTilemap:
            for tile in row:
                if tile.type == "water":
                    tile.ID = WATER_ID

                tile.update(params)
        


    def render(self, params):
        for row in self.visibleWaterTilemap: #place the water tilemap under the land tilemap
            for tile in row:
                tile.render(params)
        
        for row in self.visibleTilemap:
            for tile in row:
                tile.render(params)

        