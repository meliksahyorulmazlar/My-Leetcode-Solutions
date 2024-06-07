class Solution:
    def generateTheString(self, n: int) -> str:
        # this checks if it is a power of 2
        if n == 2:
            return "xy"
        elif n > 0 and (n & (n - 1)) == 0:
            s1 = ((n//2)+1) * "a"
            s2 = ((n//2)-1) * "h"
            return s1 +s2
        elif n % 2 == 0 and n//2 % 2== 0:
            s1 = ((n//2)+1) * "a"
            s2 = ((n//2)-1) * "h"
            return s1 +s2
        elif n % 2 == 0:
            s1 = (n//2) * "a"
            s2 = (n//2) * "h"
            return s1+s2
        else:
            return n* "h"

