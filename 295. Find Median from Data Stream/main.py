class MedianFinder:

    def __init__(self):
        self.list = []
        self.length = 0

    def addNum(self, num: int) -> None:
        self.list.append(num)
        self.length += 1

    def findMedian(self) -> float:
        self.list = sorted(self.list)
        if self.length % 2 == 0:
            return (self.list[self.length // 2] + self.list[(self.length // 2) - 1]) / 2
        else:
            return self.list[self.length // 2]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
