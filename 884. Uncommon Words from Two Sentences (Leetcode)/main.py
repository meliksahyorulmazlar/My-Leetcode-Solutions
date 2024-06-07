class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        word_count = {}
        s1 = s1.split()
        s2 = s2.split()
        words = s1+s2
        for word in words:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        chosen = []
        for key in word_count:
            if word_count[key] == 1:
                chosen.append(key)
        return chosen







sol = Solution()
sol.uncommonFromSentences("apple apple","banana")