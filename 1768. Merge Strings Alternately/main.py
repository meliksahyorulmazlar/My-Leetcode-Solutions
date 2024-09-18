class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count1 = len(word1)
        count2 = len(word2)

        length = max(count1, count2)
        output = ""

        for i in range(length):
            if count1 != 0:
                output += word1[i]
                count1 -= 1

            if count2 != 0:
                output += word2[i]
                count2 -= 1

        return output
