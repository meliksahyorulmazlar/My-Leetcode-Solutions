class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        number = original
        while number in nums:
            number = number * 2

        return number