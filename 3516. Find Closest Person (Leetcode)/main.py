class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_amount = abs(z-x)
        y_amount = abs(z-y)
        if x_amount == y_amount:
            return 0
        elif x_amount < y_amount:
            return 1
        else:
            return 2