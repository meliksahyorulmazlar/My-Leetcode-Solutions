class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum([pow(nums[i],2) for i in range(0,len(nums)) if len(nums) % (i+1) == 0])