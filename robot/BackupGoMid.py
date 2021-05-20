import math

class lackOfProgress:

    def isLackOfProgress(self,ballpos): 
        TIME_STEP = 64
        progress_check_steps = math.ceil(10/(TIME_STEP/1000.0)) 
        progress_check_threshold = 0.4

        self.steps = progress_check_steps
        self.threshold = progress_check_threshold
        self.samples = [0 for x in range(self.steps)]
        self.iterator = 0
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
