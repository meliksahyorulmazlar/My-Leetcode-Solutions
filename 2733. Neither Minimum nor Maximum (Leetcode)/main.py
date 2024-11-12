class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        for n in nums:
            if n != min(nums) and n!=max(nums):
                return n
        return -1