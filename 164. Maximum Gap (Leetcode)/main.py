class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        total = len(nums)
        if total == 1:
            return 0

        nums = sorted(nums)

        greatest = 0
        for i in range(total - 1):
            difference = abs(nums[i + 1] - nums[i])
            if difference > greatest:
                greatest = difference

        return greatest
