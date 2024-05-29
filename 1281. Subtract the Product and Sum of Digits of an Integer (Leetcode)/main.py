class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        total = 0
        product = 1
        for i in range(len(str(n))):
            char = int(str(n)[i])
            total += char
            product *= char
        return product-total