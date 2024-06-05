class Solution(object):
    def evenOddBit(self, n):
        bits = [0,0]
        count = 0
        while n != 0:
            remainder = n %2
            n = n//2
            if count %2 == 0 and remainder == 1:
                bits[0] +=1
                count +=1
            elif count %2 == 1 and remainder == 1:
                bits[1] += 1
                count +=1
            else:
                count +=1
        return bits

