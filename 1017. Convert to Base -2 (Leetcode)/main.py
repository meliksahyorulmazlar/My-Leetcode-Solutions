class Solution(object):
    def baseNeg2(self, n):
        if n == 0:
            return "0"
        bits = []
        while n != 0:
            remainder = n % -2
            n = n // -2

            if remainder < 0:
                remainder += 2
                n += 1
            bits.append(str(remainder))
        return "".join(bits[::-1])


