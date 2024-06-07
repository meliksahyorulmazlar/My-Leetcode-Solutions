class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return (len([1 for char in s if char == letter]) * 100) // len(s)

