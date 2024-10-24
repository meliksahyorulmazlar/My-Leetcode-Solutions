class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero_range = range(0, nums.count(0))
        index = nums.count(0)
        one_range = range(index, nums.count(1) + index)
        index += nums.count(1)
        two_range = range(index, nums.count(2) + index)
        for i in zero_range:
            nums[i] = 0

        for j in one_range:
            nums[j] = 1

        for k in two_range:
            nums[k] = 2  