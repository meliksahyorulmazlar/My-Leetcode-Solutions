class Solution(object):
    def sumBase(self, n, k):
        total = 0
        while n != 0:
            remainder = n %k
            n = n//k
            total += remainder
        return total

