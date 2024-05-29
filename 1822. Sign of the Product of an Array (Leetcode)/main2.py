class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = nums[0]
        for i in range(1,len(nums)):
            product *= nums[i]
        if product >0:
            return 1
        elif product == 0:
            return 0
        else:
            return -1

    