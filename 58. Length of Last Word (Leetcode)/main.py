class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s.strip().split()[-1])
        return length
