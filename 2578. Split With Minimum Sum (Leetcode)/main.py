class Solution:
    def splitNum(self, num: int) -> int:
        numbers = [int(number) for number in list(str(num))]
        num1 = ""
        num2 = ""
        for i in range(0,len(numbers)):
            number = min(numbers)
            numbers.remove(number)
            if i % 2 ==0:
                num1 += str(number)
            else:
                num2 += str(number)
        return int(num1)+int(num2)
