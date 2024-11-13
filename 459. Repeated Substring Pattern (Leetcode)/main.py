class Solution(object):
    def repeatedSubstringPattern(self, s):
        length = len(s)
        for i in range(len(s) // 2):
            string = s[:i + 1]
            string_length = i + 1
            if string * (length // string_length) == s:
                return True

        return False