class Solution(object):
    def xorOperation(self, n, start):
        xor = start
        for i in range(1, n):
            amount = start + (2 * i)
            xor ^= amount
        return xor
