class Solution:
    def countDigits(self, num: int) -> int:
        return sum([1 for item in list(str(num)) if num % int(item) == 0])

