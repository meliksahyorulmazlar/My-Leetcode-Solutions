class Solution(object):
    def maxNumberOfBalloons(self, text):
        dictionary = {}
        for char in text:
            if char in "balloon":
                if char not in dictionary:
                    dictionary[char] = 1
                else:
                    dictionary[char] += 1

        for char in 'balloon':
            if char not in dictionary:
                return 0

        char = 'o'
        dictionary[char] = dictionary[char] // 2

        char = 'l'
        dictionary[char] = dictionary[char] // 2

        return min(list(dictionary.values()))