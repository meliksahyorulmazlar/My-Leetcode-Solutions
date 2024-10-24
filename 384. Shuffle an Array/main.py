class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums = self.original
        return self.nums

    def shuffle(self) -> List[int]:
        # shuffled = nums: shuffled is just a new name for nums, so they both refer to the same list.
        #shuffled = nums[:]: shuffled is a new list that is a shallow copy of nums, so changes to one list won't affect the other.
        shuffled = self.nums[:]
        for i in range(len(shuffled) - 1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()