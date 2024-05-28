class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        for item in nums:
            if item in dictionary:
                dictionary[item] += 1
            else:
                dictionary[item] = 1
        for key in dictionary:
            if dictionary[key] >= len(nums)/2:
                return key

