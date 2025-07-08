class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This code finds the complement
        complements = {}

        for i, num in enumerate(nums):
            complement = target-num
            if complement in complements:
                return [complements[complement],i]
            else:
                complements[num] = i
