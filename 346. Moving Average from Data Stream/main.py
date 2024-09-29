class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.list = []

    def isFull(self):
        if len(self.list) == self.size:
            return True
        return False

    def next(self, val: int) -> float:
        if self.isFull():
            self.list.pop(0)
            self.list.append(val)
            return sum(self.list) / self.size
        else:
            self.list.append(val)
            return sum(self.list) / (len(self.list))