class MinStack:

    def __init__(self):
        self.list = []

    def push(self, val: int) -> None:
        self.list.append(val)

    def pop(self) -> None:
        return self.list.pop()

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return min(self.list)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
