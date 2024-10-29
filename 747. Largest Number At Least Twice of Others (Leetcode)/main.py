class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        greatest = max(nums)
        index = nums.index(greatest)
        nums.remove(greatest)
        second = max(nums)
        if greatest >= 2*second:
            return index
        return -1