class Solution(object):
    def restoreString(self, s, indices):
        string = ""
        for i in range(len(indices)):
            index = indices.index(i)
            string += s[index]
        return string
