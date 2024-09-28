class Solution:
    def removeVowels(self, s: str) -> str:
        return s.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "")
