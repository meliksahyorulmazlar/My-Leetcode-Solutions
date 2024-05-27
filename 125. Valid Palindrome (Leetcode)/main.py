class Solution:
    def isPalindrome(self, s: str) -> bool:
        string_list = [char.lower() for char in s if char.isalnum()]
        
        print(string_list)
        new_list = string_list[::-1]
        print(new_list)
        if new_list == string_list:
            return True
        else:
            return False