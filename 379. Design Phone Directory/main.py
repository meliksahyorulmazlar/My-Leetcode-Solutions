class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.nums = [-1 for n in range(maxNumbers)]

    def get(self) -> int:
        for i in range(len(self.nums)):
            num = self.nums[i]
            if num == -1:
                self.nums[i] = i
                return i
        return -1

    def check(self, number: int) -> bool:
        if self.nums[number] == -1:
            return True
        else:
            return False

    def release(self, number: int) -> None:
        self.nums[number] = -1
        return None

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)