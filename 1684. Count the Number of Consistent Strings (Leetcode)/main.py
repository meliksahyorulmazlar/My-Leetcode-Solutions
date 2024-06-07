class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = list(allowed)
        count = 0
        for word in words:
            if len(word) == len([1 for char in word if char in allowed]):
                count += 1
        return count