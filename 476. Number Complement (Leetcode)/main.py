class Solution:
    def findComplement(self, num: int) -> int:
        bits = []
        while num > 0:
            remainder = num % 2
            num = num // 2
            bits.append(remainder)
        total = 0
        for i in range(len(bits)):
            if bits[i] == 0:
                total += pow(2,i)
        return total






