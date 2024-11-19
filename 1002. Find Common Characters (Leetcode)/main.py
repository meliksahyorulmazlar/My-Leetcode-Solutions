class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = []
        word = words[0]
        chars = list(set(word))
        result = []
        for char in chars:
            possible = []
            for word in words:
                if char not in word:
                    break
                else:
                    possible.append(word.count(char))
            if len(possible) == len(words):
                for i in range(min(possible)):
                    result.append(char)

        return result



