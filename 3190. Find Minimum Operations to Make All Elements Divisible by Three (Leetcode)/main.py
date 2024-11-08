class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if num % 3 == 0:
                count += 0
            elif num % 3 == 1:
                count += 1
            elif num % 3 == 2:
                count += 1
        return count
