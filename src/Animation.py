

class Animation:
    def __init__(self, frames, interval):
        self.frames = frames # list of frames
        self.interval = interval #in seconds
        self.timer = 0
        self.currentFrame = 0

    def update(self, params):
        self.timer += params["dt"]
        if self.timer > self.interval:
            #change frame
            self.timer = self.timer % self.interval
            self.currentFrame += 1
            
            if self.currentFrame >= len(self.frames): #loop back if it overflows
                self.currentFrame = 0

            



    def getFrame(self):
        if self.currentFrame >= len(self.frames): #loop back if it overflows
            self.currentFrame = 0

        return self.frames[self.currentFrame]
    