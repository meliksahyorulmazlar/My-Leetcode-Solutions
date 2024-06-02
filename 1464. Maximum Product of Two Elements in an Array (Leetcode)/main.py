class Solution(object):
    def maxProduct(self, nums):
        n1 = max(nums)
        nums.remove(n1)
        n2 = max(nums)
        return (n1-1)*(n2-1)
