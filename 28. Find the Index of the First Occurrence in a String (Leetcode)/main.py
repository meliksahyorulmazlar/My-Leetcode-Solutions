class Solution(object):
    def strStr(self, haystack, needle):
        sentence = haystack.replace(needle, "$")
        for i in range(len(sentence)):
            if sentence[i] == "$":
                return i

        return -1