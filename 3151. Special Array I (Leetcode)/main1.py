class Solution(object):
    def isArraySpecial(self, nums):
        for i in range(0,len(nums)-1):
            p1 = nums[i] %2
            p2 = nums[i+1] %2
            if p1 == p2:
                return False
        return True