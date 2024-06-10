class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        sums = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2,len(nums)):
                    if k > j and j > i:
                        if nums[i] < nums[j] and nums[k] < nums[j]:
                                sums.append(nums[i] + nums[j] + nums[k])
        if len(sums) ==0:
            return -1
        else:
            return min(sums)

