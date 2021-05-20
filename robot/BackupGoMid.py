import math

class lackOfProgress:
    def __init__(self,treshold,ball_pos) -> None:
        TIME_STEP = 64
        self.steps = math.ceil(10/(TIME_STEP/1000.0)) 
        self.threshold = treshold
        self.samples = [0 for x in range(self.steps)]
        self.iterator = 0
        self.prev_position = ball_pos[0]

    def isLackOfProgress(self,ballpos): 
        
        if not self.prev_position == None:
            self.prev_position = ballpos[1]

        change = math.sqrt((self.prev_position["x"] - ballpos["x"]) ** 2 +
                          (self.prev_position["y"] - ballpos["y"]) ** 2)

        self.samples[self.iterator % self.steps] = change
        self.iterator += 1
        self.prev_position = ballpos[0]

        changeSum = sum(self.samples)
        return (changeSum>=self.threshold)

    def midPos():
        mid_pos = {"x":0.6,"y":0.5}
        return mid_pos
