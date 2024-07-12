class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        result = ""
        length = len(s)
        for i in range(length):
            index = (i+k)%length
            result += s[index]
        return result


