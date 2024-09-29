class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        result = []

        for char in s:
            if char == "#":
                if result:
                    result.pop()
            else:
                result.append(char)

        output = []
        for char in t:
            if char == "#":
                if output:
                    output.pop()
            else:
                output.append(char)

        return result == output
