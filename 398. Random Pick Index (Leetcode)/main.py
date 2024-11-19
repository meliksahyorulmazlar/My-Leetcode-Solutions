import random
class Solution:

    def __init__(self, nums: List[int]):
        self.dictionary = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in self.dictionary:
                self.dictionary[num] = [i]
            else:
                self.dictionary[num].append(i)

    def pick(self, target: int) -> int:
        indices = self.dictionary[target]
        return random.choice(indices)


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)