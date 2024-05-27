class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string_form = str(x)
        new_string = ""
        for i in range(len(string_form) - 1, -1, -1):
            new_string += string_form[i]
        if string_form == new_string:
            return True
        else:
            return False




