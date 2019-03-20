import math
class EqualWidthPartitioning:
    min = 0
    max = 0
    n = 0
    width = 0

    def __init__(self, list, n):
        list = sorted(list)
        self.min = list[0]
        self.max = list[len(list)-1]
        self.width = (self.max - self.min) / n

    def bining(self, value):
        if value <= self.min:
            return 0
        if value > self.max:
            return self.n - 1
        x = math.ceil((value - self.min)/self.width)
        return x
