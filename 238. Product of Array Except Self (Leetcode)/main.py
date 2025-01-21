class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) >= 2:
            return len(nums) * [0]
        elif nums.count(0) == 1:
            product = 1
            index = None
            for i in range(len(nums)):
                num = nums[i]
                if num != 0:
                    product *= num
                    nums[i] = 0
                elif num == 0:
                    index = i
            nums[index] = product
        else:
            product = 1
            for i in range(len(nums)):
                product *= nums[i]

            for i in range(len(nums)):
                nums[i] = product // nums[i]

        return nums






