class Solution:
    def solveEquation(self, equation: str) -> str:
        equations = equation.split("=")
        slope1, y1 = self.return_count(equations[0])
        slope2, y2 = self.return_count(equations[1])


        if slope1 == slope2 and y1 != y2:
            return "No solution"
        elif slope1 == slope2 and y1 == y2:
            return "Infinite solutions"
        else:
            left_side = slope1-slope2
            right_side = y2-y1
            right_side = right_side//left_side
            return f"x={right_side}"
    def return_count(self,equation:str)->tuple:
        slope = 0
        y_intercept = 0


        multiplier = 1
        string = ""

        for i in range(len(equation)):
            char = equation[i]
            if char == "+" and i == 0:
                multiplier = 1
            elif char == "-" and i == 0:
                multiplier = -1
            elif char == "+":
                if "x" in string:
                    if string == "x":
                        slope += 1*multiplier
                    else:
                        coefficient = int(string.replace("x",""))
                        slope += coefficient*multiplier
                else:
                    y_intercept += int(string)*multiplier
                multiplier = 1
                string = ""
            elif char == "-":
                if "x" in string:
                    if string == "x":
                        slope += 1 * multiplier
                    else:
                        coefficient = int(string.replace("x", ""))
                        slope += coefficient * multiplier
                else:
                    y_intercept += int(string) * multiplier
                multiplier = -1
                string = ""
            else:
                string += char
        if string:
            if "x" in string:
                if string == "x":
                    slope += 1 * multiplier
                else:
                    coefficient = int(string.replace("x", ""))
                    slope += coefficient * multiplier
            else:
                y_intercept += int(string) * multiplier

        return slope,y_intercept

sol = Solution()
x = sol.solveEquation("2x=x")
print(x)