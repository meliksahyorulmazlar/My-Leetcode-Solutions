class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        greatest = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(i+2,len(nums)):
                    if k > j and j > i:
                        if nums[i] > 0 and nums[j] > 0 and nums[k] > 0:
                            product = (nums[i]-nums[j]) * nums[k]
                            if product > greatest:
                                greatest = product
        return greatest