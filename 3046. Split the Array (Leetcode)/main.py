class Solution(object):
    def isPossibleToSplit(self, nums):
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                if dict[num] > 2:
                    return False
        return True

