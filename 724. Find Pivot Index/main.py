class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
                right_sum = sum(nums[i + 1:])
                if left_sum == right_sum:
                    return 0
            elif i == len(nums) - 1:
                left_sum = sum(nums[0:i])
                right_sum = 0
                if left_sum == right_sum:
                    return i
            else:
                left_sum = sum(nums[0:i])
                right_sum = sum(nums[i + 1:])
                if left_sum == right_sum:
                    return i
        return -1




