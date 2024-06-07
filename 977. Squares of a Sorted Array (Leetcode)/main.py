class Solution(object):
    def sortedSquares(self, nums):
        return sorted([pow(num, 2) for num in nums])

