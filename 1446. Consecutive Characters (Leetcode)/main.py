class Solution(object):
    def maxPower(self, s):
        record = [1]
        count = 1
        char = s[0]
        for i in range(1,len(s)):
            new_char = s[i]
            if new_char == char:
                count +=1
                record.append(count)
            else:
                count = 1
                char = new_char
        return max(record)