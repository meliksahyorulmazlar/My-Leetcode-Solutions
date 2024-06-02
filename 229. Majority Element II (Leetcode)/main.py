class Solution(object):
    def majorityElement(self, nums):
        dictionary = {}
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] =1
        amount = len(nums)/3
        output = []
        for key in dictionary:
            if dictionary[key] > amount:
                output.append(key)
        return output

