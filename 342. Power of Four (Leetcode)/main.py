class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:

            while n != 1:
                remainder = n % 4
                n = n/4

                if remainder != 0:
                    return False
            return True
            
            
        