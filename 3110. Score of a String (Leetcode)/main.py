class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        for i in range(0,len(s)-1):
            char1 = s[i]
            char2 = s[i+1]
            score1 = ord(char1)
            score2 = ord(char2)
            total += abs(score1-score2)
        return total