class Solution:
    def fractionAddition(self, expression: str) -> str:
        values = []

        string = ""
        multiplier = 1
        for i in range(len(expression)):
            char = expression[i]
            if char == "-" and i == 0:
                multiplier = -1
            elif char == "+" and i == 0:
                multiplier = 1
            elif char == "-" and i != 0:
                fraction = string.split("/")
                numerator = int(fraction[0]) * multiplier
                denominator = int(fraction[1])
                values.append(numerator / denominator)
                string = ""
                multiplier = -1
            elif char == "+" and i != 0:
                fraction = string.split("/")
                numerator = int(fraction[0]) * multiplier
                denominator = int(fraction[1])
                values.append(numerator / denominator)
                string = ""
                multiplier = 1
            else:
                string += char

        if len(string) >= 3:
            fraction = string.split("/")
            numerator = int(fraction[0]) * multiplier
            denominator = int(fraction[1])
            values.append(numerator / denominator)


        result = sum(values)
        if result % 1 == 0:
            return f"{int(result)}/1"

        denominator = 2
        while True:
            if (result*denominator)% 1== 0:
                break
            denominator += 1
        return f"{int(result*denominator)}/{denominator}"

sol = Solution()
x = sol.fractionAddition("7/9+9/5-2/1")
print(x)