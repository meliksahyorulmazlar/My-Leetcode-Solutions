class MRUQueue:

    def __init__(self, n: int):
        self.nums = [i for i in range(1, n + 1)]

    def fetch(self, k: int) -> int:
        number = self.nums[k - 1]
        self.nums.pop(k - 1)
        self.nums.append(number)

        return number

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
