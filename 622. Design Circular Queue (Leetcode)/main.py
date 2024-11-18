class MyCircularQueue:

    def __init__(self, k: int):
        self.list = []
        self.length = k

    def enQueue(self, value: int) -> bool:
        if len(self.list) < self.length:
            self.list.append(value)
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.list:
            self.list.pop(0)
            return True
        else:
            return False

    def Front(self) -> int:
        if self.list:
            return self.list[0]
        else:
            return -1

    def Rear(self) -> int:
        if self.list:
            return self.list[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.list:
            return False
        else:
            return True

    def isFull(self) -> bool:
        return self.length == len(self.list)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()