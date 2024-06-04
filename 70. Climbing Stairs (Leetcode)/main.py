class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2


        a = 1
        b = 2
        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return b
