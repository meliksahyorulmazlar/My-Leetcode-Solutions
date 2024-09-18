class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            number = list(str(num))

            num = sum([int(i) for i in number])

        return num