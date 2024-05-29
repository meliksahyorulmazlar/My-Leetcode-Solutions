class Solution:
    def averageValue(self, nums: List[int]) -> int:
        nums = [num for num in nums if num % 3 == 0 and num % 2 == 0]
        try:
            return int(sum(nums)/len(nums))
        except ZeroDivisionError:
            return 0