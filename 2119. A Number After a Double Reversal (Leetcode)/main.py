class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == int(str(int(str(num)[::-1]))[::-1])
