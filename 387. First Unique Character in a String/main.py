class Solution:
    def firstUniqChar(self, s: str) -> int:
        original_characters = list(s)
        characters = []
        for char in original_characters:
            if char not in characters:
                characters.append(char)

        for char in characters:
            if s.count(char) == 1:
                return original_characters.index(char)

        return -1 
