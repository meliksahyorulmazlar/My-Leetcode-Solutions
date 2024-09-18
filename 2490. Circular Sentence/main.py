class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        if len(words) == 1:
            if sentence[0] == sentence[-1]:
                return True
            else:
                return False

        for i in range(0, len(words)):
            if i == len(words) - 1:
                if words[len(words) - 1][-1] != words[0][0]:
                    return False
            else:
                if words[i][-1] != words[i + 1][0]:
                    return False

        return True



