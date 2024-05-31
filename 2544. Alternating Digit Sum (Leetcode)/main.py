class Solution:
    def alternateDigitSum(self, n: int) -> int:
        total = 0
        for i in range(len(str(n))):
            if i % 2 == 0:
                total += int(str(n)[i])
            else:
                total += (-1 *int(str(n)[i]))
        return total
