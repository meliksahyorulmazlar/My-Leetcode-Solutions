class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()[::-1]
        return " ".join(words)









