class Solution:
    def reverse(self, x: int) -> int:
        lower_limit = pow(-2,31)
        upper_limit = pow(2,31)-1
        if x <0:
            number = -1*int("".join(list(str(x))[1::][::-1]))
            if number < lower_limit:
                return 0
            else:
                return number
        else:
            number = int("".join(list(str(x))[::-1]))
            if number > upper_limit:
                return 0
            else:
                return number
    

s = Solution()
x = s.reverse(x=123)
print(x)