class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        negative_numbers = 0
        for i in range(0,len(nums)):
            if nums[i] < 0:
                negative_numbers +=1
        if negative_numbers % 2 == 0:
            return 1
        else:
            return -1