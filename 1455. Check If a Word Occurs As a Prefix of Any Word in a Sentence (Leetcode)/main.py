class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()
        for i in range(len(words)):
            if searchWord == words[i][0:len(searchWord)]:
                return i+1
        return -1
