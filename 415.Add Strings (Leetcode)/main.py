class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        number1 = 0
        number2 = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            number1 += int(num1[i]) * pow(10,i)
        print(number1)
        for i in range(len(num2)):
            number2 += int(num2[i]) * pow(10,i)
        print(number2)
        return number1 + number2
    


sol = Solution()
sol.addStrings("11","123")
