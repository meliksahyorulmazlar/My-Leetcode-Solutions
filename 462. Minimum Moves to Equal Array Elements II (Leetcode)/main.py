class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        if length % 2 == 0:
            median = (nums[length // 2] + nums[(length // 2) - 1]) // 2
        else:
            median = nums[length // 2]

        count = 0
        for num in nums:
            count += abs(num - median)
        return count
