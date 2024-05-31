class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        return max([i for i in range(1,largest+1) if largest % i == 0 and smallest % i == 0])
