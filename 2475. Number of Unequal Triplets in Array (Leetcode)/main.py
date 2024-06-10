class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2,len(nums)):
                    if  j > i and k > j:
                        if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                            count += 1
        return count