class Skiplist:

    def __init__(self):
        self.list = []

    def search(self, target: int) -> bool:
        if target in self.list:
            return True
        return False

    def add(self, num: int) -> None:
        self.list.append(num)

    def erase(self, num: int) -> bool:
        if self.search(num):
            self.list.remove(num)
            return True
        return False

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
