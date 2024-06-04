class Solution(object):
    def matrixSum(self, nums):
        score = 0
        while len(nums[-1]) != 0:
            items = []
            for i in range(len(nums)):
                numbers = nums[i]
                greatest = max(numbers)
                items.append(greatest)
                numbers.remove(greatest)
            score += max(items)
        return score

