class Solution(object):
    def mostFrequentEven(self, nums):
        dictionary = {}
        for num in nums:
            parity = num % 2
            if parity == 0:
                if num not in dictionary:
                    dictionary[num] = 1
                else:
                    dictionary[num] +=1
        if len(dictionary) == 0:
            return -1
        else:
            result = sorted(dictionary.keys(),key= lambda x: (-dictionary[x],x))
            return result[0]