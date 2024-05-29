class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        product = nums[0]
        for i in range(1,len(nums)):
            product *= nums[i]
        if product >0:
            return 1
        else:
            return -1