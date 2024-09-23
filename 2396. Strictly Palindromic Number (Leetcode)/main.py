class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            new_string = self.convert(n,i)
            result = self.check_palindrome(new_string)
            if result == False:
                return False
        return True

    def convert(self,number:int,base:int)->str:
        output = []

        while number != 0:
            remainder = number % base
            number = number//base
            output.append(str(remainder))
        string = "".join(output[::-1])
        return string

    def check_palindrome(self,string:str):
        if string == string[::-1]:
            return True
        else:
            return False