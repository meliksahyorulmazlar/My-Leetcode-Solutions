class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        char = s[0]
        for i in range(1,len(s)):
            new_char = s[i]
            if char.lower() != new_char.lower():
                count += 1
            char = new_char
        return count
