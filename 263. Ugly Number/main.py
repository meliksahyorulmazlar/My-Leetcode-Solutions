class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        while n!= 1:
            if n % 2 == 0:
                n = n//2
                print(n)
            elif n % 3 == 0:
                n = n//3
                print(n)
            elif n % 5 == 0:
                n = n//5
                print(n)
            else:
                return False
        return True
