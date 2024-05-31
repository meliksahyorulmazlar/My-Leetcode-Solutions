class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        x = sorted(nums)
        print(x)
        if x[-1] >= 2* x[-2]:
            print(nums)
        else:
            return -1

