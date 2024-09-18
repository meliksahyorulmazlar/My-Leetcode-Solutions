class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        found = False
        count = 1
        while not found:

            square = count ** 2

            if square == num:
                return True
            elif square < num:
                count += 1
            else:
                return False


