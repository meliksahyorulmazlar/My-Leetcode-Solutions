class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        total = 0
        greatest = max(nums)
        smallest = min(nums)
        total += greatest-smallest
        nums.remove(greatest)
        nums.remove(smallest)
        for num in nums:
            total += num-smallest
        return total