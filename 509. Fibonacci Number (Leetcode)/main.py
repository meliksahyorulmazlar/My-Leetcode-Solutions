class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            a = 1
            b = 1
            for i in range(n-2):
                c = b
                b = a+b
                a = c
            return b

s
