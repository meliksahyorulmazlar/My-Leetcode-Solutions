class CustomStack:

    def __init__(self, maxSize: int):
        self.list = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.list) < self.size:
            self.list.append(x)

    def pop(self) -> int:
        if len(self.list) == 0:
            return -1
        else:
            return self.list.pop()

    def increment(self, k: int, val: int) -> None:
        length = len(self.list)
        if length < k:
            for i in range(len(self.list)):
                self.list[i] += val
        else:
            for i in range(k):
                self.list[i] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)