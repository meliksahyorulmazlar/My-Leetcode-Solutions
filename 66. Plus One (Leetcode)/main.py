class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(d) for d in digits]
        number = int("".join(digits))
        number = str(number + 1)
        return [int(n) for n in list(number)]