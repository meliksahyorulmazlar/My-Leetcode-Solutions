class Solution:
    def greatestLetter(self, s: str) -> str:
        upper = []
        for char in s:
            if char.lower() in s and char.upper() in s:
                upper.append(char.upper())

        if len(upper) == 0:
            return ""
        else:
            return max(upper)
