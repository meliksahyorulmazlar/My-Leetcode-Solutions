class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if 0 >= n:
            return False
        is_true = True
        while is_true:
            if n> 1:
                remainder = n % 2
                if remainder != 0:
                    return False
                else:
                    n /= 2
            elif n == 1:
                return True