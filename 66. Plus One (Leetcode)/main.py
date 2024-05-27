class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        digits = digits[::-1]
        for i in range(len(digits)):
            digit = digits[i]
            total += digit*pow(10,i)
        total += 1
        total = list(str(total))
        return [int(item) for item in total]