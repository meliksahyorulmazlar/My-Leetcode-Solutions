class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums = [num for num in nums if nums.count(num)>2]
        if len(nums) >=1:
            return False
        else:
            return True