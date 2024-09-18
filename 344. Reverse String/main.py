class Solution:
    def reverseString(self, s: List[str]) -> None:
        length = len(s)

        count = length // 2

        for i in range(count):
            first = s[i]
            last = s[length - 1 - i]
            s[i], s[length - 1 - i] = last, first



