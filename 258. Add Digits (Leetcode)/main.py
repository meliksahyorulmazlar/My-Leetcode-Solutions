class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        number = str(num)
        while len(number) >1:
            number = [int(item) for item in list(number)]
            total = sum(number)
            number = str(total)
        number = int(number)
        return number