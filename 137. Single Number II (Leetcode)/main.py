class Solution(object):
    def singleNumber(self, nums):
        dictionary = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] +=1
        for key in dictionary:
            if dictionary[key] ==1:
                return key
