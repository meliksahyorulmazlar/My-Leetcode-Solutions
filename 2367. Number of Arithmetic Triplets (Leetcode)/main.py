class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2,len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count += 1
        return count
