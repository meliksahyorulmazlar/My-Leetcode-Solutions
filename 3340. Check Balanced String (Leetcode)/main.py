class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum([int(char) for char in num[0::2]]) == sum([int(char) for char in num[1::2]])