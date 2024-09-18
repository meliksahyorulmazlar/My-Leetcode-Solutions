class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while count < 15 and n != 1:
            number = list(str(n))

            n = sum([pow(int(n), 2) for n in number])
            count += 1

        if count == 15:
            return False
        else:
            return True
