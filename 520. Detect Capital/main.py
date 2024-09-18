class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        length = len(word)
        # check if all are upper-case
        count_total = sum([1 for char in word if char.isupper()])
        if count_total == length:
            return True

        # check if none are upper case
        count = sum([1 for char in word if char.islower()])
        if count == length:
            return True

        # check if only the first letter is capital
        if count_total == 1 and word[0].isupper():
            return True

        return False

