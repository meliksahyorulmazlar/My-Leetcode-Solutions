class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        bits = []
        while n > 0:
            remainder = n % 2
            n = n // 2
            bits.append(remainder)
        total = 0
        for i in range(len(bits)):
            if bits[i] == 0:
                total += pow(2,i)
        return total
