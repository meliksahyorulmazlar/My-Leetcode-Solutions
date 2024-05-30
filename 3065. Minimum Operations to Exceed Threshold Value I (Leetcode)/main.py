class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len([num for num in nums if num < k])