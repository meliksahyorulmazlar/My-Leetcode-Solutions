class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        if num % 10 == 0:
            return False
        else:
            return True
