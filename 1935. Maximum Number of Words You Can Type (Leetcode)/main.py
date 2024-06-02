class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        words = text.split()
        letters = list(brokenLetters)
        countable = 0
        for word in words:
            count = 0
            for letter in letters:
                if letter not in word:
                    count += 1
            if len(letters) == count:
                countable += 1

        return countable