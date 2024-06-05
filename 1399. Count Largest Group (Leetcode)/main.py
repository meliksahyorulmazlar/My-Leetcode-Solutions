class Solution(object):
    def countLargestGroup(self, n):
        dictionary = {}

        for i in range(1,n+1):
            total = sum([int(item) for item in list(str(i))])
            if total not in dictionary:
                dictionary[total] = [i]
            else:
                dictionary[total].append(i)
        greatest = max([len(dictionary[key]) for key in dictionary])
        count = 0
        for key in dictionary:
            if len(dictionary[key]) == greatest:
                count +=1
        return count

