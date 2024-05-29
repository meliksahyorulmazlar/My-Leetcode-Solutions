class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        number = str(x)
        total = 0
        for i in range(len(number)):
            total += int(number[i])
        if x % total ==0:
            return total
        else:
            return -1
        