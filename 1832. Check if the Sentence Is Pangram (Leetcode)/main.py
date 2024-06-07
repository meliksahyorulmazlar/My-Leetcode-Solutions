class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for char in sentence:
            seen.add(char)
        if len(seen) == 26:
            return True
        else:
            return False
