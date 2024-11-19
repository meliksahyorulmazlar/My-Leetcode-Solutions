class Solution:
    def makeFancyString(self, s: str) -> str:
        output = ''
        char = s[0]
        for i in range(1, len(s)):
            new = s[i]
            if char[0] == new:
                if len(char) <= 2:
                    char += char
            else:
                if len(char) >= 3:
                    output += (2 * char[0])
                    char = new
                else:
                    output += char
                    char = new
        if len(char) >= 3:
            output += (2 * char[0])
            char = new
        else:
            output += char

        return output

