class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n == 2:
            return [1,1]
        else:
            for i in range(1,n):
                n2 = n-i
                if "0" not in str(i) and "0" not in str(n2):
                    return [i,n2]