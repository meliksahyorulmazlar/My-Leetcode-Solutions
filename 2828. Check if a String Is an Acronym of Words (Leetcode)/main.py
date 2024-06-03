class Solution(object):
    def isAcronym(self, words, s):
        return s == "".join([w[0] for w in words])
