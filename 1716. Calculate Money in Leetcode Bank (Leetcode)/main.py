class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        for i in range(1, n + 1):
            if i % 7 == 0:
                total += (i // 7) + 6
            else:
                total += (i % 7) + (i // 7)
        return total
