class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        not_found = True
        while not_found:
            num = n
            product = 1
            for n in str(n):
                product *= int(n)

            if product % t == 0:
                return num
            else:
                num += 1
                n = num
