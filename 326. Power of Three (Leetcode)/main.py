class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if 0 >=n:
            return False
        else:
            while n>1:
                remainder = n%3
                print(remainder)
                n = n/3
                if remainder != 0:
                    print(False)

            print(True)
        

sol = Solution()
sol.isPowerOfThree(27)