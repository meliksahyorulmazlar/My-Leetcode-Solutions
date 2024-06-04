class Solution(object):
    def repeatedCharacter(self, s):
        letters = list(s)
        dict = {}
        for letter in letters:
            if letter not in dict:
                dict[letter] = 1
            else:
                return letter
