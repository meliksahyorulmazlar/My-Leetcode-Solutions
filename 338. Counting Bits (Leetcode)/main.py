class Solution(object):
    def countBits(self, n):
        result = []

        for i in range(0,n+1):
            if i == 0:
                result.append(0)
            else:
                count = 0
                while i != 0:
                    remainder = i % 2
                    i = i//2
                    if remainder == 1:
                        count +=1
                result.append(count)
        return result

