class Solution(object):
    def triangularSum(self, nums):

        while len(nums) > 1:
            items = []
            for i in range(len(nums) - 1):
                value = (nums[i] + nums[i + 1]) % 10
                items.append(value)
            nums = items
        return nums[0]
