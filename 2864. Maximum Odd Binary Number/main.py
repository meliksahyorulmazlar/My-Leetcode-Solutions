class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero_count = s.count("0")

        one_count = s.count("1")

        if one_count == 1:
            return ("0"*zero_count)+"1"
        else:
            return ("1"*(one_count-1))+("0"*zero_count) + "1"
