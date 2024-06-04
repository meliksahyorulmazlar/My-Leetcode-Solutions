class Solution(object):
    def singleNumber(self, nums):
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary.pop(num)
        for key in dictionary:
            return key  
